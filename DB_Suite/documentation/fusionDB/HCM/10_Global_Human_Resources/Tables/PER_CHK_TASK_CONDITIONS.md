# PER_CHK_TASK_CONDITIONS

PER_CHK_TASK_CONDITIONS: Stores condition to activate a task.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchktaskconditions-11321.html#perchktaskconditions-11321](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchktaskconditions-11321.html#perchktaskconditions-11321)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_TASK_CONDITIONS_PK | TASK_CONDITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_CONDITION_ID | NUMBER |  | 18 | Yes | TASK_CONDITION_ID |
| TASK_ACTION_CODE | VARCHAR2 | 250 |  | Yes | TASK_ACTION_CODE |
| ACTION_TYPE | VARCHAR2 | 80 |  | Yes | ACTION_TYPE |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | TASK_IN_CHECKLIST_ID |
| EVENT_CODE | VARCHAR2 | 270 |  |  | EVENT_CODE |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | ENABLED_FLAG |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CONDITION_TEXT1 | VARCHAR2 | 4000 |  |  | CONDITION_TEXT1 |
| CONDITION_TEXT2 | VARCHAR2 | 4000 |  |  | CONDITION_TEXT2 |
| CONDITION_TEXT3 | VARCHAR2 | 4000 |  |  | CONDITION_TEXT3 |
| CONDITION_TEXT4 | VARCHAR2 | 4000 |  |  | CONDITION_TEXT4 |
| CONDITION_TEXT5 | VARCHAR2 | 4000 |  |  | CONDITION_TEXT5 |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_TASK_CONDITIONS_N1 | Non Unique | Default | TASK_IN_CHECKLIST_ID |
| PER_CHK_TASK_CONDITIONS_PK | Unique | Default | TASK_CONDITION_ID, ORA_SEED_SET1 |
| PER_CHK_TASK_CONDITIONS_PK1 | Unique | Default | TASK_CONDITION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
