# BEN_EXTRACT_REQUEST

This table holds information for each run of the extract  process for a given carrier.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractrequest-5438.html#benextractrequest-5438](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractrequest-5438.html#benextractrequest-5438)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_EXTRACT_REQUEST_PK | EXT_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_REQUEST_ID | NUMBER |  | 18 | Yes | Identifies the extract request. |
| LAYOUT_ID | NUMBER |  | 18 | Yes | TEMPLATE_ID |
| CARRIER_ID | NUMBER |  | 18 | Yes | CARRIER_ID |
| REQUEST_DATE | DATE |  |  |  | EFFECTIVE_DATE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| STATUS_FLAG | VARCHAR2 | 30 |  |  | STATUS_FLAG |
| EXTRACT_OPTION | VARCHAR2 | 30 |  |  | EXTRACT_OPTION |
| EXTRACT_TYPE | VARCHAR2 | 30 |  |  | EXTRACT_TYPE |
| TOTAL_EMPLOYEES | NUMBER |  | 18 |  | Total number of employees processed under this request. |
| TOTAL_DEPENDENTS | NUMBER |  | 18 |  | Total number of dependents processed under this request. |
| TOTAL_PLANS | NUMBER |  | 9 |  | Total number of plans processed under this request. |
| TOTAL_ROWS | NUMBER |  | 18 |  | Total number of detail records for this request. |
| CARRIER_RESPONSE | VARCHAR2 | 20 |  |  | Identifies the response received from the plan carrier for this request. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| LAST_SUCCESSFUL_TRNSMDT | TIMESTAMP |  |  |  | Timestamp of when this request was last successfully transmitted. |
| COMMENTS | VARCHAR2 | 2000 |  |  | User entered comments |
| TRANSMISSION_LOG | VARCHAR2 | 2000 |  |  | Messages generated while transmitting the file |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_EXTRACT_REQUEST_N1 | Non Unique | Default | CARRIER_ID |
| BEN_EXTRACT_REQUEST_U1 | Unique | Default | EXT_REQUEST_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
