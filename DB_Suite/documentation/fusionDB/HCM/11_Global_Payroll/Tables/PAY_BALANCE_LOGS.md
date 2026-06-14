# PAY_BALANCE_LOGS

This table contains data returned by the mechanism for monitoring how a balance value was retrieved, such as from the latest balance, or the run balance or by calling the route.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancelogs-29413.html#paybalancelogs-29413](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancelogs-29413.html#paybalancelogs-29413)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BALANCE_LOGS_PK | SESSION_ID, SEQUENCE_NUM |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SESSION_ID | NUMBER |  | 18 | Yes | SESSION_ID |
| SEQUENCE_NUM | NUMBER |  | 18 | Yes | SEQUENCE_NUM |
| DATE_MONITORED | DATE |  |  | Yes | DATE_MONITORED |
| MONITOR_TYPE | VARCHAR2 | 30 |  | Yes | MONITOR_TYPE |
| MODULE_NAME | VARCHAR2 | 80 |  |  | MODULE_NAME |
| DEFINED_BALANCE_ID | NUMBER |  | 18 |  | Foreign key to PAY_DEFINED_BALANCES. |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_REL_ACTION_ID |
| SHORT_MESSAGE | VARCHAR2 | 240 |  |  | SHORT_MESSAGE |
| CONTEXT_STACK | CLOB |  |  |  | CONTEXT_STACK |
| SQL_TEXT | CLOB |  |  |  | SQL_TEXT |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BALANCE_LOGS_PK | Unique | Default | SESSION_ID, SEQUENCE_NUM |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
