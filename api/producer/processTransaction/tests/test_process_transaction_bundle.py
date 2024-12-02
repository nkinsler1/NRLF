import json

from freeze_uuid import freeze_uuid
from freezegun import freeze_time
from moto import mock_aws

from api.producer.processTransaction.process_transaction_bundle import handler
from nrlf.core.dynamodb.repository import DocumentPointerRepository
from nrlf.producer.fhir.r4.model import (
    Bundle,
    BundleEntry,
    BundleEntryRequest,
    DocumentReference,
)
from nrlf.tests.data import load_document_reference
from nrlf.tests.dynamodb import mock_repository
from nrlf.tests.events import (
    create_headers,
    create_mock_context,
    create_test_api_gateway_event,
    default_response_headers,
)


@mock_aws
@mock_repository
@freeze_time("2024-03-21T12:34:56.789")
@freeze_uuid("00000000-0000-0000-0000-000000000001")
def test_create_single_document_reference_with_transaction_happy_path(
    repository: DocumentPointerRepository,
):
    doc_ref: DocumentReference = load_document_reference("Y05868-736253002-Valid")

    request_bundle = Bundle(
        entry=[
            BundleEntry(
                resource=doc_ref, request=BundleEntryRequest(url="/", method="POST")
            )
        ],
        resourceType="Bundle",
        type="transaction",
    )

    event = create_test_api_gateway_event(
        headers=create_headers(),
        body=request_bundle.model_dump_json(),
    )

    result = handler(event, create_mock_context())
    body = result.pop("body")

    assert result == {
        "statusCode": "200",
        "headers": {
            **default_response_headers(),
        },
        "isBase64Encoded": False,
    }

    parsed_body = json.loads(body)
    assert parsed_body == {
        "resourceType": "Bundle",
        "type": "transaction-response",
        "entry": [
            {
                "response": {
                    "status": "201",
                    "location": "/producer/FHIR/R4/DocumentReference/Y05868-00000000-0000-0000-0000-000000000001",
                },
            },
        ],
    }

    created_doc_pointer = repository.get_by_id(
        "Y05868-00000000-0000-0000-0000-000000000001"
    )

    assert created_doc_pointer is not None
    assert created_doc_pointer.created_on == "2024-03-21T12:34:56.789Z"
    assert created_doc_pointer.updated_on is None
    assert json.loads(created_doc_pointer.document) == {
        **(doc_ref.model_dump(exclude_none=True)),
        "meta": {
            "lastUpdated": "2024-03-21T12:34:56.789Z",
        },
        "date": "2024-03-21T12:34:56.789Z",
        "id": "Y05868-00000000-0000-0000-0000-000000000001",
    }
