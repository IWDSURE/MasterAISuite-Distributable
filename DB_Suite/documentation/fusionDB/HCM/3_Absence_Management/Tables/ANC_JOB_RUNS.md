# ANC_JOB_RUNS

Table holds information of absences job runs.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancjobruns-10189.html#ancjobruns-10189](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancjobruns-10189.html#ancjobruns-10189)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_JOB_RUNS_PK | JOB_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_RUN_ID | NUMBER |  | 18 | Yes | Job run identifier |
| BATCH_EXE_CD | VARCHAR2 | 30 |  | Yes | Job Batch execution code |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| STATUS | VARCHAR2 | 30 |  | Yes | Job status |
| START_DATETIME | TIMESTAMP |  |  | Yes | Start date time |
| END_DATETIME | TIMESTAMP |  |  |  | End date time |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | Ess request identifier |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ARGUMENT1 | VARCHAR2 | 255 |  |  | ARGUMENT1 Value |
| ARGUMENT2 | VARCHAR2 | 255 |  |  | ARGUMENT2  Value |
| ARGUMENT3 | VARCHAR2 | 255 |  |  | ARGUMENT3  Value |
| ARGUMENT4 | VARCHAR2 | 255 |  |  | ARGUMENT4  Value |
| ARGUMENT5 | VARCHAR2 | 255 |  |  | ARGUMENT5  Value |
| ARGUMENT6 | VARCHAR2 | 255 |  |  | ARGUMENT6  Value |
| ARGUMENT7 | VARCHAR2 | 255 |  |  | ARGUMENT7  Value |
| ARGUMENT8 | VARCHAR2 | 255 |  |  | ARGUMENT8  Value |
| ARGUMENT9 | VARCHAR2 | 255 |  |  | ARGUMENT9  Value |
| ARGUMENT10 | VARCHAR2 | 255 |  |  | ARGUMENT10  Value |
| ARGUMENT11 | VARCHAR2 | 255 |  |  | ARGUMENT11  Value |
| ARGUMENT12 | VARCHAR2 | 255 |  |  | ARGUMENT12  Value |
| ARGUMENT13 | VARCHAR2 | 255 |  |  | ARGUMENT13  Value |
| ARGUMENT14 | VARCHAR2 | 255 |  |  | ARGUMENT14  Value |
| ARGUMENT15 | VARCHAR2 | 255 |  |  | ARGUMENT15  Value |
| ARGUMENT16 | VARCHAR2 | 255 |  |  | ARGUMENT16  Value |
| ARGUMENT17 | VARCHAR2 | 255 |  |  | ARGUMENT17  Value |
| ARGUMENT18 | VARCHAR2 | 255 |  |  | ARGUMENT18  Value |
| ARGUMENT19 | VARCHAR2 | 255 |  |  | ARGUMENT19  Value |
| ARGUMENT20 | VARCHAR2 | 255 |  |  | ARGUMENT20  Value |
| ARGUMENT21 | VARCHAR2 | 255 |  |  | ARGUMENT21  Value |
| ARGUMENT22 | VARCHAR2 | 255 |  |  | ARGUMENT22  Value |
| ARGUMENT23 | VARCHAR2 | 255 |  |  | ARGUMENT23  Value |
| ARGUMENT24 | VARCHAR2 | 255 |  |  | ARGUMENT24  Value |
| ARGUMENT25 | VARCHAR2 | 255 |  |  | ARGUMENT25  Value |
| ARGUMENT26 | VARCHAR2 | 255 |  |  | ARGUMENT26  Value |
| ARGUMENT27 | VARCHAR2 | 255 |  |  | ARGUMENT27  Value |
| ARGUMENT28 | VARCHAR2 | 255 |  |  | ARGUMENT28  Value |
| ARGUMENT29 | VARCHAR2 | 255 |  |  | ARGUMENT29  Value |
| ARGUMENT30 | VARCHAR2 | 255 |  |  | ARGUMENT30  Value |
| EFFECTIVE_DATE | DATE |  |  |  | Effective date |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_JOB_RUNS_U1 | Unique | Default | JOB_RUN_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
