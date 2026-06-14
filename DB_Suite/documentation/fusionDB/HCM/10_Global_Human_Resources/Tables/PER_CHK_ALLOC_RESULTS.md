# PER_CHK_ALLOC_RESULTS

Table to hold checklist allocation result state

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** DEFAULT

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkallocresults-9198.html#perchkallocresults-9198](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkallocresults-9198.html#perchkallocresults-9198)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_ALLOC_RESULTS_PK | CHK_ALLOC_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHK_ALLOC_RESULT_ID | NUMBER |  | 18 | Yes | CHK_ALLOC_RESULT_ID |
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 |  | ALLOCATED_CHECKLIST_ID |
| INITIATOR_PERSON_ID | NUMBER |  | 18 |  | INITIATOR_PERSON_ID |
| INITIATOR_USER | VARCHAR2 | 64 |  |  | INITIATOR_USER |
| SELF_ASSIGNED_FLAG | VARCHAR2 | 4 |  |  | SELF_ASSIGNED_FLAG |
| DEF_COMPLETION_DATE | DATE |  |  |  | DEF_COMPLETION_DATE |
| CHECKLIST_INSTANCE | VARCHAR2 | 20 |  |  | CHECKLIST_INSTANCE |
| CHECKLIST_ID | NUMBER |  | 18 |  | CHECKLIST_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| CHECKLIST_CATEGORY | VARCHAR2 | 60 |  |  | CHECKLIST_CATEGORY |
| CHECKLIST_STATUS | VARCHAR2 | 60 |  |  | CHECKLIST_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| COMPLETED_ON | VARCHAR2 | 30 |  |  | COMPLETED_ON |
| COMPLETION_DATE | DATE |  |  |  | COMPLETION_DATE |
| COMPLETED_BY | VARCHAR2 | 64 |  |  | COMPLETED_BY |
| CHECKLIST_SUB_CATEGORY | VARCHAR2 | 60 |  |  | CHECKLIST_SUB_CATEGORY |
| SUBJECT_TYPE | VARCHAR2 | 240 |  |  | SUBJECT_TYPE |
| SUBJECT_KEY | VARCHAR2 | 240 |  |  | SUBJECT_KEY |
| OBJECT_REFERENCE_ID | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID |
| OBJECT_REFERENCE_ID1 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID1 |
| OBJECT_REFERENCE_ID2 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID2 |
| OBJECT_REFERENCE_KEY | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY |
| OBJECT_REFERENCE_KEY1 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY1 |
| OBJECT_REFERENCE_KEY2 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY2 |
| USER_GUID | VARCHAR2 | 64 |  |  | USER_GUID |
| START_DATE_TIME | TIMESTAMP |  |  |  | START_DATE_TIME |
| END_DATE_TIME | TIMESTAMP |  |  |  | END_DATE_TIME |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_ALLOC_RESULTS_PK | Unique | DEFAULT | CHK_ALLOC_RESULT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
