#!/usr/bin/env python
# Put pointers from the provided files into the pointers table
# This will overwrite the pointer if it already exists in the table
import json

import fire
from aws_session_assume import get_boto_session

from nrlf.core.dynamodb.model import DocumentPointer
from nrlf.core.logger import logger
from nrlf.producer.fhir.r4.model import DocumentReference

logger.setLevel("ERROR")


def _put_pointers_from_files(
    *filenames, env: str = "dev", table_name: str | None = None
):
    docrefs: list[DocumentReference] = []
    print("Reading docrefs from files...")
    for filename in filenames:
        with open(filename) as f:
            docref_json = json.load(f)
            docref = DocumentReference.model_validate(docref_json)
            docrefs.append(docref)

    session = get_boto_session(env)
    dynamodb = session.resource("dynamodb")
    if not table_name:
        table_name = f"nhsd-nrlf--{env}-pointers-table"
    table = dynamodb.Table(table_name)

    for docref in docrefs:
        try:
            print(f"Putting {docref.id}....")
            pointer = DocumentPointer.from_document_reference(docref)
            table.put_item(Item=pointer.model_dump())
        except Exception as e:
            print(f"Unable to put pointer for {docref.id}. Error: {e}")


if __name__ == "__main__":
    fire.Fire(_put_pointers_from_files)
