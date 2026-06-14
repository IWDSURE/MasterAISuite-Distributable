# PAY_TASK_ACTIONS

PAY _TASK_ACTIONS TABLE TO STORE PAYROLLFLOWS ACTIONS

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskactions-8283.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskactions-8283.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TASK_ACTIONS_PK | TASK_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ACTION_ID | NUMBER |  | 18 | Yes | TASK_ACTION_ID |
| BASE_TASK_ACTION_ID | NUMBER |  | 18 | Yes | BASE_TASK_ACTION_ID |
| BASE_TASK_ACTION_NAME | VARCHAR2 | 100 |  | Yes | BASE_TASK_ACTION_NAME |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| EXECUTION_MODE | VARCHAR2 | 20 |  |  | EXECUTION_MODE |
| DEFAULT_ACTION_FLAG | VARCHAR2 | 1 |  |  | DEFAULT_ACTION_FLAG |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | ACTIVE_FLAG |
| ACTION_TYPE | VARCHAR2 | 20 |  |  | ACTION_TYPE |
| ACTION_METHOD | VARCHAR2 | 200 |  |  | ACTION_METHOD |
| ACTION_SEQUENCE | VARCHAR2 | 1 |  |  | ACTION_SEQUENCE |
| BASE_TASK_ID | NUMBER |  | 18 |  | BASE_TASK_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PARENT_ACTION_FLAG | VARCHAR2 | 1 |  |  | PARENT_ACTION_FLAG |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TASK_ACTIONS_N1 | Non Unique | Default | BASE_TASK_ACTION_ID |
| PAY_TASK_ACTIONS_N2 | Non Unique | Default | BASE_TASK_ID |
| PAY_TASK_ACTIONS_N20 | Non Unique | Default | SGUID |
| PAY_TASK_ACTIONS_U1 | Unique | Default | TASK_ACTION_ID, ORA_SEED_SET1 |
| PAY_TASK_ACTIONS_U11 | Unique | Default | TASK_ACTION_ID, ORA_SEED_SET2 |
| PAY_TASK_ACTIONS_U2 | Unique | Default | BASE_TASK_ACTION_NAME, BASE_TASK_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_TASK_ACTIONS_U21 | Unique | Default | BASE_TASK_ACTION_NAME, BASE_TASK_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
