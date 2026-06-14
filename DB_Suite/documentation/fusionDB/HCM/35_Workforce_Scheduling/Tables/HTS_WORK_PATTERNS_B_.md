# HTS_WORK_PATTERNS_B_

Table to store the work pattern information. Work patterns will be used to assign to workers.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternsb-17797.html#htsworkpatternsb-17797](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternsb-17797.html#htsworkpatternsb-17797)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORK_PATTERNS_B_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORK_PATTERN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for a work pattern. |
| WORK_PATTERN_ALTCD | VARCHAR2 | 30 |  |  | Work pattern alternate code. Unique and non-translatable. |
| WORK_SHIFT_TYPE | VARCHAR2 | 30 |  |  | Identifies the type of shift associated to this work pattern. |
| WORK_PATTERN_TYPE_ID | NUMBER |  | 18 |  | Identifier of the work pattern type associated to this work pattern. |
| TEMPLATE_FLAG | VARCHAR2 | 30 |  |  | Identifies whether work pattern is considered as a template. |
| REPEAT_CYCLE | VARCHAR2 | 32 |  |  | Repeating cycle. |
| REPEAT_NUM | NUMBER |  | 9 |  | Length of work pattern in repeating period unit. |
| START_DAY_OF_PATTERN | VARCHAR2 | 30 |  |  | Identifies the day on which work pattern starts. |
| NON_WORKING_CYCLES | VARCHAR2 | 240 |  |  | Identifies the non-working cycles in the work pattern stored as a single value with comma as a separator. |
| WORK_DAY_DEF_ID | NUMBER |  | 18 |  | Identifier of the workday definition associated to this work pattern. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WORK_PATTERNS_B_U1_ | Unique | HTS_WORK_PATTERNS_B_U1_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORK_PATTERN_ID |
| HTS_WORK_PATTERNS_B_U2_ | Unique | HTS_WORK_PATTERNS_B_U2_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORK_PATTERN_ALTCD |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
