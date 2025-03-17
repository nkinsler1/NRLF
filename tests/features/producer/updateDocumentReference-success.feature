# Update Document Reference
# Update Document Reference urlencoded
# Update Document Reference - multiple changes
Feature: Producer - updateDocumentReference - Success Scenarios

  Scenario: Successfully Update a DocumentReference
    Given the application 'DataShare' (ID 'z00z-y11y-x22x') is registered to access the API
    And the organisation 'X26' is authorised to access pointer types:
      | system                 | value            |
      | http://snomed.info/sct | 1363501000000100 |
      | http://snomed.info/sct | 736253002        |
    And a DocumentReference resource exists with values:
      | property    | value                          |
      | id          | X26-1114567892-updateDocTest   |
      | subject     | 9999999999                     |
      | status      | current                        |
      | type        | 736253002                      |
      | category    | 734163000                      |
      | contentType | application/pdf                |
      | url         | https://example.org/my-doc.pdf |
      | custodian   | X26                            |
      | author      | X26                            |
    When producer 'X26' updates a DocumentReference 'X26-1114567892-updateDocTest' with values:
      | property  | value            |
      | docStatus | entered-in-error |
    Then the response status code is 200
    And the response is an OperationOutcome with 1 issue
    And the OperationOutcome contains the issue:
      """
      {
      "severity": "information",
      "code": "informational",
      "details": {
        "coding": [
          {
            "system": "https://fhir.nhs.uk/ValueSet/NRL-ResponseCode",
            "code": "RESOURCE_UPDATED",
            "display": "Resource updated"
          }
        ]
      },
      "diagnostics": "The DocumentReference has been updated"
      }
      """
