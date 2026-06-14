# IRC_CX_SITE_FONT_STYLES

The table stores site font related attributes.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitefontstyles-29753.html#irccxsitefontstyles-29753](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitefontstyles-29753.html#irccxsitefontstyles-29753)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_FONT_STYLES_PK | FONT_STYLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FONT_STYLE_ID | NUMBER |  | 18 | Yes | Identifier of the site font related attributes. System generated value. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| WEB_SAFE_FONT_NAME | VARCHAR2 | 200 |  |  | Font family name. The font-family property specifies the font for an element. |  |
| COLOR | VARCHAR2 | 20 |  |  | Font color. The color property specifies the color of text. |  |
| FONT_SIZE | NUMBER |  | 6 |  | Font size. The font-size property sets the size of a font. |  |
| FONT_WEIGHT | VARCHAR2 | 20 |  |  | Font weight. The font-weight property sets how thick or thin characters in text should be displayed. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_FONT_STYLES_PK | Unique | Default | FONT_STYLE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
