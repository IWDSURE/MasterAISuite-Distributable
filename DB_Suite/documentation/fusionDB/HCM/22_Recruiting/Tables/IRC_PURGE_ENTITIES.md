# IRC_PURGE_ENTITIES

The table is use to store recruiting purging job configuration information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpurgeentities-23701.html#ircpurgeentities-23701](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpurgeentities-23701.html#ircpurgeentities-23701)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PURGE_ENTITIES_PK | ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTITY_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated |
| ENTITY_NAME | VARCHAR2 | 64 |  | Yes | This stores entity name to be purged. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This is used to indicate whether entity is enabled for purge. Y means purge enabled and N means purge disabled. |
| DROP_PARTITION_FLAG | VARCHAR2 | 1 |  | Yes | This is used to indicate whether entity is enabled for drop partition. Y means drop partition enabled and N means drop partition disabled. |
| ACTIVE_DAYS | NUMBER |  | 6 | Yes | Number of active days kept in the entity. |
| BATCH_SIZE | NUMBER |  | 10 | Yes | The number of rows to be purged in each batch for each entity type. |
| EXECUTION_ORDER | NUMBER |  | 3 | Yes | The priority order of the entity to be purged. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PURGE_ENTITIES_PK | Unique | FUSION_TS_SEED | ENTITY_ID, ORA_SEED_SET1 |
| IRC_PURGE_ENTITIES_PK1 | Unique | FUSION_TS_SEED | ENTITY_ID, ORA_SEED_SET2 |
| IRC_PURGE_ENTITIES_U1 | Unique | FUSION_TS_SEED | ENTITY_NAME, ORA_SEED_SET1 |
| IRC_PURGE_ENTITIES_U11 | Unique | FUSION_TS_SEED | ENTITY_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
