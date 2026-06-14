# PER_TASKS_IN_CHECKLIST_TL

PER_TASKS_IN_CHECKLIST_TL holds translated information for Checklist Templates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasksinchecklisttl-15525.html#pertasksinchecklisttl-15525](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasksinchecklisttl-15525.html#pertasksinchecklisttl-15525)

## Primary Key

| Name | Columns |
|------|----------|
| PER_TASKS_IN_CHECKLIST_TL_PK | TASK_IN_CHECKLIST_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| NOTE_TITLE | VARCHAR2 | 150 |  |  | Stores title for notes section |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CHECKLIST_TASK_NAME | VARCHAR2 | 240 |  | Yes | Translated name of Checklist Template Task |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Translated description of Checklist Template Task |
| ACTION_URL | VARCHAR2 | 1000 |  |  | Translated Action URL of Checklist Template Task |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
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
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| USER_DISPLAY_NAME | VARCHAR2 | 240 |  |  | USER_DISPLAY_NAME |
| TASK_DETAILS | CLOB |  |  |  | Task Details (Rich Details) |
| MEETING_LOCATION | VARCHAR2 | 240 |  |  | Meeting Location for task type meeting |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_TASKS_IN_CHECKLIST_TL_PK | Unique | FUSION_TS_TX_DATA | TASK_IN_CHECKLIST_ID, LANGUAGE, ORA_SEED_SET1 |
| PER_TASKS_IN_CHECKLIST_TL_PK1 | Unique | FUSION_TS_TX_DATA | TASK_IN_CHECKLIST_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
