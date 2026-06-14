# IRC_CX_ICONS

Table in which custom icons are stored, icons are defined for the particular site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxicons-27947.html#irccxicons-27947](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxicons-27947.html#irccxicons-27947)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_ICONS_PK | ICON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ICON_ID | NUMBER |  | 18 | Yes | The primary key, system generated value. |
| SITE_ID | NUMBER |  | 18 | Yes | Foreign key to the irc_cx_sites_b table. |
| ICON_CODE | VARCHAR2 | 32 |  | Yes | Custom icon identifier in the system. |
| TYPE | VARCHAR2 | 32 |  | Yes | The type of this custom icon for example SVG_URL, SVG_IMAGE, FONT_AWESOME_CODE. |
| DEFINITION | VARCHAR2 | 1000 |  |  | The definition of the custom icon, can be URL or Identifier depending on type. |
| IMAGE | BLOB |  |  |  | The image file of the Custom Icon. |
| STATUS_CODE | VARCHAR2 | 32 |  | Yes | The status code of the Custom Icon. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_ICONS_FK1 | Non Unique | Default | SITE_ID |
| IRC_CX_ICONS_PK | Unique | Default | ICON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
