# IRC_CX_PROV_SETTINGS

List of the supported setting for the given external providers(like site key). Seeded values.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxprovsettings-13618.html#irccxprovsettings-13618](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxprovsettings-13618.html#irccxprovsettings-13618)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_PROV_SETTINGS_PK | SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | Identifier of the setting. System generated value. |
| VISIBILITY_FLAG | VARCHAR2 | 1 |  | Yes | Flag that is saying if this external provider setting should be visible in the payload. |
| PROVIDER_ID | NUMBER |  | 18 | Yes | Foreign key to the irc_cx_providers table. |
| SETTING_CODE | VARCHAR2 | 1000 |  | Yes | Code of the external provider's setting which will be interpreted by front-end that is needed to initialize/call api. |
| SUPPORTED_FLAG | VARCHAR2 | 1 |  | Yes | Flag that is saying if this external provider is supported by ORC. |
| REQUIRED_FLAG | VARCHAR2 | 1 |  | Yes | Flag informing that the given setting is mandatory, used in configuration. |
| SETTING_NAME | VARCHAR2 | 1000 |  | Yes | Name of the setting that will be displayed on administration page. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_PROV_SETTINGS_FK1 | Non Unique | FUSION_TS_SEED | PROVIDER_ID |
| IRC_CX_PROV_SETTINGS_PK | Unique | FUSION_TS_SEED | SETTING_ID, ORA_SEED_SET1 |
| IRC_CX_PROV_SETTINGS_PK1 | Unique | FUSION_TS_SEED | SETTING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
