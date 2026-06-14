# IRC_CAMP_EXTERNAL_WORKSPACES

Table to store the id of Teams (for MS Teams) and Workspaces (for Slack).

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampexternalworkspaces-20172.html#irccampexternalworkspaces-20172](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampexternalworkspaces-20172.html#irccampexternalworkspaces-20172)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_EXTERNAL_WORKSPA_PK | CAMP_EXTERNAL_WORKSPACE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_EXTERNAL_WORKSPACE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table |
| TEAM_ID | VARCHAR2 | 64 |  | Yes | Stores the MS Teams app teams uuid or Slack workspace id (team_id). |
| TEAM_NAME | VARCHAR2 | 128 |  |  | Stores MsTeams team name or slack workspace name |
| CAMP_TEAM_EXT_MSG_SENDER_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_TEAM_EXT_MSG_SENDERS table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_EXTERNAL_WORKSPA_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_EXTERNAL_WORKSPA_FK2 | Non Unique | Default | CAMP_TEAM_EXT_MSG_SENDER_ID |
| IRC_CAMP_EXTERNAL_WORKSPA_PK | Unique | Default | CAMP_EXTERNAL_WORKSPACE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
