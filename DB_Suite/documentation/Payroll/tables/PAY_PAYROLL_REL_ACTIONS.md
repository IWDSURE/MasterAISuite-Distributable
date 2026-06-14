# PAY_PAYROLL_REL_ACTIONS

This table contains details of the individuals processed in a payroll process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollrelactions-20415.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollrelactions-20415.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAYROLL_REL_ACTIONS_PK | PAYROLL_REL_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | PAYROLL_RELATIONSHIP_ID |
| ACTION_STATUS | VARCHAR2 | 1 |  | Yes | ACTION_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ACTION_SEQUENCE | NUMBER |  | 18 | Yes | ACTION_SEQUENCE |
| CHUNK_NUMBER | NUMBER |  | 18 | Yes | CHUNK_NUMBER |
| SOURCE_ACTION_ID | NUMBER |  | 18 |  | SOURCE_ACTION_ID |
| RUN_TYPE_ID | NUMBER |  | 18 |  | RUN_TYPE_ID |
| PRE_PAYMENT_ID | NUMBER |  | 18 |  | PRE_PAYMENT_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| SERIAL_NUMBER | VARCHAR2 | 30 |  |  | SERIAL_NUMBER |
| RETRO_COMPONENT_ID | NUMBER |  | 18 |  | RETRO_COMPONENT_ID |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| PARENT_OBJECT_ID | VARCHAR2 | 2000 |  |  | PARENT_OBJECT_ID |
| PROCESS_PATH | VARCHAR2 | 80 |  |  | COLUMN1 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PAYROLL_REL_ACTIONS_FK2 | Non Unique | Default | PRE_PAYMENT_ID |
| PAY_PAYROLL_REL_ACTIONS_N3 | Non Unique | Default | SOURCE_ACTION_ID |
| PAY_PAYROLL_REL_ACTIONS_N4 | Non Unique | Default | PAYROLL_ACTION_ID, ACTION_STATUS |
| PAY_PAYROLL_REL_ACTIONS_N50 | Non Unique | Default | PAYROLL_ACTION_ID, CHUNK_NUMBER |
| PAY_PAYROLL_REL_ACTIONS_N51 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, PAYROLL_ACTION_ID |
| PAY_PAYROLL_REL_ACTIONS_N52 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, ACTION_SEQUENCE, ACTION_STATUS |
| PAY_PAYROLL_REL_ACTIONS_PK | Unique | Default | PAYROLL_REL_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
