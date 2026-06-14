# PAY_FLOW_INSTANCES

Its an Instance table to capture Flow Instances

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowinstances-15514.html#payflowinstances-15514](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowinstances-15514.html#payflowinstances-15514)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_INSTANCES_PK | FLOW_INSTANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_INSTANCE_ID | NUMBER |  | 18 | Yes | This column is the primary key of the table pay_flow_instances. |
| FLOW_CATEGORIES | VARCHAR2 | 100 |  |  | This column contains the flow category value of the flow instance. |
| CONTEXT_PARAM_VALUES | CLOB |  |  |  | This column contains the context param values of the flow instance. |
| SUBMISSION_CONTEXT | VARCHAR2 | 100 |  |  | This column contains the submission context value of the flow instance. |
| ROOT_FLOW_INSTANCE_ID | NUMBER |  | 18 |  | This column contains the root flow instance id of the flow instance. |
| INSTANCE_NAME | VARCHAR2 | 200 |  |  | This column contains the instance name of the flow instance. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | This column contains the ldg id of the flow instance. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | This column contains the value of legislation code which is foreign key to FND_TERRITORIES. |
| BASE_FLOW_ID | NUMBER |  | 18 | Yes | This column contains the base flow id of the flow instance. |
| FI_TASK_STATUS | VARCHAR2 | 20 |  |  | This column contains the flow instance task status. |
| FI_PAYROLL_ID | NUMBER |  | 20 |  | This column contains the flow instance payroll id. |
| FI_PAYROLL_PERIOD | NUMBER |  | 18 |  | This column contains the flow instance payroll period. |
| FI_PROCESS_DATE | DATE |  |  |  | This column contains the flow instance process date. |
| FI_TASK_TYPE | VARCHAR2 | 20 |  |  | This column contains the flow instance task type. |
| ERRORED | VARCHAR2 | 1 |  |  | This column contains the errored flag value of the flow. |
| MARKED_FOR_RETRY | VARCHAR2 | 1 |  |  | This column contains the marked for retry value of the flow instance. |
| REVERSED | VARCHAR2 | 1 |  |  | This column contains the reversed value of the flow instance. |
| NUMBER_OF_TASKS | NUMBER |  | 3 |  | This column contains the number of tasks value in the flow instance. |
| FI_COMPLETED_TASKS | NUMBER |  | 3 |  | This column contains the number of completed task in the flow instance. |
| RECUR_SCH_FORMULA_ID | NUMBER |  | 18 |  | Formula to calculate a recurring schedule for flow instance |
| RECUR_TIME_COMPONENT | VARCHAR2 | 50 |  |  | This column contains the recur time component value in the flow instance. |
| PROGRESS | NUMBER |  | 9 |  | This column contains the number of progress task in the flow instance. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This column contains the value of enterprise id which is foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RUN_ID | NUMBER |  | 18 |  | This column contains the run id of the flow instance. |
| STATUS | VARCHAR2 | 30 |  |  | This column contains the status of the flow instance. |
| RECUR_SCH_TIME_DEF_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID: Column used to capture TimeDefinitionId that will define the recurring schedule. |
| SCHEDULED_DATE | TIMESTAMP |  |  |  | Column capturing the scheduled execution date for the flow instance. |
| SCHEDULE_END_DATE | TIMESTAMP |  |  |  | Timestamp capturing end of the recurring schedule. |
| RECURRING_FLAG | VARCHAR2 | 1 |  |  | Flag indicating if the flow instance need to be submitted recurringly |
| FI_TASK_FLOW_FLAG | VARCHAR2 | 2 |  |  | Flag indicating whether the tasks belongs to a composite flow or not. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 20 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 20 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 20 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| INSTANTIATED_BY | VARCHAR2 | 100 |  | Yes | This column contains the instantiated by value of the flow instance. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| EXECUTION_MODE | VARCHAR2 | 20 |  |  | This column contains the execution mode value of the flow. |
| FI_TOTAL_COMPLETED | NUMBER |  |  |  | This column contains the number of total completed flow instance. |
| FI_ROLLEDBACK | VARCHAR2 | 30 |  |  | This column contains the rolledback value of flow instance. |
| FLOW_INSTANCE_NAME_UNIQUE | VARCHAR2 | 200 |  |  | This column contains the name unique value of flow instance. |
| FLOW_INSTANCE_UNIQUE | VARCHAR2 | 200 |  |  | This column contains the unique value of flow instance. |
| IS_FULL_ROLLBACK | VARCHAR2 | 30 |  |  | This column contains the is full rollback value of flow instance. |
| IS_SKIPPED | VARCHAR2 | 30 |  |  | This column contains the is skipped value of flow instance. |
| IS_INCOMPLETE | VARCHAR2 | 30 |  |  | This column contains the is incomplete value of flow instance. |
| IS_EXTRACT | VARCHAR2 | 2 |  |  | This column contains the is extract value of flow instance. |
| IS_DATA_LOADER | VARCHAR2 | 2 |  |  | This column contains the is data loader value of flow instance. |
| FLOW_ID | NUMBER |  | 18 |  | This column contains the flow id value of flow instance. |
| SUB_STATUS | VARCHAR2 | 40 |  |  | This column contains the sub status value of flow instance. |
| AC_TYPE | VARCHAR2 | 10 |  |  | This column contains the ac type value of flow instance. |
| OUTBOUND_ENABLED_FLAG | VARCHAR2 | 1 |  |  | This column contains the outbound enabled flag value of flow instance. |
| IS_BG_PROCESSING_ACTIVE | VARCHAR2 | 1 |  |  | This column contains the is bg processing active value of flow instance. |
| BG_PROCESSING_STATUS | VARCHAR2 | 50 |  |  | This column contains the bg processing status value of flow instance. |
| IS_VERIFY_PENDING | VARCHAR2 | 4 |  |  | This column contains the is verify pending value of flow instance. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLOW_INSTANCES_N1 | Non Unique | Default | BASE_FLOW_ID, STATUS, CREATION_DATE |
| PAY_FLOW_INSTANCES_N2 | Non Unique | Default | STATUS |
| PAY_FLOW_INSTANCES_N3 | Non Unique | Default | INSTANCE_NAME |
| PAY_FLOW_INSTANCES_N5 | Non Unique | Default | CREATION_DATE, CREATED_BY, INSTANTIATED_BY |
| PAY_FLOW_INSTANCES_PK | Unique | Default | FLOW_INSTANCE_ID |
| PAY_FLOW_INSTANCES_U1 | Unique | Default | LEGISLATIVE_DATA_GROUP_ID, BASE_FLOW_ID, NVL("FLOW_INSTANCE_NAME_UNIQUE","FLOW_INSTANCE_ID") |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
