# HTS_WORK_PATTERN_ASSIGNMENTS

Table to store the work pattern assignment information.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternassignments-21872.html#htsworkpatternassignments-21872](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternassignments-21872.html#htsworkpatternassignments-21872)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORK_PAT_ASSIGNMENTS_PK | WORK_PATTERN_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for a work pattern assignment. |
| SOURCE_WORK_PAT_TEMPLATE_ID | NUMBER |  | 18 |  | Identifier of work pattern template which was used to create the work pattern. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person ID to which the work pattern is assigned. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment ID of the person to which the work pattern is assigned. |
| WORK_PATTERN_ID | NUMBER |  | 18 | Yes | Identifier of the work pattern associated to this work pattern assignment. |
| WORK_PATTERN_CATEGORY | VARCHAR2 | 30 |  | Yes | Category of work pattern that is assigned. |
| DATE_FROM | DATE |  |  | Yes | Date from which the assignment of the work pattern is valid. |
| DATE_TO | DATE |  |  |  | Date up to which the assignment of the work pattern is valid. |
| ANCHOR_DATE | DATE |  |  |  | Date belonging to a week which follows Week 1 of the multi-week pattern. |
| ANCHOR_NUM | NUMBER |  | 9 |  | Identifies the period in repeating period unit during which work pattern starts. |
| SOURCE | VARCHAR2 | 30 |  |  | Source through which work pattern was created |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WORK_PAT_ASSIGNMENTS_N1 | Non Unique | Default | PERSON_ID, DATE_FROM, DATE_TO |
| HTS_WORK_PAT_ASSIGNMENTS_N2 | Non Unique | Default | ASSIGNMENT_ID, DATE_FROM, DATE_TO |
| HTS_WORK_PAT_ASSIGNMENTS_N3 | Non Unique | Default | DATE_FROM, DATE_TO |
| HTS_WORK_PAT_ASSIGNMENTS_U1 | Unique | Default | WORK_PATTERN_ASSIGNMENT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
