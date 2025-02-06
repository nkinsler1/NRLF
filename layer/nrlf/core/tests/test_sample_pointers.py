import os

import pytest

from nrlf.consumer.fhir.r4.model import DocumentReference as ConsumerDocumentReference
from nrlf.core.validators import DocumentReferenceValidator
from nrlf.producer.fhir.r4.model import DocumentReference as ProducerDocumentReference


@pytest.fixture
def sample_pointer_data() -> str:
    json_files = [f for f in os.listdir("./tests/data/samples") if f.endswith(".json")]

    for file in json_files:
        with open(f"./tests/data/samples/{file}", "r") as f:
            pointer_data = f.read()
            yield pointer_data


def test_sample_pointer_as_consumer(sample_pointer_data: str):
    docref = ConsumerDocumentReference.model_validate_json(sample_pointer_data)

    validator = DocumentReferenceValidator()
    result = validator.validate(data=docref)

    assert result.is_valid


def test_sample_pointer_as_producer(sample_pointer_data: str):
    docref = ProducerDocumentReference.model_validate_json(sample_pointer_data)

    validator = DocumentReferenceValidator()
    result = validator.validate(data=docref)

    assert result.is_valid
