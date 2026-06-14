# PAY_BALANCE_VALIDATION

This table contains validity information of each run level balance for the legislative data group.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancevalidation-14678.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancevalidation-14678.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BALANCE_VALIDATION_PK | BALANCE_VALIDATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BALANCE_VALIDATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| DEFINED_BALANCE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_DEFINED_BALANCES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| RUN_BALANCE_STATUS | VARCHAR2 | 1 |  | Yes | Status of the Run Balance population. |
| BALANCE_LOAD_DATE | DATE |  |  |  | The Date from which run balances where loaded for this Balance |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BALANCE_VALIDATION_PK | Unique | Default | BALANCE_VALIDATION_ID |
| PAY_BALANCE_VALIDATION_UK1 | Unique | Default | DEFINED_BALANCE_ID, LEGISLATIVE_DATA_GROUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
