# IRC_CAMP_MSTEAMS_BOT_CHNL_MAP

Table to store the mapping of bot-appi-id, team, channels and service URL.which will be use in BOT Connector api's to send the message

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampmsteamsbotchnlmap-24488.html#irccampmsteamsbotchnlmap-24488](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampmsteamsbotchnlmap-24488.html#irccampmsteamsbotchnlmap-24488)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_MSTEAMS_BOT_CHNL_PK | CAMP_MSTEAMS_BOT_CHNL_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_MSTEAMS_BOT_CHNL_MAP_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| TEAM_ID | VARCHAR2 | 128 |  | Yes | Stores the internal ID of the team within the Microsoft Teams app. |
| TEAM_THREAD_ID | VARCHAR2 | 128 |  | Yes | Microsoft Teams team thread-style identifier. |
| TEAM_NAME | VARCHAR2 | 128 |  | Yes | Stores the Name of the team within the Microsoft Teams app. |
| TEAM_STATUS | VARCHAR2 | 128 |  | Yes | Stores the team status like activate, delete, archive. |
| CHANNEL_ID | VARCHAR2 | 128 |  | Yes | Stores the internal ID of the channel within the Microsoft Teams app. |
| SERVICE_URL | VARCHAR2 | 255 |  | Yes | Stores the Microsoft teams channels service url. |
| TENANT_ID | VARCHAR2 | 100 |  | Yes | Stores customer tenant guid of Microsoft azure. |
| BOT_APP_ID | VARCHAR2 | 100 |  | Yes | Stores the Microsoft Bot’s Azure app registration ID (client ID). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_MSTEAMS_BOT_CHNL_N1 | Non Unique | Default | CHANNEL_ID, TEAM_ID, BOT_APP_ID |
| IRC_CAMP_MSTEAMS_BOT_CHNL_N2 | Non Unique | Default | BOT_APP_ID, TEAM_STATUS |
| IRC_CAMP_MSTEAMS_BOT_CHNL_N3 | Non Unique | Default | CHANNEL_ID, TEAM_THREAD_ID, BOT_APP_ID |
| IRC_CAMP_MSTEAMS_BOT_CHNL_PK | Unique | Default | CAMP_MSTEAMS_BOT_CHNL_MAP_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
