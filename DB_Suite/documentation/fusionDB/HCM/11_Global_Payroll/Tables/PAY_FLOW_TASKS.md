# PAY_FLOW_TASKS

PAY_FLOW_TASKS captures the flow task details

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtasks-23477.html#payflowtasks-23477](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtasks-23477.html#payflowtasks-23477)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_TASKS_PK | FLOW_TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_TASK_ID | NUMBER |  | 18 | Yes | FLOW_TASK_ID |
| TASK_ALERT_CODE | VARCHAR2 | 1000 |  |  | TASK_ALERT_CODE |
| ESS_REQUEST_CATEGORY | VARCHAR2 | 100 |  |  | ESS_REQUEST_CATEGORY |
| START_NOTIF_FLAG | VARCHAR2 | 1 |  |  | START_NOTIF_FLAG |
| END_NOTIF_FLAG | VARCHAR2 | 1 |  |  | END_NOTIF_FLAG |
| OVERDUE_NOTIF_FLAG | VARCHAR2 | 1 |  |  | OVERDUE_NOTIF_FLAG |
| WARNING_NOTIF_FLAG | VARCHAR2 | 1 |  |  | WARNING_NOTIF_FLAG |
| ERROR_NOTIF_FLAG | VARCHAR2 | 1 |  |  | ERROR_NOTIF_FLAG |
| BASE_FLOW_TASK_ID | NUMBER |  | 18 | Yes | BASE_FLOW_TASK_ID |
| BASE_FLOW_TASK_NAME | VARCHAR2 | 100 |  | Yes | BASE_FLOW_TASK_NAME |
| IGNORE_PREREQ_FLAG | VARCHAR2 | 1 |  |  | IGNORE_PREREQ_FLAG |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BASE_TASK_ID | NUMBER |  | 18 | Yes | BASE_TASK_ID |
| BASE_FLOW_ID | NUMBER |  | 18 |  | BASE_FLOW_ID |
| CATEGORY_TYPE | VARCHAR2 | 30 |  |  | CATEGORY_TYPE |
| SUB_CATEGORY_TYPE | VARCHAR2 | 30 |  |  | SUB_CATEGORY_TYPE |
| PRE_CUSTOM_SERVICE | VARCHAR2 | 200 |  |  | PRE_CUSTOM_SERVICE |
| POST_CUSTOM_SERVICE | VARCHAR2 | 200 |  |  | POST_CUSTOM_SERVICE |
| OFFSET_FLOW_PARAMETER_ID | NUMBER |  | 18 |  | OFFSET_FLOW_PARAMETER_ID |
| START_DATE_OFFSET_ID | NUMBER |  | 18 |  | START DATE OFFSET ID |
| START_DATE_OFFSET_VALUE | VARCHAR2 | 20 |  |  | START DATE OFFSET VALUE |
| OFFSET_VALUE | VARCHAR2 | 20 |  |  | OFFSET_VALUE |
| DEST_UI_URL | VARCHAR2 | 200 |  |  | DEST_UI_URL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |
| START_SCH_TIME_DEF_ID | NUMBER |  | 18 |  | Time definition id that defaults the scheduled submission time of the flow task |
| START_SCH_FORMULA_ID | NUMBER |  | 18 |  | Formula that when evaluated gives the scheduled start time for the individual flow task |
| SUBMITTING_USER_FLAG | VARCHAR2 | 1 |  |  | SUBMITTING_USER_FLAG |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| EMP_ALERT_CODE | VARCHAR2 | 1000 |  |  | EMP_ALERT_CODE |
| CMPLETD_ALRTS_NOTIF_FLAG | VARCHAR2 | 1 |  |  | CMPLETD_ALRTS_NOTIF_FLAG |
| INACTIVE_FLAG | VARCHAR2 | 1 |  |  | INACTIVE_FLAG |
| VERIFY_FLAG | VARCHAR2 | 1 |  |  | VERIFY_FLAG |
| CRITICAL_ALERTS_NOTIF_FLAG | VARCHAR2 | 1 |  |  | CRITICAL_ALERTS_NOTIF_FLAG |
| CORR_PROCESSES_NOTIF_FLAG | VARCHAR2 | 1 |  |  | CORR_PROCESSES_NOTIF_FLAG |
| OUTBOUND_ENABLED_FLAG | VARCHAR2 | 1 |  |  | OUTBOUND_ENABLED_FLAG |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLOW_TASKS_N1 | Non Unique | Default | BASE_FLOW_TASK_ID |
| PAY_FLOW_TASKS_N20 | Non Unique | Default | SGUID |
| PAY_FLOW_TASKS_PK | Unique | Default | FLOW_TASK_ID, ORA_SEED_SET1 |
| PAY_FLOW_TASKS_PK1 | Unique | Default | FLOW_TASK_ID, ORA_SEED_SET2 |
| PAY_FLOW_TASKS_U1 | Unique | Default | BASE_FLOW_TASK_NAME, BASE_FLOW_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_FLOW_TASKS_U11 | Unique | Default | BASE_FLOW_TASK_NAME, BASE_FLOW_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
