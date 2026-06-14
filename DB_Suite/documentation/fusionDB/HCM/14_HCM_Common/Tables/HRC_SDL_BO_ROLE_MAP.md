# HRC_SDL_BO_ROLE_MAP

This table is used to store Business Object and Role Mappings. This mapping is used to apply data security in HSDL at Business Object level.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlborolemap-23956.html#hrcsdlborolemap-23956](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlborolemap-23956.html#hrcsdlborolemap-23956)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_BO_ROLE_MAP_PK | ROLE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_MAPPING_ID | NUMBER |  | 18 | Yes | ROLE_MAPPING_ID |
| ROLE_ID | NUMBER |  | 18 | Yes | ROLE_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| EXTRA_INFO | VARCHAR2 | 1000 |  |  | EXTRA_INFO |
| ERROR_INFORMATION | VARCHAR2 | 4000 |  |  | ERROR_INFORMATION |
| GRANT_GEN_STATUS | VARCHAR2 | 4 |  |  | GRANT_GEN_STATUS |
| GRANT_GEN_DETAILS | VARCHAR2 | 4000 |  |  | GRANT_GEN_DETAILS |
| ACTIVE_STATUS | VARCHAR2 | 4 |  |  | ACTIVE_STATUS |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PRODUCT_AREA | VARCHAR2 | 100 |  |  | PRODUCT_AREA |
| ALL_BUS_OBJ_ACCESS | VARCHAR2 | 4 |  |  | ALL_BUS_OBJ_ACCESS |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| EXCLUDE_BUSINESS_OBJECT | VARCHAR2 | 4000 |  |  | List of business object identifiers excluded from the product area |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_BO_ROLE_MAP_N1 | Non Unique | Default | ROLE_ID, BUSINESS_OBJECT_ID |
| HRC_SDL_BO_ROLE_MAP_U1 | Unique | Default | ROLE_MAPPING_ID, ORA_SEED_SET1 |
| HRC_SDL_BO_ROLE_MAP_U11 | Unique | Default | ROLE_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
