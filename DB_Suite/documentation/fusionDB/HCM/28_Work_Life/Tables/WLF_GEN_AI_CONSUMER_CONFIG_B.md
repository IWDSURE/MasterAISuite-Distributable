# WLF_GEN_AI_CONSUMER_CONFIG_B

This table stores the "GEN AI" consumer configuration details.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgenaiconsumerconfigb-13278.html#wlfgenaiconsumerconfigb-13278](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgenaiconsumerconfigb-13278.html#wlfgenaiconsumerconfigb-13278)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GEN_AI_CONSUMER_CONFIG_PK | GEN_AI_CONSUMER_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEN_AI_CONSUMER_CONFIG_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Specifies the Object Type for which the configuration applies |
| CONSUMER_IMPL_CLASS | VARCHAR2 | 1024 |  | Yes | Specifies  GenAIConsumer Implementation class |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Specifies if the seed data row is enabled or not |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GEN_AI_CONSUMER_CONFIG_PK1 | Unique | Default | GEN_AI_CONSUMER_CONFIG_ID, ORA_SEED_SET1 |
| WLF_GEN_AI_CONSUMER_CONFIG_PK2 | Unique | Default | GEN_AI_CONSUMER_CONFIG_ID, ORA_SEED_SET2 |
| WLF_GEN_AI_CONSUMER_CONFIG_U1 | Unique | Default | OBJECT_TYPE, ORA_SEED_SET1 |
| WLF_GEN_AI_CONSUMER_CONFIG_U2 | Unique | Default | OBJECT_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
