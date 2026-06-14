# PER_ACTION_TYPES_B

This tables stores Action Types. Action Types are the predefined business processes seeded by Oracle and not customer extensible

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractiontypesb-24007.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractiontypesb-24007.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACTION_TYPES_B_PK | ACTION_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_TYPE_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Uniquely identifies an Action Type |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CHANGE_ASG_VISIBLE_FLAG | VARCHAR2 | 30 |  |  | This flag determines if  a specific action is visible to change assignment flow. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| DEFAULT_ASG_STATUS | VARCHAR2 | 30 |  |  | DEFAULT_ASG_STATUS |
| SUPPORT_ASG_STATUS_DFLT | VARCHAR2 | 30 |  |  | SUPPORT_ASG_STATUS_DFLT |
| INCLUDE_CLE_FUT | VARCHAR2 | 3 |  |  | Include in Change Legal Employer Future updates copy or not. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ACTION_TYPES_B_N1 | Non Unique | Default | BUSINESS_GROUP_ID, ACTION_TYPE_CODE |
| PER_ACTION_TYPES_B_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ACTION_TYPES_B_N20 | Non Unique | Default | SGUID |
| PER_ACTION_TYPES_B_PK | Unique | Default | ACTION_TYPE_ID, ORA_SEED_SET1 |
| PER_ACTION_TYPES_B_PK1 | Unique | Default | ACTION_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
