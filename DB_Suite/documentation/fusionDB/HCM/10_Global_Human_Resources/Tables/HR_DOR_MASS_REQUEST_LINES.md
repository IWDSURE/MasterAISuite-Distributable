# HR_DOR_MASS_REQUEST_LINES

This table contains information about the mass request's lines.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdormassrequestlines-26964.html#hrdormassrequestlines-26964](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdormassrequestlines-26964.html#hrdormassrequestlines-26964)

## Primary Key

| Name | Columns |
|------|----------|
| hr_dor_mass_request_lines_PK | MASS_REQUEST_ID, DOCUMENTS_OF_RECORD_ID, ATTACHED_DOCUMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_REQUEST_ID | NUMBER |  | 18 | Yes | Uniquely identifies a mass request |
| DOCUMENTS_OF_RECORD_ID | NUMBER |  | 18 | Yes | Uniquely identifies a document record. |
| ATTACHED_DOCUMENT_ID | NUMBER |  | 18 | Yes | Uniquely identifies a attachment. |
| STATUS | VARCHAR2 | 30 |  |  | Status of the line like Errored , Skipped , Completed etc. |
| RETRIED | NUMBER |  | 5 |  | Number of retry attempts for the line. |
| ERROR_CODE | VARCHAR2 | 100 |  |  | Error code of the line in the case of Error status. |
| ERROR_MESSAGE | VARCHAR2 | 1500 |  |  | Error message of the line in the case of Error status. |
| ERROR_DETAILS | CLOB |  |  |  | Error stack of the line in the case of Error status. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_DOR_MASS_REQUEST_LINES_PK | Unique | HR_DOR_MASS_REQUEST_LINES_PK | MASS_REQUEST_ID, DOCUMENTS_OF_RECORD_ID, ATTACHED_DOCUMENT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
