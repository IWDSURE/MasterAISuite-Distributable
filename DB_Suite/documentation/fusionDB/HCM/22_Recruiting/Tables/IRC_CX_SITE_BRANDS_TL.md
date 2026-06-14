# IRC_CX_SITE_BRANDS_TL

Details of language specific branding properties.  Site Branding Table. MLS table with site branding specific properties.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitebrandstl-26539.html#irccxsitebrandstl-26539](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitebrandstl-26539.html#irccxsitebrandstl-26539)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_BRANDS_TL_PK | BRANDING_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| BRANDING_ID | NUMBER |  | 18 | Yes | Identifier of the site branding. System generated value. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| CUSTOM_CSS | CLOB |  |  |  | The custom css provided by customer. |  |
| DEFAULT_CSS | CLOB |  |  |  | Default CSS to Customer |  |
| FRONT_IMAGE_URL | VARCHAR2 | 2048 |  |  | Column containing translatable URL of background image of the site branding |  |
| LOGO_IMAGE_URL | VARCHAR2 | 2048 |  |  | URL of hero image of the site branding |  |
| MOBILE_FRONT_IMAGE_URL | VARCHAR2 | 2048 |  |  | URL of background image of the site branding for mobile version |  |
| MOBILE_LOGO_IMAGE_URL | VARCHAR2 | 2048 |  |  | URL of hero image of the site branding for mobile version |  |
| NAVIGATION_HEADER_HTML | CLOB |  |  |  | Field to store HTML value of customer navigation block for site branding |  |
| NAVIGATION_FOOTER_HTML | CLOB |  |  |  | Field to store HTML value of customer navigation footer block for site branding |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| CORPORATE_ICON_URL | VARCHAR2 | 2048 |  |  | URL of corporate icon of the site branding |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_BRANDS_TL_PK | Unique | FUSION_TS_SEED | BRANDING_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
