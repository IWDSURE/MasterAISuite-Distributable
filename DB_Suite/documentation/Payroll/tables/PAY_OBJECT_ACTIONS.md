# PAY_OBJECT_ACTIONS

This table contains detailed information for what was processed in some types of payroll actions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectactions-17358.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectactions-17358.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_OBJECT_ACTIONS_PK | OBJECT_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_ACTION_ID | NUMBER |  | 18 | Yes | OBJECT_ACTION_ID |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| OBJECT_ID | NUMBER |  | 18 | Yes | OBJECT_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | OBJECT_TYPE |
| CHUNK_NUMBER | NUMBER |  | 18 | Yes | CHUNK_NUMBER |
| ACTION_SEQUENCE | NUMBER |  | 18 | Yes | ACTION_SEQUENCE |
| ACTION_STATUS | VARCHAR2 | 1 |  | Yes | ACTION_STATUS |
| PARENT_OBJECT_ID | VARCHAR2 | 2000 |  |  | PARENT_OBJECT_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | Foreign key to the Payroll Relationships table |
| SERIAL_NUMBER | VARCHAR2 | 30 |  |  | SERIAL_NUMBER |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_OBJECT_ACTIONS_N1 | Non Unique | Default | PAYROLL_ACTION_ID, CHUNK_NUMBER |
| PAY_OBJECT_ACTIONS_N2 | Non Unique | Default | OBJECT_ID, OBJECT_TYPE |
| PAY_OBJECT_ACTIONS_N3 | Non Unique | Default | OBJECT_ID, PAYROLL_ACTION_ID |
| PAY_OBJECT_ACTIONS_N4 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, PAYROLL_ACTION_ID |
| PAY_OBJECT_ACTIONS_N5 | Non Unique | Default | PAYROLL_ACTION_ID, ACTION_STATUS |
| PAY_OBJECT_ACTIONS_N6 | Non Unique | Default | OBJECT_ID, ACTION_STATUS, OBJECT_ACTION_ID |
| PAY_OBJECT_ACTIONS_PK | Unique | Default | OBJECT_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
