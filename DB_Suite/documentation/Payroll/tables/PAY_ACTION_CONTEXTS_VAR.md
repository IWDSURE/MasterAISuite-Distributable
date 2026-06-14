# PAY_ACTION_CONTEXTS_VAR

This child table of PAY_ACTION_CONTEXTS contains context values of non-global and user defined contexts that were processed in payroll relationship actions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioncontextsvar-12235.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioncontextsvar-12235.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_CONTEXTS_VAR_PK | ACTION_CONTEXT_ID, CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_CONTEXT_ID | NUMBER |  | 18 | Yes | ACTION_CONTEXT_ID |
| CONTEXT_ID | NUMBER |  | 18 | Yes | CONTEXT_ID |
| VALUE | VARCHAR2 | 60 |  | Yes | VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ACTION_CONTEXTS_VAR_PK | Unique | Default | ACTION_CONTEXT_ID, CONTEXT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
