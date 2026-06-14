# PER_AOR_ASG_DN

This denormalized table holds the details of assignment which needs to be evaluated to calculate assignment representatives.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorasgdn-8673.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorasgdn-8673.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_AOR_ASG_DN_PK | ASSIGNMENT_ID |

## Columns

| Name | Datatype | Precision | Not-null | Comments |
|---|---|---|---|---|
| ASSIGNMENT_ID | NUMBER | 18 | Yes | This is a system generated primary key. Surrogate key. |
| ASG_ROWID | ROWID |  |  | RowId in the table |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_AOR_ASG_DN_PK | Unique | Default | ASSIGNMENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
