# HHR_VLTR_JOB

This table stores volunteering job info

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrjob-7329.html#hhrvltrjob-7329](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrjob-7329.html#hhrvltrjob-7329)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_JOB_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | Indicates the identifier of the business unit associated to the row. |
| JOB_NAME | VARCHAR2 | 4000 |  |  | JOB_NAME |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | ERROR_MESSAGE |
| STATUS | VARCHAR2 | 50 |  |  | STATUS |
| JOB_TYPE | VARCHAR2 | 50 |  |  | JOB_TYPE |
| LAST_RUN_DATE | TIMESTAMP |  |  |  | last run date |
| SCHEDULE_INTERVAL | NUMBER |  | 18 |  | SCHEDULE_INTERVAL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| RESULT | VARCHAR2 | 4000 |  |  | result of the job |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_VLTR_JOB_U1 | Unique | FUSION_TS_TX_IDX | JOB_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
