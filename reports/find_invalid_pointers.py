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
    Find pointers in the given table that are invalid.
    Parameters:
    - table_name: The name of the pointers table to use.
    """

    print(f"Finding invalid pointers in table {table_name}....")  # noqa

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
            print(".", end="", flush=True)  # noqa

        if total_scanned_count % 100000 == 0:
            print(  # noqa
                f"scanned={total_scanned_count} invalid={len(invalid_pointers)}"
            )

    end_time = datetime.now(tz=timezone.utc)

    print(" Done")  # noqa

    print("Writing invalid_pointers to file ./invalid_pointers.txt ...")  # noqa
    with open("invalid_pointers.txt", "w") as f:
        for _id, err in invalid_pointers:
            f.write(f"{_id}: {err}\n")

    return {
        "invalid_pointers": len(invalid_pointers),
        "scanned_count": total_scanned_count,
        "took-secs": timedelta.total_seconds(end_time - start_time),
    }


if __name__ == "__main__":
    fire.Fire(_find_invalid_pointers)
