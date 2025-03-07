#!/usr/bin/env python
# Set supersede info on a pointer
import json

import aws_session_assume
import fire

from nrlf.core.dynamodb.model import DocumentPointer
from nrlf.core.logger import logger
from nrlf.producer.fhir.r4.model import (
    DocumentReference,
    DocumentReferenceRelatesTo,
    Identifier,
    Reference,
)

logger.setLevel("ERROR")


def _set_pointer_supersede_info(
    pointer_id: str,
    supersede_pointer_id: str,
    delete_superceded: bool = False,
    env: str = "dev",
    table_name: str | None = None,
):
    session = aws_session_assume.get_boto_session(env)
    dynamodb = session.resource("dynamodb")

    if not table_name:
        table_name = f"nhsd-nrlf--{env}-pointers-table"
    table = dynamodb.Table(table_name)

    print(
        f"Setting pointer {pointer_id} in {table_name} to supersede {supersede_pointer_id}...."
    )

    try:
        doc_key = f"D#{pointer_id}"
        print(f"Getting {pointer_id}...")
        result = table.get_item(
            Key={"pk": doc_key, "sk": doc_key},
        )
    except Exception as e:
        print(f"Unable to get pointer. Error: {e}")
        return

    if "Item" not in result:
        print(f"Unable to set superseded info. Pointer {pointer_id} not found.")
        return

    item = result["Item"]

    try:
        pointer = DocumentPointer.model_validate({"_from_dynamo": True, **item})
    except Exception as e:
        print(f"Could not validate pointer from table. Error: {e}")
        return

    doc_ref = DocumentReference.model_validate_json(pointer.document)

    if not doc_ref.relatesTo:
        doc_ref.relatesTo = []
    else:
        for relatesTo in doc_ref.relatesTo:
            if relatesTo.code == "replaces":
                print(
                    f"Unable to add supersede info as pointer is already superseding a pointer: {relatesTo}"
                )
                return

    doc_ref.relatesTo.append(
        DocumentReferenceRelatesTo(
            code="replaces",
            target=Reference(
                type="DocumentReference",
                identifier=Identifier(value=supersede_pointer_id),
            ),
        )
    )

    print(f"Adding superseded info to {pointer_id}...")
    updated_pointer = DocumentPointer.from_document_reference(doc_ref)
    table.put_item(
        Item=updated_pointer.dict(exclude_none=True, exclude={"_from_dynamo"})
    )

    if delete_superceded:
        print(f"Deleting superseded {supersede_pointer_id}...")
        table.delete_item(
            Key={"pk": f"D#{supersede_pointer_id}", "sk": f"D#{supersede_pointer_id}"}
        )


if __name__ == "__main__":
    fire.Fire(_set_pointer_supersede_info)
