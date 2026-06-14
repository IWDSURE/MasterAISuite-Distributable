# IRC_CX_SITE_FAVICONS

site_favicons table will be having site related favourite icons with different sizes

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitefavicons-14256.html#irccxsitefavicons-14256](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitefavicons-14256.html#irccxsitefavicons-14256)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_FAVICONS_PK | FAVICON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FAVICON_ID | NUMBER |  | 18 | Yes | Identifier of the favicon. System generated value. |
| SITE_ID | NUMBER |  | 18 | Yes | Identifier of the site. Reference id to the site table |
| FAVICON_IMG | BLOB |  |  | Yes | Using base 64 FaviconImage  as blob |
| IMG_TYPE | VARCHAR2 | 20 |  | Yes | Favicon Image type with multiple resolutions to support desktop,mobile and tablet |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_FAVICONS_FK1 | Non Unique | Default | SITE_ID |
| IRC_CX_SITE_FAVICONS_PK | Unique | Default | FAVICON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
