# ANC_MX_INPUT_EXPS_F

Absence Matrix Input Expressions Base Table

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancmxinputexpsf-19511.html#ancmxinputexpsf-19511](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancmxinputexpsf-19511.html#ancmxinputexpsf-19511)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_MX_INPUT_EXPS_F_PK | MX_INPUT_EXP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MX_INPUT_EXP_ID | NUMBER |  | 18 | Yes | Matrix Input Expression |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| NAME | VARCHAR2 | 30 |  |  | Matrix  Input Expressions Name |
| DESCRIPTIONS | VARCHAR2 | 240 |  |  | Matrix  Input  Descriptions |
| EXPRESSION_TEXT | VARCHAR2 | 240 |  |  | Matrix  Input Expression Text |
| MX_TRXN_ID | VARCHAR2 | 240 |  |  | Matrix  Input Expressions Transaction |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_MX_INPUT_EXPS_F_PK | Unique | Default | MX_INPUT_EXP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
