# IRC_CX_SITE_TEMPLATES_B

Details of the site template which is used to customize the layout of a site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitetemplatesb-23219.html#irccxsitetemplatesb-23219](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitetemplatesb-23219.html#irccxsitetemplatesb-23219)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_TEMPLATES_B_PK | TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Identifier of the site template. System generated value. |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Indicates the status of the object |  |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Foreign key to the IRC_CX_SITES_B table. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SPLASH_PAGE_NUMBER | VARCHAR2 | 240 |  |  | Foreign key to the IRC_CC_ELEMENTS_B.ELEMENT_NUMBER column. |  |
| TEMPLATE_NUMBER | VARCHAR2 | 240 |  | Yes | Unique readable identifier generated for Template. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| IS_ACTIVE_FLAG | NUMBER |  | 1 | Yes | Indicates if this template is active for a site. 1 true 0 false. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_TEMPLATES_B_N1 | Non Unique | FUSION_TS_SEED | SPLASH_PAGE_NUMBER |
| IRC_CX_SITE_TEMPLATES_B_N2 | Non Unique | FUSION_TS_SEED | SITE_NUMBER |
| IRC_CX_SITE_TEMPLATES_B_PK | Unique | FUSION_TS_SEED | TEMPLATE_ID |
| IRC_CX_SITE_TEMPLATES_B_U2 | Unique | FUSION_TS_SEED | TEMPLATE_NUMBER, SITE_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
