# PAY_ELEMENT_ENTRY_VALUES_F

This table contains the actual values entered for a specific element entry. For example, the overtime element may have an input value of hours worked. The number of hours worked by an employee in a fixed period is the entry value for that period.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelemententryvaluesf-30139.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelemententryvaluesf-30139.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_ENTRY_VALUES_F_PK | ELEMENT_ENTRY_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_ENTRY_VALUE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES. |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ELEMENT_ENTRIES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTRY_USAGE_ID | NUMBER |  | 18 |  | foreign key which stores the primary key of table pay_entry_usages. |
| SCREEN_ENTRY_VALUE | VARCHAR2 | 60 |  |  | Actual element entry value stored against input value id. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELEMENT_ENTRY_VALUES_F_N1 | Non Unique | Default | INPUT_VALUE_ID |
| PAY_ELEMENT_ENTRY_VALUES_F_N2 | Non Unique | Default | ENTRY_USAGE_ID |
| PAY_ELEMENT_ENTRY_VALUES_F_N50 | Non Unique | Default | ELEMENT_ENTRY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, SCREEN_ENTRY_VALUE |
| PAY_ELEMENT_ENTRY_VALUES_F_PK | Unique | Default | ELEMENT_ENTRY_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
