# HTS_SCHEDULE_TASK_PARAMS

This table stores the parameter related to tasks in the hts_schedule_tasks table.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduletaskparams-24061.html#htsscheduletaskparams-24061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduletaskparams-24061.html#htsscheduletaskparams-24061)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_TASK_PARAMS_PK | TASK_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_PARAM_ID | NUMBER |  | 18 | Yes | Indicates the task parameter identifier. |
| TASK_ID | NUMBER |  | 18 | Yes | Indicates the reference task identifier for which this parameter is added. |
| NAME | VARCHAR2 | 80 |  | Yes | Indicates the name of the parameter. |
| TEXT_VALUE | VARCHAR2 | 4000 |  |  | Indicates the text value of the parameter. |
| NUMBER_VALUE | NUMBER |  |  |  | Indicates the number value of the parameter. |
| DATE_VALUE | DATE |  |  |  | Indicates the date value of the parameter. |
| TYPE | VARCHAR2 | 20 |  | Yes | Indicates the basic java data type of the parameter such as STRING, LONG, INTEGER or DATE. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Indicates enterprise identifier. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULE_TASK_PARAMS_N1 | Non Unique | Default | TASK_ID |
| HTS_SCHEDULE_TASK_PARAMS_PK | Unique | Default | TASK_PARAM_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
