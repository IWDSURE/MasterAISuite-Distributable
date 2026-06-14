# PAY_ELE_PAY_FREQ_RULES

This table contains the periods in which an element should be processed. For example, if a deduction should process in periods 2 and 3 of a month for employees on a weekly payroll, it would record periods 2 and 3 and ensure 1 and 4 are not processed.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelepayfreqrules-13693.html#payelepayfreqrules-13693](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelepayfreqrules-13693.html#payelepayfreqrules-13693)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELE_PAY_FREQ_RULES_PK | ELE_PAYROLL_FREQ_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELE_PAYROLL_FREQ_RULE_ID | NUMBER |  | 18 | Yes | ELE_PAYROLL_FREQ_RULE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | ELEMENT_TYPE_ID |
| PAYROLL_ID | NUMBER |  | 18 | Yes | PAYROLL_ID |
| START_DATE | DATE |  |  | Yes | START_DATE |
| RESET_PERIOD_TYPE | VARCHAR2 | 30 |  |  | RESET_PERIOD_TYPE |
| RESET_NO_OF_PERIODS | NUMBER |  | 9 |  | RESET_NO_OF_PERIODS |
| RULE_DATE_CODE | VARCHAR2 | 30 |  |  | RULE_DATE_CODE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ELE_PAY_FREQ_RULES_FK1 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PAY_ELE_PAY_FREQ_RULES_FK4 | Non Unique | Default | RESET_PERIOD_TYPE |
| PAY_ELE_PAY_FREQ_RULES_N3 | Non Unique | Default | PAYROLL_ID |
| PAY_ELE_PAY_FREQ_RULES_PK | Unique | Default | ELE_PAYROLL_FREQ_RULE_ID |
| PAY_ELE_PAY_FREQ_RULES_UK3 | Unique | Default | ELEMENT_TYPE_ID, PAYROLL_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
