# IRC_CX_SITES_B

Details of the sites which is used to publish the jobs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitesb-22812.html#irccxsitesb-22812](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitesb-22812.html#irccxsitesb-22812)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITES_B_PK | SITE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SITE_ID | NUMBER |  | 18 | Yes | Identifier of the site. System generated value. |  |
| PREVIEW_THEME_ID | NUMBER |  | 18 |  | ID of site theme which is used for preview. | Obsolete |
| SITE_URL_NAME | VARCHAR2 | 240 |  |  | Site Display Name for URL configured by the customer in the site editor visible in the URL |  |
| EVENTS_ENABLED_FLAG | NUMBER |  | 18 | Yes | Column indicating if events are enabled per site. Will be used by UI to control if events are exposed to users. |  |
| EMAIL_TEMPLATE_ID | NUMBER |  | 18 |  | Id of the email template for the given site (foreign key to IRC_MESSAGE_DESIGNS_B) |  |
| SITE_TYPE | VARCHAR2 | 10 |  | Yes | Type of the Site (External or Internal). EXT - for Existing CE site, ICE - for new internal SITE |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Indicates the status of the object |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SITE_CODE | VARCHAR2 | 200 |  | Yes | Unique site code defined by administrator. |  |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Unique identifier of the site,  auto generated value. |  |
| STATUS_CODE | VARCHAR2 | 20 |  | Yes | Status of the site informing whether site is active or not |  |
| SEQUENCE_NUMBER | NUMBER |  | 18 | Yes | Order of the site on the list of sites. |  |
| DEFAULT_LANG | VARCHAR2 | 4 |  | Yes | Default language in which site will be displayed. |  |
| ACTIVE_THEME_ID | NUMBER |  | 18 |  | ID of site theme which is activated for site. Column is deprecated. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_CX_SITES_B_FK1 | Non Unique | FUSION_TS_SEED | ACTIVE_THEME_ID |  |
| IRC_CX_SITES_B_FK2 | Non Unique | Default | PREVIEW_THEME_ID | Obsolete |
| IRC_CX_SITES_B_N1 | Non Unique | FUSION_TS_SEED | SITE_URL_NAME |  |
| IRC_CX_SITES_B_PK | Unique | FUSION_TS_SEED | SITE_ID |  |
| IRC_CX_SITES_B_U1 | Unique | FUSION_TS_SEED | SITE_CODE |  |
| IRC_CX_SITES_B_U2 | Unique | FUSION_TS_SEED | SITE_NUMBER |  |
| IRC_CX_SITES_B_UK1 | Unique | FUSION_TS_SEED | SITE_ID, DEFAULT_LANG |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
