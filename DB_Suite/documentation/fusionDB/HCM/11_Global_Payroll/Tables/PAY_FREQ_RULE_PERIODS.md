# PAY_FREQ_RULE_PERIODS

This table, which is a child table of PAY_ELE_PAY_FREQ_RULES, contains the actual frequency rule for an element. If the element should process in periods 2 and 3 of a month for employees on a weekly payroll, there will be 2 rows in this table, one for period 2 and one for period 3.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payfreqruleperiods-13426.html#payfreqruleperiods-13426](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payfreqruleperiods-13426.html#payfreqruleperiods-13426)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FREQ_RULE_PERIODS_PK | FREQ_RULE_PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FREQ_RULE_PERIOD_ID | NUMBER |  | 18 | Yes | FREQ_RULE_PERIOD_ID |
| ELE_PAYROLL_FREQ_RULE_ID | NUMBER |  | 18 | Yes | ELE_PAYROLL_FREQ_RULE_ID |
| PERIOD_NO_IN_RESET_PERIOD | NUMBER |  | 9 | Yes | PERIOD_NO_IN_RESET_PERIOD |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FREQ_RULE_PERIODS_FK1 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PAY_FREQ_RULE_PERIODS_FK2 | Non Unique | Default | ELE_PAYROLL_FREQ_RULE_ID |
| PAY_FREQ_RULE_PERIODS_PK | Unique | Default | FREQ_RULE_PERIOD_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
