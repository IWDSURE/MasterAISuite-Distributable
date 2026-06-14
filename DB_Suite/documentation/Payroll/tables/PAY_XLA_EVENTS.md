# PAY_XLA_EVENTS

This table contains the cost details and values of a worker's payroll results.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payxlaevents-13517.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payxlaevents-13517.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_XLA_EVENTS_PK | EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ID | NUMBER |  | 18 | Yes | EVENT_ID |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| ACCOUNTING_DATE | DATE |  |  |  | ACCOUNTING_DATE |
| EVENT_STATUS | VARCHAR2 | 1 |  | Yes | EVENT_STATUS |
| PAYROLL_ID | NUMBER |  | 18 | Yes | PAYROLL_ID |
| COST_ACTION_ID | NUMBER |  | 18 |  | COST_ACTION_ID |
| RUN_ACTION_ID | NUMBER |  | 18 |  | RUN_ACTION_ID |
| COST_TYPE | VARCHAR2 | 30 |  |  | COST_TYPE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| REVERSAL_FLAG | VARCHAR2 | 1 |  |  | REVERSAL_FLAG |
| TIME_PERIOD_ID | NUMBER |  | 18 |  | TIME_PERIOD_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_XLA_EVENTS_FK1 | Non Unique | Default | PAYROLL_REL_ACTION_ID, ACCOUNTING_DATE |
| PAY_XLA_EVENTS_N2 | Non Unique | Default | COST_ACTION_ID |
| PAY_XLA_EVENTS_PK | Unique | Default | EVENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
