# PAY_OBJECT_GROUP_AMENDS

This table contains the revised definition of what to include or exclude from the default definition group based on the members generated from the fast formula for the group. For example, the default definition might include all employees in a certain employment level, and be revised to include three additional employees who are not in that employment level but should be included for reporting.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroupamends-8371.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroupamends-8371.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_OBJECT_GROUP_AMENDS_PK | OBJECT_GROUP_AMEND_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_GROUP_AMEND_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_AMEND_ID |
| OBJECT_GROUP_LEVEL_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_LEVEL_ID |
| OBJECT_GROUP_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_ID |
| OBJECT_ID | NUMBER |  | 18 | Yes | OBJECT_ID |
| INCLUDE_OR_EXCLUDE | VARCHAR2 | 30 |  | Yes | INCLUDE_OR_EXCLUDE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_OBJECT_GROUP_AMENDS_N1 | Non Unique | Default | OBJECT_GROUP_ID, OBJECT_ID, OBJECT_GROUP_LEVEL_ID, INCLUDE_OR_EXCLUDE |
| PAY_OBJECT_GROUP_AMENDS_PK | Unique | Default | OBJECT_GROUP_AMEND_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
