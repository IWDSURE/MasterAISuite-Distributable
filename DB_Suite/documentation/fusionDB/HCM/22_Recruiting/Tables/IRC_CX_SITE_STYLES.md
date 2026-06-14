# IRC_CX_SITE_STYLES

Definition of css class for custom site custom styling

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitestyles-19878.html#irccxsitestyles-19878](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitestyles-19878.html#irccxsitestyles-19878)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_STYLES_PK | STYLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| STYLE_ID | NUMBER |  | 18 | Yes | Identifier of the site css style class. System generated value. |  |
| TYPE_ID | NUMBER |  | 18 |  | Contains ID of style type. Contains reference to style types dictionary table. | Obsolete |
| LINK_STATE_ID | NUMBER |  | 18 |  | Contains ID of child link state | Obsolete |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| THEME_ID | NUMBER |  | 18 | Yes | ID of parent site theme. Details of the site themes which is used to customize the look of a site. |  |
| TEXT_DECORATION | VARCHAR2 | 100 |  |  | Definition of text decoration. CSS text-decoration property specifies the decoration added to text. |  |
| FONT_STYLE_ID | NUMBER |  | 18 |  | Cointains ID of font style. Defines reference to font specific styles. |  |
| CSS_CLASS_NAME | VARCHAR2 | 100 |  |  | Contains pattern used to select the html element that has custom style. |  |
| BACKGROUND_COLOR | VARCHAR2 | 20 |  |  | Definition of background color.Css background-color property sets the background color of an element. |  |
| LINE_HEIGHT | NUMBER |  | 6 |  | The line-height property specifies the line height |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_CX_SITE_STYLES_FK1 | Non Unique | Default | THEME_ID |  |
| IRC_CX_SITE_STYLES_FK2 | Non Unique | Default | TYPE_ID | Obsolete |
| IRC_CX_SITE_STYLES_FK3 | Non Unique | Default | FONT_STYLE_ID |  |
| IRC_CX_SITE_STYLES_FK4 | Non Unique | Default | LINK_STATE_ID | Obsolete |
| IRC_CX_SITE_STYLES_PK | Unique | Default | STYLE_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
