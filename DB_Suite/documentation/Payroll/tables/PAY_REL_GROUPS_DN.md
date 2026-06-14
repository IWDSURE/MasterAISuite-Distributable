# PAY_REL_GROUPS_DN

Defines setup information for how payroll relationships behave within a legislation.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelgroupsdn-27827.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelgroupsdn-27827.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REL_GROUPS_DN_PK | RELATIONSHIP_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RELATIONSHIP_GROUP_ID | NUMBER |  | 18 | Yes | RELATIONSHIP_GROUP_ID |
| AC_TRIGGER_FLAG | VARCHAR2 | 1 |  |  | AC_TRIGGER_FLAG |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  | Yes | END_DATE |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | PAYROLL_RELATIONSHIP_ID |
| GROUP_TYPE | VARCHAR2 | 30 |  | Yes | GROUP_TYPE |
| TERM_ID | NUMBER |  | 18 | Yes | TERM_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| PARENT_REL_GROUP_ID | NUMBER |  | 18 |  | PARENT_REL_GROUP_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 | Yes | LEGAL_EMPLOYER_ID |
| ASSIGNMENT_NUMBER | VARCHAR2 | 30 |  |  | ASSIGNMENT_NUMBER |
| TAX_REPORTING_UNIT_ID | NUMBER |  | 18 |  | TAX_REPORTING_UNIT_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REL_GROUPS_DN_N1 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID |
| PAY_REL_GROUPS_DN_N2 | Non Unique | Default | ASSIGNMENT_NUMBER |
| PAY_REL_GROUPS_DN_N3 | Non Unique | Default | ASSIGNMENT_ID |
| PAY_REL_GROUPS_DN_N4 | Non Unique | Default | UPPER("ASSIGNMENT_NUMBER") |
| PAY_REL_GROUPS_DN_N5 | Non Unique | Default | TERM_ID |
| PAY_REL_GROUPS_DN_N6 | Non Unique | Default | PARENT_REL_GROUP_ID |
| PAY_REL_GROUPS_DN_PK | Unique | Default | RELATIONSHIP_GROUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
