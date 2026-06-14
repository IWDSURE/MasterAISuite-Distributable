# IRC_CX_HEADER_SETTINGS

Table in which custom header settings are stored,

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxheadersettings-30339.html#irccxheadersettings-30339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxheadersettings-30339.html#irccxheadersettings-30339)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_HEADER_SETTINGS_PK | SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | The primary key, system generated value. |
| HEADER_ID | NUMBER |  | 18 | Yes | Foreign key to the irc_cx_site_themes table. |
| SETTING_KEY | VARCHAR2 | 1000 |  | Yes | The key of the header setting used by jet client to determine the setting. |
| SETTING_VALUE | VARCHAR2 | 1000 |  |  | The value of the header setting used by jet client to determine the setting value. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_HEADER_SETTINGS_PK | Unique | Default | SETTING_ID |
| IRC_CX_HEADER_SETTINGS_U1 | Unique | Default | HEADER_ID, SETTING_KEY |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
