# HR_DOR_MASS_REQUESTS

This table contains information about the mass requests of the document records.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdormassrequests-9057.html#hrdormassrequests-9057](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdormassrequests-9057.html#hrdormassrequests-9057)

## Primary Key

| Name | Columns |
|------|----------|
| hr_dor_mass_requests_PK | MASS_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_REQUEST_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a mass request |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | An unique indentifier for the corresponding ESS request |
| SUBMISSION_TIME | TIMESTAMP |  |  |  | The time at which the request is submitted. |
| START_TIME | TIMESTAMP |  |  |  | The time at which the submitted request is started. |
| COMPLETED_TIME | TIMESTAMP |  |  |  | The time at which the submitted request is completed. |
| STATUS | VARCHAR2 | 30 |  |  | Mass rquest's status like Pending , Completed, Errored etc. |
| COMMENTS | VARCHAR2 | 4000 |  |  | User-entered comments about this mass request. |
| SOURCE_SYSTEM | VARCHAR2 | 150 |  |  | The source system or applications instance which is the source of the collected data. |
| SOURCE_SYSTEM_ID | VARCHAR2 | 150 |  |  | An unique indentifier for the system or applications instance which is the source of the collected data. |
| RETRIED | NUMBER |  | 5 |  | Number of retry attempts for the job. |
| ERROR_MESSAGE | VARCHAR2 | 1500 |  |  | Brief description of the error encountered during job execution. |
| ERROR_DETAILS | CLOB |  |  |  | Detailed information about the error, including stack trace or diagnostic data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_DOR_MASS_REQUESTS_PK | Unique | HR_DOR_MASS_REQUESTS_PK | MASS_REQUEST_ID |
| HR_DOR_MASS_REQUESTS_U1 | Unique | HR_DOR_MASS_REQUESTS_U1 | ESS_REQUEST_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
