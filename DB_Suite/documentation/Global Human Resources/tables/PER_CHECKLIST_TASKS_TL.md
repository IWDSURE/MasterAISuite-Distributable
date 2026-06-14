# PER_CHECKLIST_TASKS_TL

PER_CHECKLIST_TASKS_TL : This is the translation table for PER_CHECKLIST_TASKS_B

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklisttaskstl-6305.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklisttaskstl-6305.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_TASKS_TL_PK | CHECKLIST_TASK_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_TASK_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CHECKLIST_TASKS-B.CHECKLIST_TASK_ID |
| NOTE_TITLE | VARCHAR2 | 150 |  |  | Stores title for notes section |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CHECKLIST_TASK_NAME | VARCHAR2 | 240 |  | Yes | Task Name |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Task Description |
| ACTION_URL | VARCHAR2 | 1000 |  |  | Task Action URL
When action type is ORA_EXTERNAL_URL then this is mandatory. |
| USER_DISPLAY_NAME | VARCHAR2 | 240 |  |  | USER_DISPLAY_NAME |
| TASK_DETAILS | CLOB |  |  |  | Task Details (Rich Details) |
| MEETING_LOCATION | VARCHAR2 | 240 |  |  | Meeting Location for task type meeting |
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
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLIST_TASKS_TL_PK | Unique | FUSION_TS_TX_DATA | CHECKLIST_TASK_ID, LANGUAGE, ORA_SEED_SET1 |
| PER_CHECKLIST_TASKS_TL_PK1 | Unique | FUSION_TS_TX_DATA | CHECKLIST_TASK_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
