# IRC_CAND_DUP_NOTIF_CONFIG

The purpose of this new  table is to store lifecycle action configuration
information for new action : Duplicate Candidate Notification

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupnotifconfig-18132.html#irccanddupnotifconfig-18132](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupnotifconfig-18132.html#irccanddupnotifconfig-18132)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_DUP_NOTIF_CONFIG_PK | DUP_CAND_NOTIF_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DUP_CAND_NOTIF_CONFIG_ID | NUMBER |  | 18 | Yes | DUP_CAND_NOTIF_CONFIG_ID : Primary key for this table |
| MATCH_SCORE_LEVEL | VARCHAR2 | 32 |  |  | Duplicate check match score to be configured,uses lookup ORA_IRC_CAND_MATCHSCORE |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | STEP_ACTION_USAGE_ID : Foriegn Key irc_lc_action_usages_b table. (Life cycle action context) |
| NOTIFY_RECRUITER_FLAG | VARCHAR2 | 1 |  |  | Flag that captures if Notification is enable for Recruiter |
| NOTIFY_HIRING_MGR_FLAG | VARCHAR2 | 1 |  |  | Flag that captures if Notification is enable for Hiring Manager |
| NOTIF_TEMPLATE_ID | NUMBER |  | 18 |  | Flag that captures email notification template |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_DUP_NOTIF_CONFIG_FK1 | Unique | Default | STEP_ACTION_USAGE_ID |
| IRC_CAND_DUP_NOTIF_CONFIG_FK2 | Non Unique | Default | NOTIF_TEMPLATE_ID |
| IRC_CAND_DUP_NOTIF_CONFIG_PK | Unique | Default | DUP_CAND_NOTIF_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
