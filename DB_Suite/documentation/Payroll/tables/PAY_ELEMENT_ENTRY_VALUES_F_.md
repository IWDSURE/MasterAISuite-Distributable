# PAY_ELEMENT_ENTRY_VALUES_F_

This table contains the actual values entered for a specific element entry. For example, the overtime element may have an input value of hours worked. The number of hours worked by an employee in a fixed period is the entry value for that period.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelemententryvaluesf-26826.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelemententryvaluesf-26826.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_ENTRY_VALUES_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ELEMENT_ENTRY_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_ENTRY_VALUE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_INPUT_VALUES. |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_ENTRIES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTRY_USAGE_ID | NUMBER |  | 18 |  | ENTRY_USAGE_ID |
| SCREEN_ENTRY_VALUE | VARCHAR2 | 60 |  |  | Actual entry value. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELEMENT_ENTRY_VALUES_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ELEMENT_ENTRY_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_ELE_ENTRY_VALUES_FN1_ | Non Unique | Default | ELEMENT_ENTRY_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_ELE_ENTRY_VALUES_FN2_ | Non Unique | Default | ELEMENT_ENTRY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
