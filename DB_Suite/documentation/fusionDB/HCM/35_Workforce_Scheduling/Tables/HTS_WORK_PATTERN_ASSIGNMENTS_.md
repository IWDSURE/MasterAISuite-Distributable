# HTS_WORK_PATTERN_ASSIGNMENTS_

Table to store the work pattern assignment information.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternassignments-5258.html#htsworkpatternassignments-5258](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternassignments-5258.html#htsworkpatternassignments-5258)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORK_PAT_ASSIGNMENTS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORK_PATTERN_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for a work pattern assignment. |
| SOURCE_WORK_PAT_TEMPLATE_ID | NUMBER |  | 18 |  | Identifier of work pattern template which was used to create the work pattern. |
| PERSON_ID | NUMBER |  | 18 |  | Person ID to which the work pattern is assigned. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment ID of the person to which the work pattern is assigned. |
| WORK_PATTERN_ID | NUMBER |  | 18 |  | Identifier of the work pattern associated to this work pattern assignment. |
| WORK_PATTERN_CATEGORY | VARCHAR2 | 30 |  |  | Category of work pattern that is assigned. |
| DATE_FROM | DATE |  |  |  | Date from which the assignment of the work pattern is valid. |
| DATE_TO | DATE |  |  |  | Date up to which the assignment of the work pattern is valid. |
| ANCHOR_DATE | DATE |  |  |  | Date belonging to a week which follows Week 1 of the multi-week pattern. |
| ANCHOR_NUM | NUMBER |  | 9 |  | Identifies the period in repeating period unit during which work pattern starts. |
| SOURCE | VARCHAR2 | 30 |  |  | Source through which work pattern was created |
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
| HTS_WORK_PAT_ASSIGNMENTS_N1_ | Non Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_ID, DATE_FROM, DATE_TO |
| HTS_WORK_PAT_ASSIGNMENTS_N2_ | Non Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASSIGNMENT_ID, DATE_FROM, DATE_TO |
| HTS_WORK_PAT_ASSIGNMENTS_N3_ | Non Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DATE_FROM, DATE_TO |
| HTS_WORK_PAT_ASSIGNMENTS_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORK_PATTERN_ASSIGNMENT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
