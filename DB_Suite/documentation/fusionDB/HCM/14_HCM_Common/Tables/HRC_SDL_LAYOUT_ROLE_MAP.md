# HRC_SDL_LAYOUT_ROLE_MAP

This table is used to store Template and Role Mappings. This mapping is used to apply data security in HSDL at Template and Data Set levels.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdllayoutrolemap-21783.html#hrcsdllayoutrolemap-21783](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdllayoutrolemap-21783.html#hrcsdllayoutrolemap-21783)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_LAYOUT_ROLE_MAP_PK | ROLE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_MAPPING_ID | NUMBER |  | 18 | Yes | ROLE_MAPPING_ID |
| ROLE_ID | NUMBER |  | 18 | Yes | ROLE_ID |
| LAYOUT_ID | NUMBER |  | 18 | Yes | LAYOUT_ID |
| CREATE_DATA_SET | VARCHAR2 | 4 |  | Yes | CREATE_DATA_SET |
| SAVE_DATA_SET | VARCHAR2 | 4 |  | Yes | SAVE_DATA_SET |
| UPLOAD_DATA_SET | VARCHAR2 | 4 |  | Yes | UPLOAD_DATA_SET |
| ROLLBACK_DATA_SET | VARCHAR2 | 4 |  |  | ROLLBACK_DATA_SET |
| VIEW_ALL_DATA_SETS | VARCHAR2 | 4 |  | Yes | VIEW_ALL_DATA_SETS |
| MANAGE_TEMPLATE | VARCHAR2 | 4 |  | Yes | MANAGE_TEMPLATE |
| ERROR_INFORMATION | VARCHAR2 | 4000 |  |  | ERROR_INFORMATION |
| GRANT_GEN_STATUS | VARCHAR2 | 4 |  |  | GRANT_GEN_STATUS |
| GRANT_GEN_DETAILS | VARCHAR2 | 4000 |  |  | GRANT_GEN_DETAILS |
| ACTIVE_STATUS | VARCHAR2 | 4 |  |  | ACTIVE_STATUS |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| EXTRA_INFO | VARCHAR2 | 1000 |  |  | EXTRA_INFO |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_LAYOUT_ROLE_MAP_N1 | Non Unique | Default | ROLE_ID, LAYOUT_ID |
| HRC_SDL_LAYOUT_ROLE_MAP_U1 | Unique | Default | ROLE_MAPPING_ID, ORA_SEED_SET1 |
| HRC_SDL_LAYOUT_ROLE_MAP_U11 | Unique | Default | ROLE_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
