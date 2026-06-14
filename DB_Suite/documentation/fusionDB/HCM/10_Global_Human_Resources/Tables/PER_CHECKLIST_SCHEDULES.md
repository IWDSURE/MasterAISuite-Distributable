# PER_CHECKLIST_SCHEDULES

Table to store generated schedules for allocation of checklist

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistschedules-14757.html#perchecklistschedules-14757](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistschedules-14757.html#perchecklistschedules-14757)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_SCHEDULES_PK | CHECKLIST_SCHEDULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_SCHEDULE_ID | NUMBER |  | 18 | Yes | CHECKLIST_SCHEDULE_ID |
| SCHEDULE_OWNER | VARCHAR2 | 30 |  | Yes | SCHEDULE_OWNER |
| SCHEDULE_OWNER_ID | NUMBER |  | 18 | Yes | SCHEDULE_OWNER_ID |
| SCHEDULE_TYPE | VARCHAR2 | 30 |  | Yes | SCHEDULE_TYPE |
| SCHEDULE_START_DATE | DATE |  |  |  | SCHEDULE_START_DATE |
| SCHEDULE_END_TYPE | VARCHAR2 | 30 |  |  | SCHEDULE_END_TYPE |
| SCHEDULE_END_DATE | DATE |  |  |  | SCHEDULE_END_DATE |
| SCHEDULE_NUM_OCCURRENCES | NUMBER |  | 5 |  | SCHEDULE_NUM_OCCURRENCES |
| WEEKLY_DAY_OF_WEEK | VARCHAR2 | 30 |  |  | WEEKLY_DAY_OF_WEEK |
| MONTHLY_DAY_OR_WEEK | VARCHAR2 | 30 |  |  | MONTHLY_DAY_OR_WEEK |
| MONTHLY_DAY_OF_MONTH | NUMBER |  | 2 |  | MONTHLY_DAY_OF_MONTH |
| MONTHLY_WEEK_OF_MONTH | VARCHAR2 | 30 |  |  | MONTHLY_WEEK_OF_MONTH |
| MONTHLY_DAY_OF_WEEK | VARCHAR2 | 30 |  |  | MONTHLY_DAY_OF_WEEK |
| YEARLY_MONTH | VARCHAR2 | 30 |  |  | YEARLY_MONTH |
| YEARLY_DAY_OR_WEEK | VARCHAR2 | 30 |  |  | YEARLY_DAY_OR_WEEK |
| YEARLY_DAY_OF_MONTH | NUMBER |  | 2 |  | YEARLY_DAY_OF_MONTH |
| YEARLY_WEEK_OF_MONTH | VARCHAR2 | 30 |  |  | YEARLY_WEEK_OF_MONTH |
| YEARLY_DAY_OF_WEEK | VARCHAR2 | 30 |  |  | YEARLY_DAY_OF_WEEK |
| SCHEDULE_RUNS_PER_PERIOD | VARCHAR2 | 30 |  |  | SCHEDULE_RUNS_PER_PERIOD |
| SCHEDULE_PERIOD_STATUS | VARCHAR2 | 30 |  |  | SCHEDULE_PERIOD_STATUS |
| SCHEDULE_PERIOD_GEN_DATE | DATE |  |  |  | SCHEDULE_PERIOD_GEN_DATE |
| ANALYSIS_PERIOD | NUMBER |  | 5 |  | ANALYSIS_PERIOD |
| ANALYSIS_PERIOD_UOM | VARCHAR2 | 30 |  |  | ANALYSIS_PERIOD_UOM |
| THRESHOLD_SCORE | NUMBER |  | 18 |  | THRESHOLD_SCORE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| EXPIRE_PREVIOUS_PERIOD | VARCHAR2 | 4 |  | Yes | EXPIRE_PREVIOUS_PERIOD |
| RECUR_FREQUENCY | NUMBER |  | 18 | Yes | RECUR_FREQUENCY |
| PERIOD_DURATION | NUMBER |  | 18 |  | PERIOD_DURATION |
| PERIOD_DURATION_UOM | VARCHAR2 | 30 |  |  | PERIOD_DURATION_UOM |
| ALLOW_MULTIPLE_SLOTS | VARCHAR2 | 4 |  | Yes | Identifier to indicate if multiple slots are allowed in the period |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_SCHEDULES_PK | Unique | Default | CHECKLIST_SCHEDULE_ID |
| PER_CHECKLIST_SCHEDULES_U1 | Unique | Default | SCHEDULE_OWNER, SCHEDULE_OWNER_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
