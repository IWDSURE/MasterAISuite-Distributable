# IRC_JA_NOTIF_CONFIG

This table is used to store the job sharing action configuration based on candidate selection process action context (IRC_STEP_ACTION_USAGES_B.STEP_ACTION_USAGE_ID).

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjanotifconfig-13670.html#ircjanotifconfig-13670](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjanotifconfig-13670.html#ircjanotifconfig-13670)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_NOTIF_CONFIG_PK | JA_NOTIF_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_NOTIF_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for the table. System generated. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Foreign key IRC_STEP_ACTION_USAGES_B table. (Life cycle action context) |
| NOTIFY_RECRUITER_FLAG | VARCHAR2 | 1 |  |  | Flag that captures if Notification is enable for Recruiter |
| NOTIFY_HIRING_MGR_FLAG | VARCHAR2 | 1 |  |  | Flag that captures if Notification is enable for Hiring Manager |
| INT_CAND_NOTIF_TMPL_ID | NUMBER |  | 18 |  | Email template that is to be used for Internal candidate automatic notifications. Foreign key IRC_DESCRIPTIONS_B.DESCRIPTION_ID |
| EXT_CAND_NOTIF_TMPL_ID | NUMBER |  | 18 |  | Email template that is to be used for External candidate automatic notifications. Foreign key IRC_DESCRIPTIONS_B.DESCRIPTION_ID |
| CANDIDATE_NOTIF_DELAY | NUMBER |  | 9 |  | Stores the delay time in hours before sending notification to the candidate. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_NOTIF_CONFIG_FK1 | Non Unique | Default | STEP_ACTION_USAGE_ID |
| IRC_JA_NOTIF_CONFIG_FK2 | Non Unique | Default | INT_CAND_NOTIF_TMPL_ID |
| IRC_JA_NOTIF_CONFIG_FK3 | Non Unique | Default | EXT_CAND_NOTIF_TMPL_ID |
| IRC_JA_NOTIF_CONFIG_PK | Unique | Default | JA_NOTIF_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
