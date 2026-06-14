# PAY_MASS_GLB_TRANSFER_CONFIG

Table is to store the payroll config options in Mass Global Transfer

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymassglbtransferconfig-31014.html#paymassglbtransferconfig-31014](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymassglbtransferconfig-31014.html#paymassglbtransferconfig-31014)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_MASS_GLB_TRANSFER_CON_PK | MASS_GLB_TRANSFER_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_GLB_TRANSFER_CONFIG_ID | NUMBER |  | 18 | Yes | MASS_GLB_TRANSFER_CONFIG_ID |
| MASS_ACTION_HEADER_ID | NUMBER |  | 18 | Yes | MASS_ACTION_HEADER_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| TAX_REPORTING_UNIT_ID | NUMBER |  | 18 |  | TAX_REPORTING_UNIT_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COPY_PPM_FLAG | VARCHAR2 | 1 |  |  | Possible Values Y/N |
| COPY_COSTING_FLAG | VARCHAR2 | 1 |  |  | Possible Values Y/N |
| COPY_EE_FLAG | VARCHAR2 | 1 |  |  | Possible Values Y/N |
| ELEMENT_GROUP_ID | NUMBER |  | 18 |  | ELEMENT_GROUP |
| COPY_CIR_FLAG | VARCHAR2 | 1 |  |  | Possible value Y/N |
| CIR_GROUP_ID | NUMBER |  | 18 |  | CIR_GROUP |
| MOVE_NON_REC_FLAG | VARCHAR2 | 1 |  |  | Possible Values Y/N |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| TIME_CARD_REQ_FOR_ASSIGNMENT | VARCHAR2 | 1 |  |  | TIME_CARD_REQ_ASSIGNMENT |
| OVERTIME_PERIOD_FOR_ASSIGNMENT | NUMBER |  | 18 |  | OVERTIME_PERIOD_FOR_ASSIGNMENT |
| TIME_CARD_REQ_FOR_PAYROLL | VARCHAR2 | 1 |  |  | TIME_CARD_REQ_PAYROLL |
| OVERTIME_PERIOD_FOR_PAYROLL | NUMBER |  | 18 |  | OVERTIME_PERIOD_FOR_PAYROLL |
| COPYBALANCE | VARCHAR2 | 1 |  |  | COPYBALANCE |
| BALANCE_GROUP_ID | NUMBER |  | 18 |  | BALANCE_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_MASS_GLB_TRANSFER_CON_PK | Unique | FUSION_TS_TX_DATA | MASS_GLB_TRANSFER_CONFIG_ID |
| PAY_MASS_GLB_TRANS_CONFIG_N1 | Non Unique | Default | MASS_ACTION_HEADER_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
