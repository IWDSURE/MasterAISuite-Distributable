# PER_CHECKLIST_ALLOC_CRITERIA

Table to store allocation criteria corresponding to a configuration used for mass assigning journeys.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistalloccriteria-14861.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistalloccriteria-14861.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_ALLOC_CRITE_PK | ALLOCATION_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOCATION_CRITERIA_ID | NUMBER |  | 18 | Yes | ALLOCATION_CRITERIA_ID |
| SUBJECT_TYPE | VARCHAR2 | 240 |  |  | SUBJECT_TYPE |
| SUBJECT_KEY | VARCHAR2 | 240 |  |  | SUBJECT_KEY |
| CHECKLIST_ALLOCATION_ID | NUMBER |  | 18 | Yes | CHECKLIST_ALLOCATION_ID |
| EXCLUDE_FLAG | VARCHAR2 | 4 |  | Yes | EXCLUDE_FLAG |
| CRITERIA_TYPE | VARCHAR2 | 30 |  | Yes | CRITERIA_TYPE |
| CHECKLIST_ALLOC_CRITERIA_CODE | VARCHAR2 | 240 |  | Yes | CHECKLIST_ALLOC_CRITERIA_CODE |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | ENABLED_FLAG |
| LIST_ID | NUMBER |  | 18 |  | Foreign Key to HR_VBCS_LISTS
The hcm list for which the criteria is specified |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CRITERIA_CONDITION | VARCHAR2 | 4000 |  |  | CRITERIA_CONDITION |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLIST_ALLOC_CRITE_N1 | Non Unique | Default | CHECKLIST_ALLOCATION_ID |
| PER_CHECKLIST_ALLOC_CRITE_PK | Unique | Default | ALLOCATION_CRITERIA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
