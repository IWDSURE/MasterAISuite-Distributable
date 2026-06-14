# PER_GRADES_IN_LADDERS_F_

PER_GRADES_IN_LADDERS_F stores the Grades and the order of the grades attached to a Grade Ladder.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesinladdersf-14930.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesinladdersf-14930.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GRADES_IN_LADDERS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, GRADES_IN_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GRADES_IN_LADDER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | Foreign Key to PER_GRADE_LADDERS_F table. | Active |
| GRADE_ID | NUMBER |  | 18 |  | Foreign Key to PER_GRADES_F table. | Active |
| SEQUENCE | NUMBER |  | 18 |  | Indicates the sequence of the grades within the grade ladder. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_GRADES_IN_LADDERS_FN1_ | Non Unique | Default | GRADES_IN_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_GRADES_IN_LADDERS_FN2_ | Non Unique | Default | AUDIT_ACTION_TYPE_ |
| PER_GRADES_IN_LADDERS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, GRADES_IN_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
