# PAY_BAL_ADJ_LINE_ACTIONS

This table contains the actions for a balance adjustment.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjlineactions-14194.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjlineactions-14194.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_ADJ_LINE_ACTIONS_PK | PAYROLL_REL_ACTION_ID |

## Columns

| Name | Datatype | Precision | Not-null | Comments |
|---|---|---|---|---|
| PAYROLL_REL_ACTION_ID | NUMBER | 18 | Yes | PAYROLL_REL_ACTION_ID |
| BAL_ADJ_LINE_ID | NUMBER | 18 | Yes | BAL_ADJ_LINE_ID |
| RETRO_COMPONENT_ID | NUMBER | 18 |  | RETRO_COMPONENT_ID |
| ENTERPRISE_ID | NUMBER | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_ADJ_LINE_ACTIONS_N1 | Non Unique | Default | BAL_ADJ_LINE_ID |
| PAY_BAL_ADJ_LINE_ACTIONS_PK | Unique | Default | PAYROLL_REL_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
