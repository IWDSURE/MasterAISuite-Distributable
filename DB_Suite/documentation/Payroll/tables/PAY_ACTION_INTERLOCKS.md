# PAY_ACTION_INTERLOCKS

This table contains the assignment action locking rules to control rollback processing.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioninterlocks-22861.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioninterlocks-22861.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_INTERLOCKS_PK | LOCKING_ACTION_ID, LOCKED_ACTION_ID |

## Columns

| Name | Datatype | Precision | Not-null | Comments |
|---|---|---|---|---|
| LOCKING_ACTION_ID | NUMBER | 18 | Yes | Foreign key to PAY_ASSIGNMENT_ACTIONS. |
| LOCKED_ACTION_ID | NUMBER | 18 | Yes | Foreign key to PAY_ASSIGNMENT_ACTIONS. |
| ENTERPRISE_ID | NUMBER | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ACTION_INTERLOCKS_FK2 | Non Unique | Default | LOCKED_ACTION_ID |
| PAY_ACTION_INTERLOCKS_PK | Unique | Default | LOCKING_ACTION_ID, LOCKED_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
