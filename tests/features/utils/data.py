from layer.nrlf.core.constants import (
    CATEGORY_ATTRIBUTES,
    SNOMED_PRACTICE_SETTINGS,
    SNOMED_SYSTEM_URL,
    TYPE_ATTRIBUTES,
)
from nrlf.producer.fhir.r4.model import (
    Attachment,
    CodeableConcept,
    Coding,
    DocumentReference,
    DocumentReferenceContent,
    DocumentReferenceContext,
    DocumentReferenceRelatesTo,
    Identifier,
    Reference,
)
from tests.features.utils.constants import (
    DEFAULT_TEST_AUTHOR,
    DEFAULT_TEST_CATEGORY,
    DEFAULT_TEST_CONTENT,
    DEFAULT_TEST_CONTEXT,
    DEFAULT_TEST_CUSTODIAN,
    DEFAULT_TEST_DESCRIPTION,
    DEFAULT_TEST_MASTER_ID,
    DEFAULT_TEST_SECURITY_LABEL,
    DEFAULT_TEST_SUBJECT,
    DEFAULT_TEST_TYPE,
)


def create_test_document_reference(items: dict) -> DocumentReference:

    practice_setting_code = items.get("practiceSetting", "788007007")
    practice_setting_display = SNOMED_PRACTICE_SETTINGS.get(
        str(practice_setting_code), "General practice service"
    )

    base_doc_ref = DocumentReference.model_construct(
        resourceType="DocumentReference",
        status=items.get("status", "current"),
        content=[
            DocumentReferenceContent(
                attachment=Attachment(
                    contentType=items.get("contentType", "application/json"),
                    url=items["url"],
                ),
                format=Coding(
                    system="https://fhir.nhs.uk/England/CodeSystem/England-NRLFormatCode",
                    code="urn:nhs-ic:unstructured",
                    display="Unstructured document",
                ),
            )
        ],
        context=DocumentReferenceContext(
            practiceSetting=CodeableConcept(
                coding=[
                    Coding(
                        system=SNOMED_SYSTEM_URL,
                        code=str(practice_setting_code),
                        display=practice_setting_display,
                    )
                ]
            )
        ),
    )

    if items.get("id"):
        base_doc_ref.id = items["id"]

    if type_code := items.get("type"):
        type_system = items.get("type_system", SNOMED_SYSTEM_URL)
        type_str = f"{type_system}|{type_code}"
        type_display = items.get(
            "type_display", TYPE_ATTRIBUTES.get(type_str, {}).get("display")
        )

        base_doc_ref.type = CodeableConcept(
            coding=[Coding(system=type_system, code=type_code, display=type_display)]
        )

    if items.get("subject"):
        base_doc_ref.subject = Reference(
            identifier=Identifier(
                system="https://fhir.nhs.uk/Id/nhs-number", value=items["subject"]
            )
        )

    if items.get("custodian"):
        base_doc_ref.custodian = Reference(
            identifier=Identifier(
                system="https://fhir.nhs.uk/Id/ods-organization-code",
                value=items["custodian"],
            )
        )

    if items.get("author"):
        base_doc_ref.author = [
            Reference(
                identifier=Identifier(
                    system="https://fhir.nhs.uk/Id/ods-organization-code",
                    value=items["author"],
                )
            )
        ]

    if items.get("category"):
        category_display = CATEGORY_ATTRIBUTES.get(
            f"{SNOMED_SYSTEM_URL}|{items['category']}", {}
        ).get("display")
        base_doc_ref.category = [
            CodeableConcept(
                coding=[
                    Coding(
                        system=SNOMED_SYSTEM_URL,
                        code=items["category"],
                        display=category_display,
                    )
                ]
            )
        ]

    if items.get("supercedes"):
        base_doc_ref.relatesTo = [
            DocumentReferenceRelatesTo(
                code="replaces",
                target=Reference(
                    type="DocumentReference",
                    identifier=Identifier(
                        system="https://fhir.nhs.uk/Id/ods-organization-code",
                        value=items["supercedes"],
                    ),
                ),
            )
        ]

    return base_doc_ref


def create_test_document_reference_with_defaults(
    section: str, custom_data: str, pointer_id: str = "TSTCUS-sample-id-00000"
) -> str:
    """
    Builds a DocumentReference request body for testing purposes,
    using a valid example DocumentReference body as a default, but
    with one top-level section of the resource overwritten by a json string
    """

    doc_ref_text = f"""{{ "resourceType": "DocumentReference",
      "id": "{pointer_id}",
      "status": "current",
      "docStatus": "final",
      {custom_data if section=="masterIdentifier" else DEFAULT_TEST_MASTER_ID},
      {custom_data if section=="subject" else DEFAULT_TEST_SUBJECT},
      {custom_data if section=="custodian" else DEFAULT_TEST_CUSTODIAN},
      {custom_data if section=="author" else DEFAULT_TEST_AUTHOR},
      {custom_data if section=="type" else DEFAULT_TEST_TYPE},
      {custom_data if section=="category" else DEFAULT_TEST_CATEGORY},
      {custom_data if section=="description" else DEFAULT_TEST_DESCRIPTION},
      {custom_data if section=="security" else DEFAULT_TEST_SECURITY_LABEL},
      {custom_data if section=="content" else DEFAULT_TEST_CONTENT},
      {custom_data if section=="context" else DEFAULT_TEST_CONTEXT}
    }}"""

    return doc_ref_text
