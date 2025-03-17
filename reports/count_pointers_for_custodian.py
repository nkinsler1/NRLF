from datetime import datetime, timedelta, timezone
from typing import Any, Optional

import boto3
import fire

dynamodb = boto3.client("dynamodb")
paginator = dynamodb.get_paginator("scan")


def _count_pointers(
    table_name: str, ods_code: str, created_date: Optional[str] = None
) -> dict[str, float]:
    """
    Count the number of pointers for a given custodian (ODS code) in the pointers table.
    Parameters:
    - table_name: The name of the pointers table to use.
    - ods_code: The custodian ODS code to find pointers for.
    - created_date: The created date to filter pointers on. (optional)
    """

    print(f"Counting pointers for {ods_code} in table {table_name}....")  # noqa

    params: dict[str, Any] = {
        "TableName": table_name,
        "FilterExpression": "custodian = :ods_code",
        "ExpressionAttributeValues": {":ods_code": {"S": ods_code}},
        "Select": "COUNT",
        "PaginationConfig": {"PageSize": 100},
    }

    if created_date:
        params["FilterExpression"] += " AND starts_with(created_on, :created_date)"
        params["ExpressionAttributeValues"][":created_date"] = {"S": created_date}

    custodian_pointers_count = 0
    total_scanned_count = 0

    start_time = datetime.now(tz=timezone.utc)

    for page in paginator.paginate(**params):
        custodian_pointers_count += page["Count"]
        total_scanned_count += page["ScannedCount"]

        if total_scanned_count % 1000 == 0:
            print(".", end="", flush=True)  # noqa

    end_time = datetime.now(tz=timezone.utc)

    print(" Done")  # noqa
    return {
        "items_found": custodian_pointers_count,
        "scanned_count": total_scanned_count,
        "took-secs": timedelta.total_seconds(end_time - start_time),
    }


if __name__ == "__main__":
    fire.Fire(_count_pointers)
