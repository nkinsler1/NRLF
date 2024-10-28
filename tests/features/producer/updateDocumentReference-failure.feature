# No pointer ID in headers
# Pointer in URL and body mismatch
# Invalid document reference - same as createDocumentReference
# Invalid document reference - changing immutable fields
# Provider ID mismatch
# No existing document reference
Feature: Producer - updateDocumentReference - Failure Scenarios

  Scenario: Invalid status
    Given the application 'DataShare' (ID 'z00z-y11y-x22x') is registered to access the API
    And the organisation 'X26' is authorised to access pointer types:
      | system                 | value            |
      | http://snomed.info/sct | 1363501000000100 |
      | http://snomed.info/sct | 736253002        |
    And a DocumentReference resource exists with values:
      | property    | value                          |
      | id          | X26-1114567890-updateDocTest   |
      | subject     | 9999999999                     |
      | status      | current                        |
      | type        | 736253002                      |
      | category    | 734163000                      |
      | contentType | application/pdf                |
      | url         | https://example.org/my-doc.pdf |
      | custodian   | X26                            |
      | author      | X26                            |
    When producer 'X26' updates a DocumentReference 'X26-1114567890-updateDocTest' with values:
      | property | value   |
      | status   | invalid |
    Then the response status code is 400
    And the response is an OperationOutcome with 1 issue
    And the OperationOutcome contains the issue:
      """
      {
        "severity": "error",
        "code": "invalid",
        "details": {
        "coding": [
        {
        "system": "https://fhir.nhs.uk/ValueSet/Spine-ErrorOrWarningCode-1",
        "code": "MESSAGE_NOT_WELL_FORMED",
        "display": "Message not well formed"
        }
        ]
        },
        "diagnostics": "Request body could not be parsed (status: String should match pattern '^current$')",
        "expression": [
        "status"
        ]
      }
      """
