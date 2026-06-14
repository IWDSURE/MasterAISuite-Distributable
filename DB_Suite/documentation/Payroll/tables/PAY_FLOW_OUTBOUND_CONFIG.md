# PAY_FLOW_OUTBOUND_CONFIG

This table is used for storing configurations to notify external systems.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowoutboundconfig-9681.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowoutboundconfig-9681.html)

## Primary Key

| Name | Columns |
|------|----------|
| pay_flow_outbound_config_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | CONFIG_ID |
| CONFIG_NAME | VARCHAR2 | 30 |  |  | CONFIG_NAME |
| PROPERTY_NAME | VARCHAR2 | 50 |  |  | PROPERTY_NAME |
| PROPERTY_VALUE | VARCHAR2 | 2500 |  |  | PROPERTY_VALUE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| pay_flow_outbound_config_U1 | Unique | Default | CONFIG_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
