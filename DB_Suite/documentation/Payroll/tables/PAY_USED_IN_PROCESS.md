# PAY_USED_IN_PROCESS

This table contains the object information used in the process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payusedinprocess-7245.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payusedinprocess-7245.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_USED_IN_PROCESS_PK | PAYROLL_REL_ACTION_ID, SOURCE_ID, SOURCE_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | SOURCE_TYPE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_USED_IN_PROCESS_PK | Unique | Default | PAYROLL_REL_ACTION_ID, SOURCE_ID, SOURCE_TYPE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
