# PAY_TEMP_OBJECT_ACTIONS

This table contains temporary actions that are only required while a process is in progress.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytempobjectactions-14490.html#paytempobjectactions-14490](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytempobjectactions-14490.html#paytempobjectactions-14490)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TEMP_OBJECT_ACTIONS_PK | TEMP_OBJECT_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMP_OBJECT_ACTION_ID | NUMBER |  | 18 | Yes | TEMP_OBJECT_ACTION_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | Foreign key to the Payroll Relationships table |
| OBJECT_ID | NUMBER |  | 18 | Yes | Foreign Key to a database object defined by the Object Type |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Indicates the type of object that the object id is pointing to |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to the PAY_PAYROLL_ACTION Table |
| ACTION_STATUS | VARCHAR2 | 1 |  | Yes | Valid statuses for an object action. |
| CHUNK_NUMBER | NUMBER |  | 18 | Yes | Number used to group events into chunks for parallelization. |
| ACTION_SEQUENCE | NUMBER |  | 18 | Yes | Absolute sequence number to determine physical order of events. |
| PARENT_OBJECT_ID | VARCHAR2 | 2000 |  |  | PARENT_OBJECT_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TEMP_OBJECT_ACTIONS_N1 | Non Unique | Default | OBJECT_ID |
| PAY_TEMP_OBJECT_ACTIONS_N2 | Non Unique | Default | PAYROLL_ACTION_ID, CHUNK_NUMBER |
| PAY_TEMP_OBJECT_ACTIONS_N3 | Non Unique | Default | PARENT_OBJECT_ID, PAYROLL_ACTION_ID |
| PAY_TEMP_OBJECT_ACTIONS_PK | Unique | Default | TEMP_OBJECT_ACTION_ID |
| PAY_TEMP_OBJECT_ACTIONS_N4 | Non Unique | Default | PAYROLL_ACTION_ID, ACTION_STATUS |
| PAY_TEMP_OBJECT_ACTIONS_N5 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, PAYROLL_ACTION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
