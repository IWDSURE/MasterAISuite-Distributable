# IRC_CAMP_CHANNEL_MSG_METRICS

Table to store the channels message reaction, replies and AI Generated Summary.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampchannelmsgmetrics-31264.html#irccampchannelmsgmetrics-31264](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampchannelmsgmetrics-31264.html#irccampchannelmsgmetrics-31264)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_CHANNEL_MSG_MET_PK | CAMP_CHANNEL_MSG_METRIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_CHANNEL_MSG_METRIC_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMP_CHANNEL_MESSAGE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_CHANNEL_MESSAGES table |
| REPLY_COUNT | NUMBER |  | 9 | Yes | Store the total number of replies received on the channel message |
| REACTION_COUNT | NUMBER |  | 9 | Yes | Store the total number of reactions received on the channel message |
| AI_SUMMARY | CLOB |  |  |  | AI-generated summary based on message, replies and reaction counts. |
| AI_SUMMARY_GENERATED_DATE | TIMESTAMP |  |  | Yes | Latest data pull and AI summary generate time stamp |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_CHANNEL_MSG_MET_FK1 | Non Unique | Default | CAMP_CHANNEL_MESSAGE_ID |
| IRC_CAMP_CHANNEL_MSG_MET_PK | Unique | Default | CAMP_CHANNEL_MSG_METRIC_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
