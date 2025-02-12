from datetime import datetime, timedelta, timezone
from typing import Any

import boto3
import fire

from nrlf.consumer.fhir.r4.model import DocumentReference
from nrlf.core.logger import logger
from nrlf.core.validators import DocumentReferenceValidator

dynamodb = boto3.client("dynamodb")
paginator = dynamodb.get_paginator("scan")
resource = boto3.resource("dynamodb")

logger.setLevel("ERROR")


def _validate_document(document: str):
    docref = DocumentReference.model_validate_json(document)

    validator = DocumentReferenceValidator()
    result = validator.validate(data=docref)

    if not result.is_valid:
        raise RuntimeError("Failed to validate document: " + str(result.issues))


def _find_invalid_pointers(table_name: str) -> dict[str, Any]:
    print(f"Finding invalid pointers to delete in table {table_name}....")

    params: dict[str, Any] = {
        "TableName": table_name,
        "PaginationConfig": {"PageSize": 50},
        "FilterExpression": "created_on < :date",
        "ExpressionAttributeValues": {
            ":date": {"S": "2025-01-20T00:00:00.000000+0000"}
        }
    }

    invalid_pointers = []
    total_scanned_count = 0

    start_time = datetime.now(tz=timezone.utc)

    for page in paginator.paginate(**params):
        for item in page["Items"]:
            pointer_id = item.get("id", {}).get("S")
            created_on = item.get("created_on", {}).get("S")
            # parse datetime from created_on string
            created_on = datetime.strptime(created_on, "%Y-%m-%dT%H:%M:%S.%f%z")
            if created_on > datetime(2025, 1, 20, tzinfo=timezone.utc):
                continue
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

    if len(invalid_pointers) > 0:
        print("Writing invalid pointers IDs to file ./invalid_pointers.txt ...")
        with open("invalid_pointers.txt", "w") as f:
            for _id, err in invalid_pointers:
                f.write(f"{_id}: {err}\n")

    return {
        "invalid_pointers": invalid_pointers,
        "scanned_count": total_scanned_count,
        "find-took-secs": timedelta.total_seconds(end_time - start_time),
    }


def _delete_pointers(table_name: str, pointers_to_delete: list[str]) -> dict[str, Any]:
    """
    Delete the provided pointers from the given table.
    """
    start_time = datetime.now(tz=timezone.utc)

    print("Deleting invalid pointers...")
    pointers_deleted = 0
    failed_to_delete = 0

    for _batch_id in range(0, len(pointers_to_delete), 25):
        batch = [
            {
                "DeleteRequest": {
                    "Key": {
                        "pk": {"S": f"D#{pointer_id}"},
                        "sk": {"S": f"D#{pointer_id}"},
                    }
                }
            }
            for pointer_id in pointers_to_delete[_batch_id : _batch_id + 25]
        ]

        result = dynamodb.batch_write_item(RequestItems={table_name: batch})

        unprocessed_items = len(result.get("UnprocessedItems", []))
        pointers_deleted += len(batch) - unprocessed_items
        failed_to_delete += unprocessed_items
        if pointers_deleted % 1000 == 0:
            print(".", end="", flush=True)

    end_time = datetime.now(tz=timezone.utc)

    print(" Done")
    return {
        "pointers_to_delete": len(pointers_to_delete),
        "deleted_pointers": pointers_deleted,
        "failed_deletes": failed_to_delete,
        "deletes-took-secs": timedelta.total_seconds(end_time - start_time),
    }


def _find_and_delete_invalid_pointers(table_name: str) -> dict[str, float | int]:
    """
    Find and delete any pointers in the given table that are invalid based on the FHIR model and NRLF validators.
    Parameters:
    - table_name: The name of the pointers table to find and delete pointer from.
    """
    find_result = _find_invalid_pointers(table_name)

    if len(find_result["invalid_pointers"]) == 0:
        return {
            "invalid_pointers": 0,
            "scanned_count": find_result["scanned_count"],
            "find-took-secs": find_result["find-took-secs"],
        }

    confirmation_input = input(
        "Would you like to delete all the invalid pointers? (yes/no): "
    )
    if confirmation_input != "yes":
        print("Invalid pointers NOT deleted.")
        find_result.pop("invalid_pointers")
        return find_result

    pointers_to_delete = [_id for _id, _ in find_result["invalid_pointers"]]

    delete_result = _delete_pointers(table_name, pointers_to_delete)

    find_result.pop("invalid_pointers")

    return {**find_result, **delete_result}


def _fix_invalid_pointers(table_name: str) -> dict[str, Any]:
    print(f"Finding and fixing invalid pointers in table {table_name}....")

    params: dict[str, Any] = {
        "TableName": table_name,
        "PaginationConfig": {"PageSize": 50},
        "FilterExpression": "created_on < :date",
        "ExpressionAttributeValues": {
            ":date": {"S": "2025-01-20T00:00:00.000000+0000"}
        }
    }

    fixed_pointers = []
    total_scanned_count = 0
    total_fixed_count = 0

    start_time = datetime.now(tz=timezone.utc)

    for page in paginator.paginate(**params):
        for item in page["Items"]:
            pointer_id = item.get("id", {}).get("S")
            created_on = item.get("created_on", {}).get("S")
            # parse datetime from created_on string
            created_on = datetime.strptime(created_on, "%Y-%m-%dT%H:%M:%S.%f%z")
            if created_on > datetime(2025, 1, 20, tzinfo=timezone.utc):
                continue
            document = item.get("document", {}).get("S", "")
            try:
                docref = DocumentReference.model_validate_json(document)
                if (
                    docref.type.coding[0].display == "Mental Health Crisis plan"
                ):
                    #print(f"Fixing document {pointer_id}")
                    docref.type.coding[0].display = "Mental health crisis plan"
                    resource.Table(table_name).update_item(
                        Key={"pk": f"D#{pointer_id}", "sk": f"D#{pointer_id}"},
                        UpdateExpression="SET document = :d",
                        ExpressionAttributeValues={":d": docref.json()},
                    )
                    fixed_pointers.append(pointer_id)
                    total_fixed_count += 1
            except Exception as exc:
                print(f"Failed to fix document {pointer_id}: {exc}")

        total_scanned_count += page["ScannedCount"]

        if total_fixed_count % 100 == 0:
            print("x", end="", flush=True)
        
        if total_scanned_count % 1000 == 0:
            print(".", end="", flush=True)

        if total_scanned_count % 100000 == 0:
            print(f"scanned={total_scanned_count} fixed={len(fixed_pointers)}")

    end_time = datetime.now(tz=timezone.utc)

    print(f" Done. Fixed {len(fixed_pointers)} invalid pointers")

    #save fixed pointers to file
    if len(fixed_pointers) > 0:
        print("Writing fixed pointers IDs to file ./fixed_pointers.txt ...")
        with open("fixed_pointers.txt", "w") as f:
            for _id in fixed_pointers:
                f.write(f"{_id}\n")

    return {
        "fixed_pointers": fixed_pointers,
        "scanned_count": total_scanned_count,
        "fix-took-secs": timedelta.total_seconds(end_time - start_time),
    }


def _fix_invalid_pointers_from_file(table_name: str, file_path: str) -> dict[str, Any]:
    print(f"Fixing invalid pointers from file {file_path} in table {table_name}....")

    with open(file_path, "r") as f:
        pointer_ids = [line.split(":")[0] for line in f.readlines()]

    fixed_pointers = []
    total_fixed_count = 0

    start_time = datetime.now(tz=timezone.utc)

    for pointer_id in pointer_ids:
        try:
            response = dynamodb.get_item(
                TableName=table_name,
                Key={"pk": {"S": f"D#{pointer_id}"}, "sk": {"S": f"D#{pointer_id}"}}
            )
            item = response.get("Item")
            if not item:
                print(f"Pointer {pointer_id} not found.")
                continue

            document = item.get("document", {}).get("S", "")

            # if "https://fhir.nhs.uk/STU3/CodeSystem/NRL-FormatCode-1" in document:
            #     document = document.replace(
            #         "https://fhir.nhs.uk/STU3/CodeSystem/NRL-FormatCode-1",
            #         "https://fhir.nhs.uk/England/CodeSystem/England-NRLFormatCode",
            #     )
            #     resource.Table(table_name).update_item(
            #         Key={"pk": f"D#{pointer_id}", "sk": f"D#{pointer_id}"},
            #         UpdateExpression="SET document = :d",
            #         ExpressionAttributeValues={":d": document},
            #     )
            #     fixed_pointers.append(pointer_id)
            #     total_fixed_count += 1

            docref: DocumentReference = DocumentReference.model_validate_json(document)
            if docref.content[0].attachment.contentType.startswith("application/pdf") and len(docref.content[0].attachment.contentType) > len("application/pdf"):
                docref.content[0].attachment.contentType = "application/pdf"
                resource.Table(table_name).update_item(
                    Key={"pk": f"D#{pointer_id}", "sk": f"D#{pointer_id}"},
                    UpdateExpression="SET document = :d",
                    ExpressionAttributeValues={":d": docref.json()},
                )
                fixed_pointers.append(pointer_id)
                total_fixed_count += 1
       
            if docref.content[0].attachment.url.startswith("ssp://") and docref.content[0].attachment.contentType != "application/pdf":
                docref.content[0].attachment.contentType = "application/pdf"
                resource.Table(table_name).update_item(
                    Key={"pk": f"D#{pointer_id}", "sk": f"D#{pointer_id}"},
                    UpdateExpression="SET document = :d",
                    ExpressionAttributeValues={":d": docref.json()},
                )
                fixed_pointers.append(pointer_id)
                total_fixed_count += 1

            if docref.content[0].attachment.contentType == "application/pdf" and docref.content[0].attachment.url.endswith("pdf"):
                if docref.content[0].attachment.url.startswith("https://"):
                    docref.content[0].attachment.url.replace(("https://"), ("ssp://"))
                
                if docref.content[0].format.code == "urn:nhs-ic:record-contact" or docref.content[0].format.display == "Contact details (HTTP Unsecured)":
                    docref.content[0].format.code = "urn:nhs-ic:unstructured"
                    docref.content[0].format.display = "Unstructured Document"
                resource.Table(table_name).update_item(
                    Key={"pk": f"D#{pointer_id}", "sk": f"D#{pointer_id}"},
                    UpdateExpression="SET document = :d",
                    ExpressionAttributeValues={":d": docref.json()},
                )
                fixed_pointers.append(pointer_id)
                total_fixed_count += 1

        except Exception as exc:
            print(f"Failed to fix document {pointer_id}: {exc}")

        if total_fixed_count % 100 == 0:
            print("x", end="", flush=True)

    end_time = datetime.now(tz=timezone.utc)

    print(f" Done. Fixed {len(fixed_pointers)} invalid pointers")

    if len(fixed_pointers) > 0:
        print("Writing fixed pointers IDs to file ./fixed_pointers_from_file.txt ...")
        with open("fixed_pointers_from_file.txt", "w") as f:
            for _id in fixed_pointers:
                f.write(f"{_id}\n")

    return {
        "fixed_pointers": fixed_pointers,
        "total_fixed_count": total_fixed_count,
        "fix-took-secs": timedelta.total_seconds(end_time - start_time),
    }

if __name__ == "__main__":
    fire.Fire({
        "find_and_delete_invalid_pointers": _find_and_delete_invalid_pointers,
        "fix_invalid_pointers": _fix_invalid_pointers,
        "find_invalid_pointers": _find_invalid_pointers,
        "fix_invalid_pointers_from_file": _fix_invalid_pointers_from_file,
    })
