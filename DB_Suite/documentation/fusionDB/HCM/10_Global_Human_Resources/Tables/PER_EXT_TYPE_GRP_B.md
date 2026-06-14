# PER_EXT_TYPE_GRP_B

Table to seed parent Extract Types to consolidate the existing Extract Types.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexttypegrpb-23724.html#perexttypegrpb-23724](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexttypegrpb-23724.html#perexttypegrpb-23724)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_TYPE_GRP_B_PK | EXT_TYPE_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| EXT_TYPE_GRP_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |  |
| EXT_TYPE_GRP_CODE | VARCHAR2 | 30 |  | Yes | EXT_TYPE_GRP_CODE |  |
| ALLOW_USER_CREATION | VARCHAR2 | 1 |  |  | ALLOW_USER_CREATION |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
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
| PER_EXT_TYPE_GRP_B_PK | Unique | FUSION_TS_TX_DATA | EXT_TYPE_GRP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
