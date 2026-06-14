# HWR_METIS_CALENDAR_JOB_RUN_B

The message table stores information about the calendar job executed.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmetiscalendarjobrunb-11247.html#hwrmetiscalendarjobrunb-11247](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmetiscalendarjobrunb-11247.html#hwrmetiscalendarjobrunb-11247)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_METIS_CALENDAR_JOB_RU_PK | CAL_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAL_JOB_ID | NUMBER |  | 18 | Yes | CALENDAThis is the primary key for this table. The number should be generated from the sequence HWR METIS_CALENDAR_JOB_RUN_S |
| LAST_JOB_RUN_TIME | TIMESTAMP |  |  | Yes | LAST_JOB_RUN_TIME |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_METIS_CAL_JOB_RUN_B_U1 | Unique | FUSION_TS_TX_DATA | CAL_JOB_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
