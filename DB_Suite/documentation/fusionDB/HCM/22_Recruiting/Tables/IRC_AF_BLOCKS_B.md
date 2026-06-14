# IRC_AF_BLOCKS_B

Stores all the Blocks that can be used in Apply Flow.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafblocksb-20105.html#ircafblocksb-20105](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafblocksb-20105.html#ircafblocksb-20105)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AF_BLOCKS_B_PK | BLOCK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BLOCK_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BLOCK_CODE | VARCHAR2 | 30 |  | Yes | Unique code for the block. Required value. |
| BLOCK_USAGE_CODE | VARCHAR2 | 256 |  | Yes | Stores the Block usage as lookup code. The corresponding lookup type is ORA_IRC_BLOCK_USAGE. |
| BLOCK_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the Block usage as lookup code. The corresponding lookup type is ORA_IRC_BLOCK_TYPE. |
| PROFILE_CONTENT_TYPE_ID | NUMBER |  | 18 |  | Stores the content type for profile type Blocks. Foreign key to HRT_CONTENT_TYPES_B table. |
| REUSABLE_FLAG | VARCHAR2 | 1 |  |  | Stores whether the Block can be reused in the Apply Flow Version multiple times. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AF_BLOCKS_B_PK | Unique | FUSION_TS_SEED | BLOCK_ID, ORA_SEED_SET1 |
| IRC_AF_BLOCKS_B_PK1 | Unique | FUSION_TS_SEED | BLOCK_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
