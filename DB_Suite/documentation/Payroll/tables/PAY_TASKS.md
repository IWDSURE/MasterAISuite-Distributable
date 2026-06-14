# PAY_TASKS

PAY_TASK describes the tasks that can take part in process flows

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytasks-15936.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytasks-15936.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TASKS_PK | TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 | Yes | TASK_ID |
| ESS_REQUEST_CATEGORY | VARCHAR2 | 100 |  |  | ESS_REQUEST_CATEGORY |
| BASE_TASK_ID | NUMBER |  | 18 | Yes | BASE_TASK_ID |
| BASE_TASK_NAME | VARCHAR2 | 100 |  | Yes | BASE_TASK_NAME |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TASK_TYPE | VARCHAR2 | 30 |  |  | TASK_TYPE |
| AUTOMATIC_FLAG | VARCHAR2 | 1 |  |  | AUTOMATIC_FLAG |
| DEF_CATEGORY_TYPE | VARCHAR2 | 30 |  |  | DEF_CATEGORY_TYPE |
| DEF_SUB_CATEGORY_TYPE | VARCHAR2 | 30 |  |  | DEF_SUB_CATEGORY_TYPE |
| DEFAULT_CHECKLIST_NAME | VARCHAR2 | 100 |  |  | DEFAULT_CHECKLIST_NAME |
| NAME_SPACE | VARCHAR2 | 200 |  |  | NAME_SPACE |
| DEST_UI_URL | VARCHAR2 | 200 |  |  | DEST_UI_URL |
| ACTION_FREEZE_FLAG | VARCHAR2 | 1 |  |  | ACTION_FREEZE_FLAG |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| START_SCH_TIME_DEF_ID | NUMBER |  | 18 |  | Time definition id that defaults the scheduled submission time of the task when the task participates in the flow |
| START_SCH_FORMULA_ID | NUMBER |  | 18 |  | Formula that when evaluated gives the scheduled start time for the individual flow task |
| SUBMITTING_USER_FLAG | VARCHAR2 | 1 |  |  | SUBMITTING_USER_FLAG |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| HIDE_INCOMPLT_ACTION_FLAG | VARCHAR2 | 1 |  |  | Indicates whether to show or hide Mark as Incomplete action for a task |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TASKS_N1 | Non Unique | Default | BASE_TASK_ID |
| PAY_TASKS_PK | Unique | Default | TASK_ID, ORA_SEED_SET1 |
| PAY_TASKS_PK1 | Unique | Default | TASK_ID, ORA_SEED_SET2 |
| PAY_TASKS_U1 | Unique | Default | BASE_TASK_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_TASKS_U11 | Unique | Default | BASE_TASK_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
