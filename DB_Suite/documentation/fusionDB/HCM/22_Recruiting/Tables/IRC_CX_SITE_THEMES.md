# IRC_CX_SITE_THEMES

Details of the site themes which is used to customize the look of a site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitethemes-29185.html#irccxsitethemes-29185](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitethemes-29185.html#irccxsitethemes-29185)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_THEMES_PK | THEME_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| THEME_ID | NUMBER |  | 18 | Yes | Identifier of the site theme. System generated value. |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Indicates the status of the object |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| TEMPLATE_ID | NUMBER |  |  | Yes | ID of parent site template which defines the layout of the site. |  |
| THEME_NUMBER | VARCHAR2 | 240 |  | Yes | Unique readable identifier generated for Theme. |  |
| THEME_NAME | VARCHAR2 | 200 |  | Yes | Unique name for the site theme. |  |
| HEADER_MODE | NUMBER |  | 1 | Yes | Flag that says in which mode header should be displayed. |  |
| FOOTER_MODE | NUMBER |  | 1 | Yes | Flag that says in which mode footer should be displayed. |  |
| CUSTOM_JS_ENABLED_FLAG | NUMBER |  | 1 | Yes | Flag that says in which if custom js should be enabled |  |
| GENERATED_CUSTOM_CSS | CLOB |  |  |  | Generated CSS the value that will be exposed by ce-custom.css controller. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_THEMES_FK1 | Non Unique | FUSION_TS_SEED | TEMPLATE_ID |
| IRC_CX_SITE_THEMES_PK | Unique | FUSION_TS_SEED | THEME_ID |
| IRC_CX_SITE_THEMES_U1 | Unique | FUSION_TS_SEED | THEME_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
