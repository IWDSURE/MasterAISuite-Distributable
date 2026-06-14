# PAY_FLOW_PARAM_VALUES

Table captures the flow parameter values

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowparamvalues-29899.html#payflowparamvalues-29899](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowparamvalues-29899.html#payflowparamvalues-29899)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_PARAM_VALUES_PK | FLOW_PARAM_VAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_PARAM_VAL_ID | NUMBER |  | 18 | Yes | FLOW_PARAM_VAL_ID |
| FLOW_PARAM_CMP_VALUES | CLOB |  |  |  | FLOW_PARAM_CMP_VALUES |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BASE_FLOW_PARAMETER_ID | NUMBER |  | 18 | Yes | BASE_FLOW_PARAMETER_ID |
| FLOW_INSTANCE_ID | NUMBER |  | 18 | Yes | FLOW_INSTANCE_ID |
| FLOW_PARAM_VALUE | VARCHAR2 | 2000 |  |  | FLOW_PARAM_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLOW_PARAM_VALUES_N1 | Non Unique | Default | BASE_FLOW_PARAMETER_ID |
| PAY_FLOW_PARAM_VALUES_N2 | Non Unique | Default | FLOW_INSTANCE_ID |
| PAY_FLOW_PARAM_VALUES_PK | Unique | Default | FLOW_PARAM_VAL_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
