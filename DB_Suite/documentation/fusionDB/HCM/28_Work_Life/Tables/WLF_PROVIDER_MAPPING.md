# WLF_PROVIDER_MAPPING

Table to store content type, learning level and business driver mappings

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfprovidermapping-3136.html#wlfprovidermapping-3136](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfprovidermapping-3136.html#wlfprovidermapping-3136)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PROVIDER_MAPPING_PK | PROVIDER_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROVIDER_MAPPING_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_TYPE | VARCHAR2 | 30 |  | Yes | This column stores the provider type information |
| MAPPING_TYPE | VARCHAR2 | 30 |  | Yes | This column stores the mapping type information |
| PROVIDER_CONTENT_CODE | VARCHAR2 | 30 |  | Yes | This column stores the provider content code |
| PROVIDER_CONTENT_VALUE | VARCHAR2 | 80 |  | Yes | This column stores the provider content meaning |
| TARGET_CODE | VARCHAR2 | 30 |  | Yes | This column stores the target code |
| MUTABLE_FLAG | VARCHAR2 | 1 |  | Yes | Indicates if target code is updatable |
| RULE | VARCHAR2 | 4000 |  |  | Seeded values for updating target code |
| DEFAULT_TARGET_CODE | VARCHAR2 | 30 |  |  | Indicates default seeded target code |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| COMPLETION_RULE | VARCHAR2 | 32 |  |  | This column holds the value for Completion Rule |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROVIDER_MAPPING_N1 | Non Unique | Default | PROVIDER_TYPE |
| WLF_PROVIDER_MAPPING_N2 | Non Unique | Default | MAPPING_TYPE |
| WLF_PROVIDER_MAPPING_PK | Unique | Default | PROVIDER_MAPPING_ID, ORA_SEED_SET1 |
| WLF_PROVIDER_MAPPING_PK1 | Unique | Default | PROVIDER_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
