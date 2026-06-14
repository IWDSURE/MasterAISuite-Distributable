# IRC_GEO_LEVEL_MAPPINGS

This table is used to maintain Geography level mappings for each country . This is a 3 level mapping table where for each country a mapping entry is defined to refer a colum name in HZ_GEOGRAPHIES table for level2 and level3 values.

The main purpose if having a 3 level geo mapping table is while location indexing, the FQN gets built only on 3 levels like "City, State,Country".

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeolevelmappings-5176.html#ircgeolevelmappings-5176](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeolevelmappings-5176.html#ircgeolevelmappings-5176)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GEO_LEVEL_MAPPINGS_PK | GEO_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEO_MAPPING_ID | NUMBER |  | 18 | Yes | Primary Key - Sequence generated key. Fusion Global sequence generator is used to generate the key at run-time. |
| COUNTRY_CODE | VARCHAR2 | 30 |  |  | Country code of the GEOGRAPHY_ID. This columns is created for readability purpose. |
| GEO_LEVEL2_COLUMN_NAME | VARCHAR2 | 60 |  |  | This tells what column name should be used for LEVEL2 data. The value for this column name tells what column need to be referred in Hz_GEOGRAPHIES table to fetch LEVEL2 data . |
| GEO_LEVEL3_COLUMN_NAME | VARCHAR2 | 60 |  |  | This tells what column name should be used for LEVEL3 data. The value for this column name tells what column need to be referred in Hz_GEOGRAPHIES table to fetch LEVEL2 data . |
| ACTIVE_FLAG | VARCHAR2 | 1 |  | Yes | Flag to mark when a country is active. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Used for Seed Data soft delete purpose. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GEO_LEVEL_MAPPINGS_N1 | Non Unique | FUSION_TS_SEED | COUNTRY_CODE |
| IRC_GEO_LEVEL_MAPPINGS_U1 | Unique | FUSION_TS_SEED | GEO_MAPPING_ID, ORA_SEED_SET1 |
| IRC_GEO_LEVEL_MAPPINGS_U11 | Unique | FUSION_TS_SEED | GEO_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
