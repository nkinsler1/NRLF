import os

import pytest

from nrlf.consumer.fhir.r4.model import DocumentReference as ConsumerDocumentReference
from nrlf.core.validators import DocumentReferenceValidator
from nrlf.producer.fhir.r4.model import DocumentReference as ProducerDocumentReference


def sample_pointer_files() -> list[str]:
    return [f for f in os.listdir("./tests/data/samples") if f.endswith(".json")]


def load_sample_pointer_data(pointer_file: str) -> str:
    with open(f"./tests/data/samples/{pointer_file}", "r") as f:
        return f.read()


@pytest.mark.parametrize("sample_pointer_file", sample_pointer_files())
def test_sample_pointer_as_consumer(sample_pointer_file: str):
    sample_pointer_data = load_sample_pointer_data(sample_pointer_file)

    docref = ConsumerDocumentReference.model_validate_json(sample_pointer_data)
    result = DocumentReferenceValidator().validate(data=docref)

    assert result.is_valid


@pytest.mark.parametrize("sample_pointer_file", sample_pointer_files())
def test_sample_pointer_as_producer(sample_pointer_file: str):
    sample_pointer_data = load_sample_pointer_data(sample_pointer_file)

    docref = ProducerDocumentReference.model_validate_json(sample_pointer_data)
    result = DocumentReferenceValidator().validate(data=docref)

    assert result.is_valid
