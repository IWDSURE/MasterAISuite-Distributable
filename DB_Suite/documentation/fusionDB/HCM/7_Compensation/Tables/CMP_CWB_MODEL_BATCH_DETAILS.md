# CMP_CWB_MODEL_BATCH_DETAILS

CMP_CWB_MODEL_BATCH_DETAILS identifies the request details of model batch.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelbatchdetails-28496.html#cmpcwbmodelbatchdetails-28496](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelbatchdetails-28496.html#cmpcwbmodelbatchdetails-28496)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_MODEL_BATCH_DETAI_PK | MODEL_ID, USER_PERSON_ID, ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| MODEL_ID | NUMBER |  | Yes | MODEL_ID |
| USER_PERSON_ID | NUMBER |  | Yes | USER_PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | Yes | ASSIGNMENT_ID |
| APPLY_REQUEST_ID | NUMBER |  |  | APPLY_REQUEST_ID |
| DYNC_CAL_REQUEST_ID | NUMBER |  |  | DYNC_CAL_REQUEST_ID |
| PLAN_ID | NUMBER |  |  | PLAN_ID |
| PERIOD_ID | NUMBER |  |  | PERIOD_ID |
| REQUEST_SUBMITTED_DATE | TIMESTAMP |  |  | REQUEST_SUBMITTED_DATE |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_MODEL_U2 | Unique | Default | MODEL_ID, USER_PERSON_ID, ASSIGNMENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
