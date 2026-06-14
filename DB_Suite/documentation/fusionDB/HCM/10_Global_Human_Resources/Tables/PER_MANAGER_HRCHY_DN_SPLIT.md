# PER_MANAGER_HRCHY_DN_SPLIT

This table is used internally to populate column flattened manager hierarchy view. This wont be exposed in the middle layer.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchydnsplit-30040.html#permanagerhrchydnsplit-30040](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchydnsplit-30040.html#permanagerhrchydnsplit-30040)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MANAGER_ID | NUMBER |  | 18 |  | Manager Identifier |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign Key to Per Assignments. Identifies the manager's assignment |
| SPLIT_START_DATE | DATE |  |  |  | Effective Start Date of when the manager hierarchy information got split |
| SPLIT_END_DATE | DATE |  |  |  | Effective End Date of when the manager hierarchy information got split |
| IMMEDIATE_REPORTEE_ASG_ID | NUMBER |  | 18 |  | Immediate Reportee Assignment ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_MANAGER_HRCHY_DN_SPLIT_N1 | Non Unique | Default | MANAGER_ASSIGNMENT_ID, SPLIT_START_DATE, SPLIT_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
