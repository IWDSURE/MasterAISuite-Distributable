# HRG_DATA_INTEG_CHECKS

This table stores all the data that has issue.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgdataintegchecks-23949.html#hrgdataintegchecks-23949](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgdataintegchecks-23949.html#hrgdataintegchecks-23949)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_DATA_INTEG_CHECKS_PK | DATA_INTEG_CHECK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_INTEG_CHECK_ID | NUMBER |  | 18 | Yes | Primary key of Data Integrity Checks. |
| PARENT_ID | NUMBER |  | 18 |  | Parent Id of Data Integrity Checks. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| REQ_START_TIME | TIMESTAMP |  |  |  | Enterprise Service Scheduler Job Start Time. |
| REQ_END_TIME | TIMESTAMP |  |  |  | Enterprise Service Scheduler Job End Time. |
| PROCESS_MODE | VARCHAR2 | 30 |  | Yes | Processing Mode of Enterprise Service Scheduler job. |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | Foreign key to hra_tmpl_defns_b. |
| REVIEW_PERIOD_NAME | VARCHAR2 | 240 |  |  | Performance Template Name as defined in hra_tmpl_defns_tl. |
| GOAL_PLAN_ID | NUMBER |  | 18 |  | Foreign key to hra_tmpl_periods_b. |
| GOAL_PLAN_NAME | VARCHAR2 | 240 |  |  | Customary name of Template Periods. |
| WORKER_NAME | VARCHAR2 | 240 |  |  | Display name of worker in per_person_names_f. |
| MANAGER_NAME | VARCHAR2 | 240 |  |  | Display name of manager in per_person_names_f. |
| TABLE_NAME | VARCHAR2 | 30 |  |  | Table Name of the data that has issue. |
| TABLE_PK_COLUMN_NAME | VARCHAR2 | 30 |  |  | Primary Key column name of the issue table. |
| TABLE_PK_COLUMN_VALUE | NUMBER |  | 18 |  | Primary Key column value of the issue table. |
| COLUMN_NAME | VARCHAR2 | 30 |  |  | Column Name of the data that has issue. |
| OLD_VALUE | VARCHAR2 | 240 |  |  | Old/Current Value of data that is wrong. |
| NEW_VALUE | VARCHAR2 | 240 |  |  | New/Correct Value of data that is wrong. |
| ISSUE_CATEGORY | VARCHAR2 | 80 |  |  | Category of the issue identified. |
| COMMENT_TEXT | VARCHAR2 | 4000 |  |  | Comment text of the data quality issue. |
| ERROR_TEXT | VARCHAR2 | 4000 |  |  | Error Text of Enterprise Service Scheduler job failure. |
| DATA_CORRECTED | VARCHAR2 | 1 |  |  | Flag for indentifying the data corrected or not. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_DATA_INTEG_CHECKS_N1 | Non Unique | FUSION_TS_TX_IDX | REVIEW_PERIOD_ID, REQUEST_ID, TABLE_NAME |
| HRG_DATA_INTEG_CHECKS_N2 | Non Unique | FUSION_TS_TX_IDX | LAST_UPDATE_DATE |
| HRG_DATA_INTEG_CHECKS_PK | Unique | FUSION_TS_TX_IDX | DATA_INTEG_CHECK_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
