# PER_CHECKLIST_PERIODS

Table to store generated periods for allocation of checklist

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistperiods-24956.html#perchecklistperiods-24956](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistperiods-24956.html#perchecklistperiods-24956)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_PERIODS_PK | CHECKLIST_PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_PERIOD_ID | NUMBER |  | 18 | Yes | CHECKLIST_PERIOD_ID |
| CHECKLIST_SCHEDULE_ID | NUMBER |  | 18 | Yes | CHECKLIST_SCHEDULE_ID |
| PERIOD_NUMBER | NUMBER |  | 18 | Yes | PERIOD_NUMBER |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  | Yes | END_DATE |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | ENABLED_FLAG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| START_TIME_VALUE | NUMBER |  | 5 |  | Time stamp of the start of the period in minutes |
| END_TIME_VALUE | NUMBER |  | 5 |  | Time stamp of the end of the period in minutes |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_PERIODS_PK | Unique | Default | CHECKLIST_PERIOD_ID |
| PER_CHECKLIST_PERIODS_U1 | Unique | Default | CHECKLIST_SCHEDULE_ID, START_DATE, START_TIME_VALUE, END_DATE, END_TIME_VALUE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
