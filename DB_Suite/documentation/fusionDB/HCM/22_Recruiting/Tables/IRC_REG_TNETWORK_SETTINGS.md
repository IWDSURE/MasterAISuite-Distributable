# IRC_REG_TNETWORK_SETTINGS

Table used to store Talent Network configuration details in Fusion Recruiting application.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircregtnetworksettings-20277.html#ircregtnetworksettings-20277](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircregtnetworksettings-20277.html#ircregtnetworksettings-20277)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REG_TNETWORK_SETTINGS_PK | SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REGISTRATION_ID | NUMBER |  | 18 | Yes | To store the registration id. Foreign Key to IRC_REG_TNETWORK_CONFIG. |
| KEY | VARCHAR2 | 30 |  |  | Used To Key returned Talent Network Like integration User Name etc |
| VALUE | VARCHAR2 | 4000 |  |  | Used To value returned Talent Network Like integration UserName value etc |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REG_TNETWORK_SETTINGS_FK1 | Non Unique | Default | REGISTRATION_ID |
| IRC_REG_TNETWORK_SETTINGS_PK | Unique | Default | SETTING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
