# PER_GRADES_IN_LADDERS_F

PER_GRADES_IN_LADDERS_F stores the Grades and the order of the grades attached to a Grade Ladder.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesinladdersf-5427.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesinladdersf-5427.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GRADES_IN_LADDERS_F_PK | GRADES_IN_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GRADES_IN_LADDER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| GRADE_LADDER_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_GRADE_LADDERS_F table. | Active |
| GRADE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_GRADES_F table. | Active |
| SEQUENCE | NUMBER |  | 18 | Yes | Indicates the sequence of the grades within the grade ladder. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_GRADES_IN_LADDERS_F_N1 | Non Unique | FUSION_TS_TX_DATA | GRADE_LADDER_ID |
| PER_GRADES_IN_LADDERS_F_N2 | Non Unique | FUSION_TS_TX_DATA | GRADE_ID |
| PER_GRADES_IN_LADDERS_F_PK | Unique | Default | GRADES_IN_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
