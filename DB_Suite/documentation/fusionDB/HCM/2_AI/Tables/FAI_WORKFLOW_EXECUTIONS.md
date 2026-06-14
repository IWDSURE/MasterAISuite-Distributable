# FAI_WORKFLOW_EXECUTIONS

This table will store workflow agent execution details in each workflow step.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowexecutions-15103.html#faiworkflowexecutions-15103](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowexecutions-15103.html#faiworkflowexecutions-15103)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_WORKFLOW_EXECUTIONS_PK | WORKFLOW_EXECUTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKFLOW_EXECUTION_ID | NUMBER |  | 18 | Yes | The system generated primary key. |
| WORKFLOW_ID | NUMBER |  | 18 | Yes | Foreign key referencing to FAI_WORKFLOWS table. |
| EXECUTION_GROUP_NUMBER | VARCHAR2 | 200 |  | Yes | Collection of workflow execution steps grouped within one workflow execution. |
| TRACE | VARCHAR2 | 200 |  |  | Execution traceId captured at runtime. |
| TYPE | VARCHAR2 | 200 |  |  | This field will capture type of execution. |
| STEP | VARCHAR2 | 200 |  |  | This field will store Workflow step of this execution. |
| AGENT_ID | NUMBER |  | 18 |  | Foreign key reference to HR_GEN_AI_AGENTS table. |
| OWNER_ID | NUMBER |  | 18 |  | The user identification who executes the Workflow. |
| EXECUTION_DETAILS | CLOB |  |  |  | This field will store details of step execution. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| EXECUTION_TIME | NUMBER |  | 10 |  | Time taken to execute the step |
| LLM_REQ_INPUT_TOKEN_CNT | NUMBER |  | 10 |  | Token count for  LLM input |
| LLM_OUTPUT_TOKEN_CNT | NUMBER |  | 10 |  | Token count for LLM output |
| SOURCE | VARCHAR2 | 200 |  | Yes | Source of invocation. Can be Admin/Eval/End_User etc., |
| TRIGGER_TYPE | VARCHAR2 | 200 |  | Yes | Conversation was triggered by Email/Webhook etc., |
| WORKFLOW_CODE | VARCHAR2 | 200 |  |  | Workflow Code referencing to FAI_WORKFLOWS table. |
| STATUS | VARCHAR2 | 32 |  |  | Workflow Status referencing to FAI_WORKFLOWS table. |
| VERSION | NUMBER |  | 9 |  | Workflow Version referencing to FAI_WORKFLOWS table. |
| APPLICATION_CODE | VARCHAR2 | 300 |  |  | Stores the code of the application |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_WORKFLOW_EXECUTIONS_N1 | Non Unique | Default | WORKFLOW_ID |
| FAI_WORKFLOW_EXECUTIONS_N2 | Non Unique | Default | AGENT_ID |
| FAI_WORKFLOW_EXECUTIONS_N3 | Non Unique | Default | EXECUTION_GROUP_NUMBER |
| FAI_WORKFLOW_EXECUTIONS_N4 | Non Unique | Default | OWNER_ID, TYPE, STEP |
| FAI_WORKFLOW_EXECUTIONS_N5 | Non Unique | Default | OWNER_ID, TRACE |
| FAI_WORKFLOW_EXECUTIONS_PK | Unique | Default | WORKFLOW_EXECUTION_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
