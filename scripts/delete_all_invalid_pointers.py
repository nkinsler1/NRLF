from datetime import datetime, timedelta, timezone
from typing import Any

import boto3
import fire

from nrlf.consumer.fhir.r4.model import DocumentReference
from nrlf.core.logger import logger
from nrlf.core.validators import DocumentReferenceValidator

dynamodb = boto3.client("dynamodb")
paginator = dynamodb.get_paginator("scan")

logger.setLevel("ERROR")


def _validate_document(document: str):
    docref = DocumentReference.model_validate_json(document)

    validator = DocumentReferenceValidator()
    result = validator.validate(data=docref)

    if not result.is_valid:
        raise RuntimeError("Failed to validate document: " + str(result.issues))


def _find_invalid_pointers(table_name: str) -> dict[str, float | int]:
    """
    Find and delete pointers in the given table that are invalid based on the FHIR model and NRLF validators.
    Parameters:
    - table_name: The name of the pointers table to find and delete pointer from.
    """

    print(f"Finding invalid pointers to delete in table {table_name}....")

    params: dict[str, Any] = {
        "TableName": table_name,
        "PaginationConfig": {"PageSize": 50},
    }

    invalid_pointers = []
    total_scanned_count = 0

    start_time = datetime.now(tz=timezone.utc)

    for page in paginator.paginate(**params):
        for item in page["Items"]:
            pointer_id = item.get("id", {}).get("S")
            document = item.get("document", {}).get("S", "")
            try:
                _validate_document(document)
            except Exception as exc:
                invalid_pointers.append((pointer_id, exc))

        total_scanned_count += page["ScannedCount"]

        if total_scanned_count % 1000 == 0:
            print(".", end="", flush=True)

        if total_scanned_count % 100000 == 0:
            print(f"scanned={total_scanned_count} invalid={len(invalid_pointers)}")

    end_time = datetime.now(tz=timezone.utc)

    print(f" Done. Found {len(invalid_pointers)} invalid pointers")

    if len(invalid_pointers) == 0:
        return {
            "invalid_pointers": 0,
            "scanned_count": total_scanned_count,
            "took-secs": timedelta.total_seconds(end_time - start_time),
        }

    print("Writing invalid pointers IDs to file ./invalid_pointers.txt ...")
    with open("invalid_pointers.txt", "w") as f:
        for _id, err in invalid_pointers:
            f.write(f"{_id}: {err}\n")

    confirmation_input = input(
        "Would you like to delete all the invalid pointers? (yes/no): "
    )
    if confirmation_input != "yes":
        print("Invalid pointers NOT deleted.")
        return {
            "invalid_pointers": len(invalid_pointers),
            "scanned_count": total_scanned_count,
            "took-secs": timedelta.total_seconds(end_time - start_time),
        }

    print("Deleting invalid pointers...")
    pointers_deleted = 0
    for _id, _ in invalid_pointers:
        try:
            item_key = {"S": f"D#{_id}"}
            dynamodb.delete_item(
                TableName=table_name,
                Key={"pk": item_key, "sk": item_key},
                ReturnValues="NONE",
            )

            pointers_deleted += 1

            if pointers_deleted % 1000 == 0:
                print(".", end="", flush=True)
        except Exception as exc:
            print(f"Failed to delete pointer {_id}: {exc}")

    end_time = datetime.now(tz=timezone.utc)

    print(" Done")
    return {
        "invalid_pointers_total": len(invalid_pointers),
        "invalid_pointers_deleted": pointers_deleted,
        "scanned_count": total_scanned_count,
        "took-secs": timedelta.total_seconds(end_time - start_time),
    }


if __name__ == "__main__":
    fire.Fire(_find_invalid_pointers)
