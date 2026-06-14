# PAY_FLOW_METRICS

This table is used to store the metrics for a flow.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowmetrics-20566.html#payflowmetrics-20566](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowmetrics-20566.html#payflowmetrics-20566)

## Primary Key

| Name | Columns |
|------|----------|
| pay_flow_metrics_PK | FLOW_METRICS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_METRICS_ID | NUMBER |  |  | Yes | FLOW_METRICS_ID |
| BASE_FLOW_ID | NUMBER |  |  | Yes | BASE_FLOW_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  |  |  | LEGISLATIVE_DATA_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LATEST_INSTANCE_ID | NUMBER |  |  | Yes | LATEST_INSTANCE_ID |
| LATEST_EXECUTION_DATE | TIMESTAMP |  |  | Yes | LATEST_EXECUTION_DATE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| pay_flow_metrics_PK | Unique | Default | FLOW_METRICS_ID |
| pay_flow_metrics_U1 | Unique | Default | BASE_FLOW_ID, LEGISLATIVE_DATA_GROUP_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
