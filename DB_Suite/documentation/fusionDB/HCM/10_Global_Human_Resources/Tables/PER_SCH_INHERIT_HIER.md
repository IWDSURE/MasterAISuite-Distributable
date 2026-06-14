# PER_SCH_INHERIT_HIER

THis table hols the hierarchy order and sequence of  levels based on which Schedule has to be retrieved

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perschinherithier-20408.html#perschinherithier-20408](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perschinherithier-20408.html#perschinherithier-20408)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SCH_INHERIT_HIER_PK | INHERIT_LEVEL |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INHERIT_LEVEL | VARCHAR2 | 30 |  | Yes | INHERIT_LEVEL |
| IN_HIER | VARCHAR2 | 1 |  | Yes | IN_HIER |
| HIER_SEQ | NUMBER |  |  |  | HIER_SEQ |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SCH_INHERIT_HIER_PK | Unique | Default | INHERIT_LEVEL, ORA_SEED_SET1 |
| PER_SCH_INHERIT_HIER_PK1 | Unique | Default | INHERIT_LEVEL, ORA_SEED_SET2 |
| PER_SCH_INHERIT_HIER_U1 | Unique | Default | HIER_SEQ, ORA_SEED_SET1 |
| PER_SCH_INHERIT_HIER_U11 | Unique | Default | HIER_SEQ, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
