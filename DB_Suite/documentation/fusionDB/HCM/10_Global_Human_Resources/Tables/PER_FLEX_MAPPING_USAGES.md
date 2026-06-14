# PER_FLEX_MAPPING_USAGES

This table stores the usages for each flexfield mappings.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perflexmappingusages-4402.html#perflexmappingusages-4402](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perflexmappingusages-4402.html#perflexmappingusages-4402)

## Primary Key

| Name | Columns |
|------|----------|
| PER_FLEX_MAPPING_USAGES_F_PK | FLEX_MAPPING_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FLEX_MAPPING_USAGE_ID | NUMBER |  | 18 | Yes | This field uniquely identifies a mapping usage | Active |
| FLEX_SEGMENT_MAPPING_ID | NUMBER |  | 18 | Yes | This field uniquely identifies a mapping | Active |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This field specifies the id of legal employer | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This specifies the id for an enterprise | Active |
| POSITION_SYNC_ENABLED_FLAG | VARCHAR2 | 1 |  |  | This field specifies if position synchronization is enabled for the legal employer,enterprise or not | Active |
| POSITION_DEFAULT_ENABLED_FLAG | VARCHAR2 | 1 |  |  | This field specifies if position defaulting is enabled for the legal employer,enterprise or not | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_FLEX_MAPPING_USAGES_F_PK | Unique | FUSION_TS_TX_IDX | FLEX_MAPPING_USAGE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
