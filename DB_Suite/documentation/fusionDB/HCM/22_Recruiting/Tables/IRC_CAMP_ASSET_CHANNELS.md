# IRC_CAMP_ASSET_CHANNELS

Stores the target channel for an social media asset in a campaign.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetchannels-16260.html#irccampassetchannels-16260](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetchannels-16260.html#irccampassetchannels-16260)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ASSET_CHANNELS_PK | CHANNEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANNEL_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGN_ASSETS_B table. |
| CHANNEL_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the name of social media channel. Lookup type - ORA_IRC_CAMP_CHANNEL_TYPE |
| CHANNEL_POST_URL | VARCHAR2 | 1000 |  |  | Stores the URL of the targeted channel post. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ASSET_CHANNELS_FK1 | Non Unique | Default | ASSET_ID |
| IRC_CAMP_ASSET_CHANNELS_PK | Unique | Default | CHANNEL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
