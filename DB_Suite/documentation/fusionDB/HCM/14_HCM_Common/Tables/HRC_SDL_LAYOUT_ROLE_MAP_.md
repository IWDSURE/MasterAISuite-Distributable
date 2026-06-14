# HRC_SDL_LAYOUT_ROLE_MAP_

This table is used to store Template and Role Mappings. This mapping is used to apply data security in HSDL at Template and Data Set levels.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdllayoutrolemap-21655.html#hrcsdllayoutrolemap-21655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdllayoutrolemap-21655.html#hrcsdllayoutrolemap-21655)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_LAYOUT_ROLE_MAP_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ROLE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_MAPPING_ID | NUMBER |  | 18 | Yes | ROLE_MAPPING_ID |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ROLE_ID | NUMBER |  | 18 |  | ROLE_ID |
| LAYOUT_ID | NUMBER |  | 18 |  | LAYOUT_ID |
| CREATE_DATA_SET | VARCHAR2 | 4 |  |  | CREATE_DATA_SET |
| SAVE_DATA_SET | VARCHAR2 | 4 |  |  | SAVE_DATA_SET |
| UPLOAD_DATA_SET | VARCHAR2 | 4 |  |  | UPLOAD_DATA_SET |
| ROLLBACK_DATA_SET | VARCHAR2 | 4 |  |  | ROLLBACK_DATA_SET |
| VIEW_ALL_DATA_SETS | VARCHAR2 | 4 |  |  | VIEW_ALL_DATA_SETS |
| MANAGE_TEMPLATE | VARCHAR2 | 4 |  |  | MANAGE_TEMPLATE |
| ERROR_INFORMATION | VARCHAR2 | 4000 |  |  | ERROR_INFORMATION |
| GRANT_GEN_STATUS | VARCHAR2 | 4 |  |  | GRANT_GEN_STATUS |
| GRANT_GEN_DETAILS | VARCHAR2 | 4000 |  |  | GRANT_GEN_DETAILS |
| ACTIVE_STATUS | VARCHAR2 | 4 |  |  | ACTIVE_STATUS |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| EXTRA_INFO | VARCHAR2 | 1000 |  |  | EXTRA_INFO |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_LAYOUT_ROLE_MAP_U1_ | Unique | HRC_SDL_LAYOUT_ROLE_MAP_U1_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ROLE_MAPPING_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
