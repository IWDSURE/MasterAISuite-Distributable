# PER_EXT_BLOCK_LINKS

Links to capture block relationships.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextblocklinks-19954.html#perextblocklinks-19954](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextblocklinks-19954.html#perextblocklinks-19954)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_BLOCK_LINKS_PK | EXT_BLOCK_LINK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_BLOCK_LINK_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PARENT_BLOCK_ID | NUMBER |  | 18 |  | Block Id of the parent Block |
| REPORT_BLOCK_ID | NUMBER |  | 18 |  | Block Id of the child Block |
| PARENT_BLOCK_DBI_ID | NUMBER |  | 18 |  | Database item id of the parent block |
| BLOCK_DBI_ID | NUMBER |  | 18 |  | Database item id of the child block |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EXT_BLOCK_LINKS_FK1 | Non Unique | Default | REPORT_BLOCK_ID |
| PER_EXT_BLOCK_LINKS_N1 | Non Unique | Default | PARENT_BLOCK_ID |
| PER_EXT_BLOCK_LINKS_N20 | Non Unique | Default | SGUID |
| PER_EXT_BLOCK_LINKS_PK | Unique | Default | EXT_BLOCK_LINK_ID, ORA_SEED_SET1 |
| PER_EXT_BLOCK_LINKS_PK1 | Unique | Default | EXT_BLOCK_LINK_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
