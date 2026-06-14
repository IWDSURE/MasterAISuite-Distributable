# PER_ASSIGNMENT_STATUS_TYPES

This table holds pre-defined and user defined status types (for Assignments or Sets of Employment/Placement Terms). Current seeded values will have to be revisited to ensure we remove obsolete values and incorporate Enterprise statuses.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentstatustypes-15618.html#perassignmentstatustypes-15618](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentstatustypes-15618.html#perassignmentstatustypes-15618)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASSIGNMENT_STATUS_TYP_PK | ASSIGNMENT_STATUS_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ASSIGNMENT_STATUS_TYPE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | The legislation to which the status type applies. | Active |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | Obsolete. | Active |
| DEFAULT_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether this is the default user status for the PER_SYSTEM_STATUS. | Active |
| PRIMARY_FLAG | VARCHAR2 | 30 |  |  | Obsolete. | Active |
| PAY_SYSTEM_STATUS | VARCHAR2 | 30 |  |  | Payroll status indicating whether the assignment is processed in payroll runs. | Active |
| PER_SYSTEM_STATUS | VARCHAR2 | 30 |  |  | HR status used extensively within the system to determine how the assignment is processed. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| START_DATE | DATE |  |  |  | Date status is active on. |  |
| END_DATE | DATE |  |  |  | If this is not null, then status is not active after this date. |  |
| ASSIGNMENT_STATUS_CODE | VARCHAR2 | 30 |  |  | Unique code representing the status. |  |
| ORIG_ASSIGN_STATUS_TYPE_ID | NUMBER |  | 18 |  | Link to seeded assignment status. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| COUNTRY | VARCHAR2 | 2000 |  |  | Possible Values ALL/NULL/Comma separated Legislationcode for multiple countries |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ASSIGNMENT_STATUS_TYPE_UK1 | Unique | Default | ASSIGNMENT_STATUS_CODE, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| PER_ASSIGNMENT_STATUS_TYP_N20 | Non Unique | Default | SGUID |
| PER_ASSIGNMENT_STATUS_TYP_PK | Unique | Default | ASSIGNMENT_STATUS_TYPE_ID, ORA_SEED_SET1 |
| PER_ASSIGNMENT_STATUS_TYP_PK1 | Unique | Default | ASSIGNMENT_STATUS_TYPE_ID, ORA_SEED_SET2 |
| PER_ASSIGNMENT_STATUS_TYP_UK11 | Unique | Default | ASSIGNMENT_STATUS_CODE, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
