Producer guidance:

The test cases in this section are MANDATORY and demonstrate core functionality of the system.

While some implementations may not use some interactions, we do require producers to be able to create, update/supersede and delete pointers.

|  |  |  |  |
| --- | --- | --- | --- |
| **Step** | **Detailed instructions** | **Evidence required** | **Expected outcome** |
| 1 | Authenticate as a valid organisation with a valid access token |  |  |
| 2 | Construct a new DocumentReference for the request body.   * Use test patient with NHS number **9876543210** * Type should reflect whichever type you plan on using in live, as agreed in IAG. * All mandatory fields must be populated, and any other fields you plan to use in your live implementation should be populated as you intend to use them. * Do not include a **relatesTo** section. | Please include a **copy of the request body** as it was sent in. | Request body is a valid FHIR R4 DocumentReference that adheres to the additional constraints detailed in the API specification, as well as any other constraints mentioned in the compliance checklist. |
| 3 | Send as a POST request to the /DocumentReference endpoint, along with headers specified in the API spec.  Audit logs should contain details of the request. | Save an extract or screenshot of the **audit logs for this** **request** in the appropriate folder. | Audit logs show:   * HTTP request body * HTTP request URL * HTTP verb * ODS code of sender * NHS number of patient * Request date-time * Request ID * Correlation ID? |
| 4 | Record the unique .id generated for your newly created pointer. Audit logs should contain details of the response to the request in step 3.  Id: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | Save an extract or screenshot of the **audit logs for this** **response** in the appropriate folder. | Audit logs show:   * HTTP response body (an OperationOutcome indicating RESOURCE\_CREATED) * HTTP response code (201) * Response datetime * The pointer ID (found in the location header) * Correlation ID? |

### **TC-P02 - Read happy path / success scenario**

|  |  |  |  |
| --- | --- | --- | --- |
| **Step** | **Detailed instructions** | **Evidence required** | **Expected outcome** |
| 1 | Authenticate as a valid organisation with a valid access token |  |  |
| 3 | Send a GET request for the pointer created in TC-01 using the ID generated and recorded. | Save an extract or screenshot of the **audit logs for this** **request** in the appropriate folder. | Audit logs show:   * HTTP request body * HTTP request URL * HTTP verb * ODS code of sender * NHS number of patient * Request date-time * Request ID * Correlation ID? |
| 4 | View the pointer received in the response. | Save an extract or screenshot of the **audit logs for this** **response** in the appropriate folder. | Audit logs show:   * HTTP response body (an DocumentReference) * HTTP response code (200) * Response datetime * The pointer ID (found in the location header) * Correlation ID? |

### **TC-P03 - Supersede happy path / success scenario**

|  |  |  |  |
| --- | --- | --- | --- |
| **Step** | **Instructions/ Guidance** | **Evidence required** | **Expected outcome** |
| 1 | Authenticate as a valid organisation with a valid access token |  |  |
| 2 | Construct a DocumentReference for the request body that will supersede the pointer created in TC01.   * Use the same request body as in TC01. NHS number, type and category must match. * Populate the **relatesTo** section with the pointer ID generated in TC01 (found in the location header of the response). | Please include a **copy of the request body** as it was sent in. | Request body is a valid FHIR R4 DocumentReference that adheres to the additional constraints detailed in the API specification, as well as any other constraints mentioned in the compliance checklist. |
| 3 | Send as a POST request to the /DocumentReference endpoint, along with headers specified in the API spec.  Audit logs should contain details of the request. | Save an extract or screenshot of the **audit logs for this** **request** in the appropriate folder. | Audit logs show:   * HTTP request body * HTTP request URL * HTTP verb * ODS code of sender * NHS number of patient * Request date-time * Request ID * Correlation ID? |
| 4 | Record the unique .id generated for your newly created pointer. Audit logs should contain details of the response to the request in step 3.  Id: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | Save an extract or screenshot of the **audit logs for this** **response** in the appropriate folder. | Audit logs show:   * HTTP response body (an OperationOutcome indicating RESOURCE\_CREATED) * HTTP response code (201) * Response datetime * The pointer ID (found in the location header) * Correlation ID? |

### **TC-P04 - Search happy path / success scenario (multiple results)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Step** | **Detailed instructions** | **Evidence required** | **Expected outcome** |
| 1 | Authenticate as a valid organisation with a valid access token |  |  |
| 2a  OR  2b | Send a GET search request for all pointers using the NHS number.  Send a POST search request for all pointers using the NHS number. | Save an extract or screenshot of the **audit logs for this** **request** in the appropriate folder. | Audit logs show:   * HTTP request body * HTTP request URL * HTTP verb * ODS code of sender * NHS number of patient * Request date-time * Request ID * Correlation ID? |
| 3 | View the searchset bundle received in the response.  There should be at least TWO DocumentReferences; the one you created (and superseded) in the previous tests, and another one created by NRLF filled with example data. | Save an extract or screenshot of the **audit logs for this** **response** in the appropriate folder. | Audit logs show:   * HTTP response body (an DocumentReference) * HTTP response code (200) * Response datetime * The pointer ID (found in the location header) * Correlation ID? |

### **Unhappy paths**

Choose one of the following negative scenarios for each interaction, and provide the evidence suggested. We recognise that if your application is designed to prevent misuse, these could be difficult to recreate using the UI; it may be necessary to make a small temporary change to configuration or send the request in another way. If you cannot complete one of these please reach out to the NRLF team via your organisation’s dedicated Slack channel.

The purpose of these tests is to show that your audit logging system properly records even failed attempts and error responses, in accordance with SAR requirements.

**“Create” / “Update” / “Supersede” example error scenarios:**

* Message body is not FHIR-compliant (expected response: 400)
* Message body does not meet the NRL business logic profile (expected response: 400 or 422), e.g.
  + A mandatory field such as ‘context.practiceSetting’, ‘author’, or ‘category’ is missing.
  + A mandatory field has an invalid value, e.g. a
  + The category does not match the type (e.g. a Mental Health Crisis Plan is submitted in the ‘Observations’ category instead of ‘Care plan’) or uses the wrong system (i.e. not SNOMED)
  + The display value on a mandatory codeable concept does not match the expected text in the ValueSet (e.g. SNOMED code 736253002, but display is ‘Radiology report’ instead of ‘Mental health crisis plan’
* Missing a mandatory header
* Marking the ‘type’ of a pointer as one for which your organisation has not been granted permissions.

**“Read” example error scenarios:**

* Missing or incorrect mandatory header
* The pointer is a type for which your organisation does not have access
* The pointer was created by a different organisation

**“Delete” example error scenarios:**

* Missing or incorrect mandatory headers
* The pointer is created by a different organisation

Please indicate which case you have chosen and provide the following:

* Request body
* Audit logs
* Response body
