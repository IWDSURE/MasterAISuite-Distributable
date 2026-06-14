# PER_CHK_ALLOC_TASK_RESULTS

Table to hold checklist task allocation result state

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** DEFAULT

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkalloctaskresults-29441.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkalloctaskresults-29441.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_ALLOC_TASK_RESULTS_PK | CHK_ALLOC_TASK_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHK_ALLOC_TASK_RESULT_ID | NUMBER |  | 18 | Yes | CHK_ALLOC_TASK_RESULT_ID |
| CHK_ALLOC_RESULT_ID | NUMBER |  | 18 | Yes | CHK_ALLOC_RESULT_ID |
| START_DATE_TIME | TIMESTAMP |  |  |  | START_DATE_TIME |
| END_DATE_TIME | TIMESTAMP |  |  |  | END_DATE_TIME |
| COMPLETED_BY | VARCHAR2 | 64 |  |  | COMPLETED_BY |
| COMPLETION_DATE | DATE |  |  |  | COMPLETION_DATE |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| USER_GUID | VARCHAR2 | 64 |  |  | USER_GUID |
| TASK_TYPE | VARCHAR2 | 30 |  |  | TASK_TYPE |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 |  | TASK_IN_CHECKLIST_ID |
| PARENT_CHECKLIST_ID | NUMBER |  | 18 |  | PARENT_CHECKLIST_ID |
| STATUS | VARCHAR2 | 60 |  |  | STATUS |
| TASK_SEQUENCE | NUMBER |  | 9 |  | TASK_SEQUENCE |
| OBJECT_REFERENCE_ID | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID |
| OBJECT_REFERENCE_ID1 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID1 |
| OBJECT_REFERENCE_ID2 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID2 |
| OBJECT_REFERENCE_KEY | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY |
| OBJECT_REFERENCE_KEY1 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY1 |
| OBJECT_REFERENCE_KEY2 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY2 |
| DW_INSTRUCTION_ID | NUMBER |  | 18 |  | DW_INSTRUCTION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHK_ALLOC_TASK_RESULTS_PK | Unique | DEFAULT | CHK_ALLOC_TASK_RESULT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
