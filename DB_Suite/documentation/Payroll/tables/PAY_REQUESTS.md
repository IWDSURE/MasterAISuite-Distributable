# PAY_REQUESTS

PAY_REQUESTS_TABLE captures all the requests details for the flow

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrequests-9896.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrequests-9896.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REQUESTS_PK | PAY_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_REQUEST_ID | NUMBER |  | 18 | Yes | PAY_REQUEST_ID |
| TASK_ACTION_SEQ | NUMBER |  | 18 |  | TASK_ACTION_SEQ |
| FLOW_INSTANCE_ID | NUMBER |  | 18 |  | FLOW_INSTANCE_ID |
| ITER_FLOW_INSTANCE_ID | NUMBER |  | 18 |  | ITER_FLOW_INSTANCE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FLOW_TASK_INSTANCE_ID | NUMBER |  | 18 |  | FLOW_TASK_INSTANCE_ID |
| CALL_TYPE | VARCHAR2 | 30 |  |  | CALL_TYPE |
| CALL_ID | NUMBER |  | 18 |  | CALL_ID |
| PAY_TASK_ACTION_ID | NUMBER |  | 18 |  | PAY_TASK_ACTION_ID |
| PARAM_NAME_VALS | CLOB |  |  |  | PARAM_NAME_VALS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ITERATION_LABEL | VARCHAR2 | 4000 |  |  | ITERATION_LABEL |
| ITERATION_BASE_TASK_NAME | VARCHAR2 | 100 |  |  | ITERATION_BASE_TASK_NAME |
| ABS_PARENT_REQUEST_ID | NUMBER |  | 18 |  | ABS_PARENT_REQUEST_ID |
| EXECUTION_MODE | VARCHAR2 | 20 |  |  | EXECUTION_MODE |
| PAYROLL_RELATIONSHIP_GROUP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_GROUP_ID |
| PARENT_PAY_REQUEST_ID | NUMBER |  | 18 |  | PARENT_PAY_REQUEST_ID |
| ACTION_CONTEXT | VARCHAR2 | 20 |  |  | ACTION_CONTEXT |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REQUESTS_FK1 | Non Unique | Default | FLOW_INSTANCE_ID |
| PAY_REQUESTS_FK2 | Non Unique | Default | FLOW_TASK_INSTANCE_ID |
| PAY_REQUESTS_N1 | Non Unique | Default | CALL_TYPE, CALL_ID |
| PAY_REQUESTS_PK | Unique | Default | PAY_REQUEST_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
