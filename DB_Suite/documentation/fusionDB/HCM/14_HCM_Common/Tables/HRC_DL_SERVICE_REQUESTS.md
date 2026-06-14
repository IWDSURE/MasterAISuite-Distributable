# HRC_DL_SERVICE_REQUESTS

This table stores the details of the service call

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlservicerequests-27152.html#hrcdlservicerequests-27152](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlservicerequests-27152.html#hrcdlservicerequests-27152)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_SERVICE_REQUESTS_PK | SERVICE_CALL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SERVICE_CALL_ID | NUMBER |  | 18 | Yes | Primary key column |
| SERVICE_TYPE | VARCHAR2 | 20 |  |  | Service Type Attribute. NULL for SOAP Service, REST for REST Service. |
| CONTENT_ID | VARCHAR2 | 50 |  |  | ContentId attribute value |
| PARAMETERS | VARCHAR2 | 4000 |  |  | Parameters attribute value |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | The request id of the submitted ESS job if the ESS job could be submitted successfully |
| STATUS | VARCHAR2 | 20 |  | Yes | SUCCESS: ESS submitted successfully
ERROR: Error raised and returned in web service payload, no ESS job submitted |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_SERVICE_REQUESTS_U1 | Unique | Default | SERVICE_CALL_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
