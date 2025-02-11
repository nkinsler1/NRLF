import json
import os
from datetime import datetime, timedelta, timezone
from typing import Any

import boto3
import fire

from nrlf.consumer.fhir.r4.model import DocumentReference
from nrlf.core.constants import PointerTypes
from nrlf.core.logger import logger
from nrlf.core.utils import create_fhir_instant
from nrlf.core.validators import DocumentReferenceValidator

dynamodb = boto3.client("dynamodb")
paginator = dynamodb.get_paginator("scan")

logger.setLevel("ERROR")

type_to_name = {pointer_type.value: pointer_type.name for pointer_type in PointerTypes}


def _redact_pointers(src_path: str, dest_path: str) -> None:
    """
    Redact pointers in .json files in from the source path and write the redacted pointer to the destination path.
    Parameters:
    - src_path: The path to the source directory containing the pointers.
    - dest_path: The path to the destination directory to write the redacted pointers.
    """
    src_pointer_files = [f for f in os.listdir(src_path) if f.endswith(".json")]

    for src_pointer_file in src_pointer_files:
        print("Reading", src_pointer_file)
        with open(f"{src_path}/{src_pointer_file}", "r") as f:
            pointer_data = f.read()

        docref = DocumentReference.model_validate_json(pointer_data)

        ods_code = docref.custodian.identifier.value
        type_coding = docref.type.coding[0]
        pointer_type = type_to_name[f"{type_coding.system}|{type_coding.code}"]

        mock_timestamp = create_fhir_instant()
        docref.meta.lastUpdated = mock_timestamp
        docref.date = mock_timestamp

        mock_id = f"c2a99222-eb50-4451-ad6e-1e951627800e"
        docref.subject.identifier.value = "9999999999"
        docref.id = f"{ods_code}-{mock_id}"
        if docref.masterIdentifier:
            docref.masterIdentifier.value = f"mid_{mock_id}"
        if docref.relatesTo:
            for relates_to in docref.relatesTo:
                relates_to.target.identifier.value = f"rel_{mock_id}"

        for content in docref.content:
            if content.attachment.url.startswith("ssp://"):
                content.attachment.url = "ssp://content.test.local/content"
            else:
                content.attachment.url = "https://content.test.local/content"
            content.attachment.creation = mock_timestamp
        if docref.context.related:
            for related in docref.context.related:
                related.identifier.value = "012345678910"
        if docref.context.period:
            if docref.context.period.start:
                docref.context.period.start = mock_timestamp
            if docref.context.period.end:
                docref.context.period.end = mock_timestamp

        month_year = datetime.now().strftime("%b%y")
        filename = f"{dest_path}/{ods_code}_{pointer_type}_{month_year}.json"

        print("Writing", filename)
        with open(filename, "w") as f:
            f.write(docref.model_dump_json(indent=2, exclude_unset=True))


if __name__ == "__main__":
    fire.Fire(_redact_pointers)
