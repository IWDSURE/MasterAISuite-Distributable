# PAY_FLOW_TASK_INSTANCES

Table capturing the flow task instance details

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskinstances-20726.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskinstances-20726.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_TASK_INSTANCES_PK | FLOW_TASK_INSTANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_TASK_INSTANCE_ID | NUMBER |  | 18 | Yes | FLOW_TASK_INSTANCE_ID |
| VERIFY_FLAG | VARCHAR2 | 2 |  |  | VERIFY_FLAG |
| DYN_SKIPPED_FLAG | VARCHAR2 | 2 |  |  | DYN_SKIPPED_FLAG |
| FLOW_TASK_ID | NUMBER |  | 18 |  | FLOW_TASK_ID |
| BASE_TASK_ACTION_ID | NUMBER |  | 18 |  | Current running Action ID reference |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FLOW_INSTANCE_ID | NUMBER |  | 18 | Yes | FLOW_INSTANCE_ID |
| BASE_FLOW_TASK_ID | NUMBER |  | 18 | Yes | BASE_FLOW_TASK_ID |
| ESS_SERVICE_EXEC_ID | NUMBER |  | 18 |  | ESS_SERVICE_EXEC_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| START_DATE | DATE |  |  |  | START_DATE |
| SCHEDULED_DATE | TIMESTAMP |  |  |  | Captures the scheduled start date of flow task instance |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| UI_TASK_STATUS | VARCHAR2 | 20 |  |  | TASK_STATUS |
| IS_MFR | VARCHAR2 | 20 |  |  | IS_MFR |
| IS_ERROR | VARCHAR2 | 20 |  |  | IS_ERROR |
| IS_ROLLEDBACK | VARCHAR2 | 20 |  |  | IS_ROLLEDBACK |
| FI_TOTAL_COMPLETED | NUMBER |  |  |  | TOTAL_COMPLETED |
| LOG_LEVEL | VARCHAR2 | 80 |  |  | LOG_LEVEL |
| POST_PROCESSING_FLAG | VARCHAR2 | 2 |  |  | POST_PROCESSING_FLAG |
| IS_EMBEDDED_TASK_HISTORY | VARCHAR2 | 2 |  |  | IS_EMBEDDED_TASK_HISTORY |
| OUTBOUND_STATUS | VARCHAR2 | 20 |  |  | OUTBOUND_STATUS |
| IS_CANCELLING | VARCHAR2 | 2 |  |  | IS_CANCELLING |
| IS_BG_PROCESSING_ACTIVE | VARCHAR2 | 1 |  |  | IS_BG_PROCESSING_ACTIVE |
| BG_PROCESSING_STATUS | VARCHAR2 | 50 |  |  | BG_PROCESSING_STATUS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_FLOW_TASK_INSTANCES_FK1 | Non Unique | Default | FLOW_INSTANCE_ID |
| PAY_FLOW_TASK_INSTANCES_PK | Unique | Default | FLOW_TASK_INSTANCE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
