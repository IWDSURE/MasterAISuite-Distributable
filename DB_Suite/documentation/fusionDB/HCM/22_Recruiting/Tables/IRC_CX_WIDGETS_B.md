# IRC_CX_WIDGETS_B

Admin will be able to manage different custom widget configurations.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxwidgetsb-5964.html#irccxwidgetsb-5964](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxwidgetsb-5964.html#irccxwidgetsb-5964)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_WIDGETS_B_PK | WIDGET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WIDGET_ID | NUMBER |  | 18 | Yes | Primary Key of the Table. System Generated. |
| THEME_ID | NUMBER |  | 18 | Yes | Foreign key to the irc_cx_site_themes table. |
| WIDGET_TYPE_CODE | VARCHAR2 | 200 |  | Yes | Stores the type of Widget. "ACE_WIDGET". |
| WIDGET_TEXT | VARCHAR2 | 1000 |  |  | Optional widget text set by administrator, to be used if supporting multiple widget configurations. |
| WIDGET_ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Default N, indicates if the custom widget section is enabled for configuration. |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | 'ORA_ACTIVE' can be default. Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_WIDGETS_B_FK1 | Non Unique | Default | THEME_ID |
| IRC_CX_WIDGETS_B_PK | Unique | Default | WIDGET_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
