Producer guidance:

The test cases in this section are **MANDATORY** and demonstrate core functionality of the system.

While some implementations may not use some interactions, we do require producers to be able to create,
update/supersede and delete pointers.

---

### **TC-P01 - Create happy path / success scenario**

| **Step** | **Detailed instructions** | **Evidence required** |**Expected outcome** |
|----------|---------------------------|-----------------------|---------------------|
| 1        | Authenticate as a valid organisation with a valid access token. | | |
| 2        | Construct a new DocumentReference for the request body.<br> <ul> <li>Use test patient with NHS number 9876543210</li> <li>Type should reflect whichever type you plan on using in live, as agreed in IAG.</li> <li>All mandatory fields must be populated, and any other fields you plan to use in your live implementation should be populated as you intend to use them.</li> <li>Do not include a relatesTo section.</li> </ul> | Please include a copy of the request body as it was sent in. | Request body is a valid FHIR R4 DocumentReference that adheres to the additional constraints detailed in the API specification, as well as any other constraints mentioned in the compliance checklist. |
| 3        | Send as a POST request to the /DocumentReference endpoint, along with headers specified in the API spec.<br> Audit logs should contain details of the request. | Save an extract or screenshot of the audit logs for this request in the appropriate folder. | Audit logs show:<br> <ul> <li>HTTP request body</li> <li>HTTP request URL</li> <li>HTTP verb</li> <li>ODS code of sender</li> <li>NHS number of patient</li> <li>Request date-time</li> <li>Request ID</li> <li>Correlation ID?</li> </ul> |
| 4        | Record the unique .id generated for your newly created pointer.<br> Audit logs should contain details of the response to the request in step 3.<br> Id: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | Save an extract or screenshot of the audit logs for this response in the appropriate folder. | Audit logs show:<br> <ul> <li>HTTP response body (an OperationOutcome indicating RESOURCE_CREATED)</li> <li>HTTP response code (201)</li> <li>Response datetime</li> <li>The pointer ID (found in the location header)</li> <li>Correlation ID?</li> </ul> |

---

### **TC-P02 - Read happy path / success scenario**

| **Step** | **Detailed instructions** | **Evidence required** |**Expected outcome** |
|----------|---------------------------|-----------------------|---------------------|
| 1        | Authenticate as a valid organisation with a valid access token. | | |
| 2        | Send a GET request for the pointer created in TC-01 using the ID generated and recorded. | Save an extract or screenshot of the audit logs for this request in the appropriate folder.  | Audit logs show:<br> <ul> <li>HTTP request body</li> <li>HTTP request URL</li> <li>HTTP verb</li> <li>ODS code of sender</li> <li>NHS number of patient</li> <li>Request date-time</li> <li>Request ID</li> <li>Correlation ID?</li> </ul> |
| 3        | View the pointer received in the response.                                               | Save an extract or screenshot of the audit logs for this response in the appropriate folder. | Audit logs show:<br> <ul> <li>HTTP response body (a DocumentReference)</li> <li>HTTP response code (200)</li> <li>Response datetime</li> <li>The pointer ID (found in the location header)</li> <li>Correlation ID?</li> </ul>             |

---

### **TC-P03 - Supersede happy path / success scenario**

| **Step** | **Instructions/ Guidance** | **Evidence required** | **Expected outcome** |
|----------|----------------------------|-----------------------|----------------------|
| 1        | Authenticate as a valid organisation with a valid access token. | | |
| 2        | Construct a DocumentReference for the request body that will supersede the pointer created in TC01.<br> <ul> <li>Use the same request body as in TC01. NHS number, type and category must match.</li> <li>Populate the relatesTo section with the pointer ID generated in TC01 (found in the location header of the response).</li> </ul> | Please include a copy of the request body as it was sent in.                                 | Request body is a valid FHIR R4 DocumentReference that adheres to the additional constraints detailed in the API specification, as well as any other constraints mentioned in the compliance checklist. |
| 3        | Send as a POST request to the /DocumentReference endpoint, along with headers specified in the API spec.<br> Audit logs should contain details of the request.  | Save an extract or screenshot of the audit logs for this request in the appropriate folder.  | Audit logs show:<br> <ul> <li>HTTP request body</li> <li>HTTP request URL</li> <li>HTTP verb</li> <li>ODS code of sender</li> <li>NHS number of patient</li> <li>Request date-time</li> <li>Request ID</li> <li>Correlation ID?</li> </ul> |
| 4        | Record the unique .id generated for your newly created pointer.<br> Audit logs should contain details of the response to the request in step 3.<br> Id: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | Save an extract or screenshot of the audit logs for this response in the appropriate folder. | Audit logs show:<br> <ul> <li>HTTP response body (an OperationOutcome indicating RESOURCE_CREATED)</li> <li>HTTP response code (201)</li> <li>Response datetime</li> <li>The pointer ID (found in the location header)</li> <li>Correlation ID?</li> </ul> |

---

### **TC-P04 - Search happy path / success scenario (multiple results)**

| **Step** | **Detailed instructions** | **Evidence required** |**Expected outcome** |
|----------|---------------------------|-----------------------|---------------------|
| 1        | Authenticate as a valid organisation with a valid access token.   | | |
| 2a OR 2b | <ul> <li>Send a GET search request for all pointers using the NHS number.</li> <li>Send a POST search request for all pointers using the NHS number.</li> </ul> | Save an extract or screenshot of the audit logs for this request in the appropriate folder.  | Audit logs show:<br> <ul> <li>HTTP request body</li> <li>HTTP request URL</li> <li>HTTP verb</li> <li>ODS code of sender</li> <li>NHS number of patient</li> <li>Request date-time</li> <li>Request ID</li> <li>Correlation ID?</li> </ul> |
| 3        | View the searchset bundle received in the response.<br> There should be at least TWO DocumentReferences; the one you created (and superseded) in the previous tests, and another one created by NRLF filled with example data. | Save an extract or screenshot of the audit logs for this response in the appropriate folder. | Audit logs show:<br> <ul> <li>HTTP response body (a DocumentReference)</li> <li>HTTP response code (200)</li> <li>Response datetime</li> <li>The pointer ID (found in the location header)</li> <li>Correlation ID?</li> </ul> |

---

### **Unhappy paths**

Choose one of the following negative scenarios for each interaction, and provide the evidence suggested.
We recognise that if your application is designed to prevent misuse, these could be difficult to recreate
using the UI; it may be necessary to make a small temporary change to configuration or send the request
in another way. If you cannot complete one of these please reach out to the NRLF team via your
organisation’s dedicated Slack channel.

The purpose of these tests is to show that your audit logging system properly records even failed
attempts and error responses, in accordance with SAR requirements.

**“Create” / “Update” / “Supersede” example error scenarios:**

- Message body is not FHIR-compliant (expected response: 400)
- Message body does not meet the NRL business logic profile (expected response: 400 or 422), e.g.
  - A mandatory field such as ‘context.practiceSetting’, ‘author’, or ‘category’ is missing.
  - A mandatory field has an invalid value, e.g. a
  - The category does not match the type (e.g. a Mental Health Crisis Plan is submitted in the
    ‘Observations’ category instead of ‘Care plan’) or uses the wrong system (i.e. not SNOMED)
  - The display value on a mandatory codeable concept does not match the expected text in the ValueSet
    (e.g. SNOMED code 736253002, but display is ‘Radiology report’ instead of ‘Mental health crisis plan’)
- Missing a mandatory header
- Marking the ‘type’ of a pointer as one for which your organisation has not been granted permissions.

**“Read” example error scenarios:**

- Missing or incorrect mandatory header
- The pointer is a type for which your organisation does not have access
- The pointer was created by a different organisation

**“Delete” example error scenarios:**

- Missing or incorrect mandatory headers
- The pointer is created by a different organisation

Please indicate which case you have chosen and provide the following:

- Request body
- Audit logs
- Response body
