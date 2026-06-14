# PAY_TMPLT_RULE_VALUES

This is a transaction table used to store the rule values

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulevalues-7983.html#paytmpltrulevalues-7983](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulevalues-7983.html#paytmpltrulevalues-7983)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_RULE_VALUES_PK | RULE_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_VALUE_ID | NUMBER |  | 18 | Yes | RULE_VALUE_ID |
| BASE_RULE_VALUE_ID | NUMBER |  | 18 |  | BASE_RULE_VALUE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RULE_ID | NUMBER |  | 18 | Yes | RULE_ID |
| TEMPLATE_ID | NUMBER |  | 18 |  | TEMPLATE_ID |
| RULE_VALUE | VARCHAR2 | 200 |  |  | RULE_VALUE |
| BASE_RULE_VALUE | VARCHAR2 | 200 |  |  | BASE_RULE_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TMPLT_RULE_VALUES_PK | Unique | Default | RULE_VALUE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
