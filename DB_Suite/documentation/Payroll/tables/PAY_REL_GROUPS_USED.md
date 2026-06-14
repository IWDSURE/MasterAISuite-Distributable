# PAY_REL_GROUPS_USED

This table contains details of the components of a person's configuration that were processed in a payroll run.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelgroupsused-29521.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelgroupsused-29521.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REL_GROUPS_USED_PK | PAYROLL_REL_ACTION_ID, RELATIONSHIP_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| RELATIONSHIP_GROUP_ID | NUMBER |  | 18 | Yes | RELATIONSHIP_GROUP_ID |
| STATUS | VARCHAR2 | 5 |  |  | STATUS |
| ORIGINAL_STATUS | VARCHAR2 | 5 |  |  | ORIGINAL_STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REL_GROUPS_USED_N1 | Non Unique | Default | RELATIONSHIP_GROUP_ID, PAYROLL_REL_ACTION_ID |
| PAY_REL_GROUPS_USED_PK | Unique | Default | PAYROLL_REL_ACTION_ID, RELATIONSHIP_GROUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
