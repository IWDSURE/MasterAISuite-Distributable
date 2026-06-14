# PER_CHK_ARCH_ALLOC_TASKS_TL

PER_CHK_ARCH_ALLOC_TASKS_TL : This is translation table for PER_CHK_ARCH_ALLOC_TASKS

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloctaskstl-8476.html#perchkarchalloctaskstl-8476](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloctaskstl-8476.html#perchkarchalloctaskstl-8476)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_ARCH_ALLOC_TASKS_TL_PK | ALLOCATED_TASK_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOCATED_TASK_ID | NUMBER |  | 18 | Yes | ALLOCATED_TASK_ID |
| NOTE_TITLE | VARCHAR2 | 150 |  |  | Stores title for notes section |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| TASK_NAME | VARCHAR2 | 240 |  | Yes | TASK_NAME |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | DESCRIPTION |
| ACTION_URL | VARCHAR2 | 1000 |  |  | ACTION_URL |
| USER_DISPLAY_NAME | VARCHAR2 | 240 |  |  | USER_DISPLAY_NAME |
| TASK_DETAILS | CLOB |  |  |  | TASK_DETAILS |
| MEETING_LOCATION | VARCHAR2 | 240 |  |  | MEETING_LOCATION |
| COMPLETE_ACTION_LABEL | VARCHAR2 | 120 |  |  | COMPLETE_ACTION_LABEL |
| REJECT_ACTION_LABEL | VARCHAR2 | 120 |  |  | REJECT_ACTION_LABEL |
| SAVE_ACTION_LABEL | VARCHAR2 | 120 |  |  | SAVE_ACTION_LABEL |
| CALENDAR_ACTION_LABEL | VARCHAR2 | 120 |  |  | CALENDAR_ACTION_LABEL |
| ACTIVITY_ACTION1_LABEL | VARCHAR2 | 120 |  |  | ACTIVITY_ACTION1_LABEL |
| ACTIVITY_ACTION2_LABEL | VARCHAR2 | 120 |  |  | ACTIVITY_ACTION2_LABEL |
| ACTIVITY_ACTION3_LABEL | VARCHAR2 | 120 |  |  | ACTIVITY_ACTION3_LABEL |
| ACTIVITY_ACTION4_LABEL | VARCHAR2 | 120 |  |  | ACTIVITY_ACTION4_LABEL |
| ACTIVITY_ACTION5_LABEL | VARCHAR2 | 120 |  |  | ACTIVITY_ACTION5_LABEL |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_ARCH_ALLOC_TASKS_TL_PK | Unique | FUSION_TS_TX_DATA | ALLOCATED_TASK_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
