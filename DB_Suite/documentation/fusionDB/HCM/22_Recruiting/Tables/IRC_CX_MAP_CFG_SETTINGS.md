# IRC_CX_MAP_CFG_SETTINGS

This table will keep information about properties that should be send in API calls to map providers like secret key etc.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxmapcfgsettings-26823.html#irccxmapcfgsettings-26823](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxmapcfgsettings-26823.html#irccxmapcfgsettings-26823)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_MAP_CFG_SETTINGS_PK | CONFIG_SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_SETTING_ID | NUMBER |  | 18 | Yes | Identifier of the application config setting. System generated value. |
| CONFIG_CODE | VARCHAR2 | 200 |  | Yes | Foreign key to irc_cx_map_configs table. |
| SETTING_ID | NUMBER |  | 18 | Yes | Foreign key to irc_cx_map_prov_settings. |
| SETTING_VALUE | VARCHAR2 | 1000 |  | Yes | Value of the setting.As it will store customer senssitive data like API KEY it will be Encrypted. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_MAP_CFG_SETTINGS_FK1 | Non Unique | Default | SETTING_ID |
| IRC_CX_MAP_CFG_SETTINGS_FK2 | Non Unique | Default | CONFIG_CODE |
| IRC_CX_MAP_CFG_SETTINGS_PK | Unique | Default | CONFIG_SETTING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
