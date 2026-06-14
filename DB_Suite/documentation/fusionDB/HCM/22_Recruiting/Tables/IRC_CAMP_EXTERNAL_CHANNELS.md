# IRC_CAMP_EXTERNAL_CHANNELS

Table to store the id's of MS Teams channel or slack channel.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampexternalchannels-3480.html#irccampexternalchannels-3480](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampexternalchannels-3480.html#irccampexternalchannels-3480)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_EXTERNAL_CHANNELS_PK | CAMP_EXTERNAL_CHANNEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_EXTERNAL_CHANNEL_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMP_EXTERNAL_WORKSPACE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_EXTERNAL_WORKSPACES table |
| CHANNEL_ID | VARCHAR2 | 128 |  | Yes | Stores the MS Teams channel uuid or Slack channel id. |
| CHANNEL_NAME | VARCHAR2 | 128 |  |  | Stores external channel names like ms teams channel names or slack channel names. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_EXTERNAL_CHANNELS_FK1 | Non Unique | Default | CAMP_EXTERNAL_WORKSPACE_ID |
| IRC_CAMP_EXTERNAL_CHANNELS_PK | Unique | Default | CAMP_EXTERNAL_CHANNEL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
