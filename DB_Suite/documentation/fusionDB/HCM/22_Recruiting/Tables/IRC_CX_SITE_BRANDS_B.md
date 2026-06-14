# IRC_CX_SITE_BRANDS_B

Site Branding Table. MLS table with site branding specific properties.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitebrandsb-8362.html#irccxsitebrandsb-8362](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitebrandsb-8362.html#irccxsitebrandsb-8362)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_BRANDS_B_PK | BRANDING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| BRANDING_ID | NUMBER |  | 18 | Yes | Identifier of the site branding. System generated value. |  |
| CUSTOM_JS | CLOB |  |  |  | Custom js used by system administrator |  |
| DEFAULT_JS | CLOB |  |  |  | Default js to be used on demand |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Idicates the status of the object |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| THEME_ID | NUMBER |  | 18 | Yes | Identifier of the theme of branding. ID of parent site theme. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_BRANDS_B_FK1 | Unique | FUSION_TS_SEED | THEME_ID |
| IRC_CX_SITE_BRANDS_B_PK | Unique | FUSION_TS_SEED | BRANDING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
