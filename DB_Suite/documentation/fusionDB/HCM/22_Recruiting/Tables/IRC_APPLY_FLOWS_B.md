# IRC_APPLY_FLOWS_B

Base table for Apply Flow Details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircapplyflowsb-15440.html#ircapplyflowsb-15440](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircapplyflowsb-15440.html#ircapplyflowsb-15440)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_APPLY_FLOWS_B_PK | APPLY_FLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| APPLY_FLOW_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |  |
| AF_CODE | VARCHAR2 | 30 |  | Yes | Unique code for the Apply Flow. |  |
| AF_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Apply Flow Type based on lookup. The corresponding lookup type is ORA_IRC_APPLY_FLOW_TYPE. |  |
| AF_STATUS_CODE | VARCHAR2 | 30 |  |  | Indicates the status of the apply flow version based on lookup.  The corresponding lookup type is ORA_IRC_AF_STATUS. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_APPLY_FLOWS_B_PK | Unique | Default | APPLY_FLOW_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
