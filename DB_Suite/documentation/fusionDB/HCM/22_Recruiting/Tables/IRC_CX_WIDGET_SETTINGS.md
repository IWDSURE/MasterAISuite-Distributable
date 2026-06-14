# IRC_CX_WIDGET_SETTINGS

Widget configurations settings table.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxwidgetsettings-24811.html#irccxwidgetsettings-24811](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxwidgetsettings-24811.html#irccxwidgetsettings-24811)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_WIDGET_SETTINGS_PK | SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | Primary Key of the Table. System Generated. |
| WIDGET_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CX_WIDGETS_B table. |
| SETTING_KEY | VARCHAR2 | 1000 |  | Yes | The key of the custom widget setting used by jet client to determine the setting. |
| SETTING_VALUE | VARCHAR2 | 1000 |  |  | The value of the custom widget setting used by jet client to determine the setting. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_WIDGET_SETTINGS_PK | Unique | Default | SETTING_ID |
| IRC_CX_WIDGET_SETTINGS_U1 | Unique | Default | WIDGET_ID, UPPER("SETTING_KEY") |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
