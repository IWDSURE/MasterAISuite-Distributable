# IRC_CX_SITE_SETTINGS

Table in which Site  settings are storred. Each setting is unique per site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitesettings-15898.html#irccxsitesettings-15898](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitesettings-15898.html#irccxsitesettings-15898)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_SETTINGS_PK | SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | Primary key of the template setting. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SETTING_KEY | VARCHAR2 | 1000 |  | Yes | Stores the key of the template setting. |
| SETTING_VALUE | VARCHAR2 | 1000 |  |  | Stores the value of the template setting |
| SITE_NUMBER | VARCHAR2 | 240 |  | Yes | Foreign key to the IRC_CX_SITES_B table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_SETTINGS_FK1 | Non Unique | Default | SITE_NUMBER |
| IRC_CX_SITE_SETTINGS_PK | Unique | Default | SETTING_ID |
| IRC_CX_SITE_SETTINGS_U1 | Unique | Default | SETTING_KEY, SITE_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
