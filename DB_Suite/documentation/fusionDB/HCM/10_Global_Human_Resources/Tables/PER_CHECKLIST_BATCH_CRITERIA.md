# PER_CHECKLIST_BATCH_CRITERIA

This table stores criteria of a batch action.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistbatchcriteria-25268.html#perchecklistbatchcriteria-25268](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistbatchcriteria-25268.html#perchecklistbatchcriteria-25268)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_BATCH_CRITERIA_PK | BATCH_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_CRITERIA_ID | NUMBER |  | 18 | Yes | BATCH_CRITERIA_ID |
| SUBJECT_TYPE | VARCHAR2 | 240 |  |  | SUBJECT_TYPE |
| SUBJECT_KEY | VARCHAR2 | 240 |  |  | SUBJECT_KEY |
| ALLOCATION_CRITERIA_ID | NUMBER |  | 18 |  | ALLOCATION_CRITERIA_ID |
| BATCH_ACTION_ID | NUMBER |  | 18 | Yes | BATCH_ACTION_ID |
| EXCLUDE_FLAG | VARCHAR2 | 4 |  | Yes | EXCLUDE_FLAG |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | ENABLED_FLAG |
| CRITERION_TYPE | VARCHAR2 | 30 |  | Yes | CRITERION_TYPE |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| PROCESSED_FLAG | VARCHAR2 | 4 |  | Yes | PROCESSED_FLAG |
| REFERENCE_TYPE | VARCHAR2 | 30 |  |  | REFERENCE_TYPE |
| REFERENCE_ID | NUMBER |  | 18 |  | REFERENCE_ID |
| REFERENCE_DATE | DATE |  |  |  | REFERENCE_DATE |
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
|---|---|---|---|
| PER_CHK_BATCH_CRITERIA_N1 | Non Unique | Default | BATCH_ACTION_ID |
| PER_CHK_BATCH_CRITERIA_N2 | Non Unique | Default | ALLOCATION_CRITERIA_ID |
| PER_CHK_BATCH_CRITERIA_PK | Unique | Default | BATCH_CRITERIA_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
