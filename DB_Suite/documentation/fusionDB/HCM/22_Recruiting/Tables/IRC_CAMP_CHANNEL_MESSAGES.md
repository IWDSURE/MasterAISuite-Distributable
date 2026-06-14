# IRC_CAMP_CHANNEL_MESSAGES

Table to store the id's of messages sent to MS Teams channel or Slack channel etc.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampchannelmessages-3972.html#irccampchannelmessages-3972](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampchannelmessages-3972.html#irccampchannelmessages-3972)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_CHANNEL_MESSAGES_PK | CAMP_CHANNEL_MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_CHANNEL_MESSAGE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMP_EXTERNAL_CHANNEL_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_EXTERNAL_CHANNELS table |
| MESSAGE_ID | VARCHAR2 | 50 |  | Yes | Store the message id of the sent message which is send to channel_id |
| MESSAGE_STATUS | VARCHAR2 | 64 |  | Yes | Store either of the value ORA_ACTIVE or ORA_DELETED. If the message or channel or team/workspace deleted at slack/MsTeam side, we mark value as ORA_DELETED. |
| ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_ASSETS table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_CHANNEL_MESSAGES_FK1 | Non Unique | Default | CAMP_EXTERNAL_CHANNEL_ID |
| IRC_CAMP_CHANNEL_MESSAGES_FK2 | Non Unique | Default | ASSET_ID |
| IRC_CAMP_CHANNEL_MESSAGES_PK | Unique | Default | CAMP_CHANNEL_MESSAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
