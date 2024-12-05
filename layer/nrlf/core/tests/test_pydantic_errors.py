from unittest.mock import Mock

import pytest

from nrlf.core.errors import ParseError
from nrlf.core.validators import DocumentReferenceValidator
from nrlf.tests.data import load_document_reference_json


def test_validate_content_missing_attachment():
    validator = DocumentReferenceValidator()
    document_ref_data = load_document_reference_json("Y05868-736253002-Valid")

    document_ref_data["content"][0].pop("attachment")

    with pytest.raises(ParseError) as error:
        validator.validate(document_ref_data)

    exc = error.value
    assert len(exc.issues) == 1
    assert exc.issues[0].model_dump(exclude_none=True) == {
        "severity": "error",
        "code": "invalid",
        "details": {
            "coding": [
                {
                    "system": "https://fhir.nhs.uk/ValueSet/Spine-ErrorOrWarningCode-1",
                    "code": "INVALID_RESOURCE",
                    "display": "Invalid validation of resource",
                }
            ]
        },
        "diagnostics": "Failed to parse DocumentReference resource (content.0.attachment: Field required)",
        "expression": ["content.0.attachment"],
    }


def test_validate_content_missing_content_type():
    validator = DocumentReferenceValidator()
    document_ref_data = load_document_reference_json("Y05868-736253002-Valid")

    document_ref_data["content"][0]["attachment"].pop("contentType")

    with pytest.raises(ParseError) as error:
        validator.validate(document_ref_data)

    exc = error.value
    assert len(exc.issues) == 1
    assert exc.issues[0].model_dump(exclude_none=True) == {
        "severity": "error",
        "code": "invalid",
        "details": {
            "coding": [
                {
                    "system": "https://fhir.nhs.uk/ValueSet/Spine-ErrorOrWarningCode-1",
                    "code": "INVALID_RESOURCE",
                    "display": "Invalid validation of resource",
                }
            ]
        },
        "diagnostics": "Failed to parse DocumentReference resource (content.0.attachment.contentType: Field required)",
        "expression": ["content.0.attachment.contentType"],
    }


def test_validate_content_invalid_content_type():
    validator = DocumentReferenceValidator()
    document_ref_data = load_document_reference_json("Y05868-736253002-Valid")

    document_ref_data["content"][0]["attachment"]["contentType"] = "invalid/type"

    with pytest.raises(ParseError) as error:
        validator.validate(document_ref_data)

    exc = error.value
    assert len(exc.issues) == 1
    assert exc.issues[0].model_dump(exclude_none=True) == {
        "severity": "error",
        "code": "invalid",
        "details": {
            "coding": [
                {
                    "system": "https://fhir.nhs.uk/ValueSet/Spine-ErrorOrWarningCode-1",
                    "code": "INVALID_RESOURCE",
                    "display": "Invalid validation of resource",
                }
            ]
        },
        "diagnostics": "Failed to parse DocumentReference resource (content.0.attachment.contentType: String should match pattern '^(application|audio|image|message|model|multipart|text|video)/[a-zA-Z0-9!#$&^_+.-]+(;[a-zA-Z0-9!#$&^_+.-]+=[a-zA-Z0-9!#$&^_+.-]+)*$')",
        "expression": ["content.0.attachment.contentType"],
    }
