# IRC_CAMP_TRACK_RESPONSE

Stores the responses for a goal in a campaign

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamptrackresponse-11486.html#irccamptrackresponse-11486](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamptrackresponse-11486.html#irccamptrackresponse-11486)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_TRACK_RESPONSE_PK | TRACK_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRACK_RESPONSE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Indicates which person responded. Foreign key to IRC_CANDIDATES table. |
| GOAL_RESPONSE_ID | NUMBER |  | 18 | Yes | Indicates what was the response. Foreign key to IRC_CAMP_GOAL_RESP_B table. |
| GOAL_ID | NUMBER |  | 18 | Yes | Indicates what was the goal for the response. Foreign key to IRC_CAMPAIGN_GOALS_B table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_TRACK_RESPONSE_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_TRACK_RESPONSE_FK2 | Non Unique | Default | PERSON_ID |
| IRC_CAMP_TRACK_RESPONSE_FK3 | Non Unique | Default | GOAL_RESPONSE_ID |
| IRC_CAMP_TRACK_RESPONSE_FK4 | Non Unique | Default | GOAL_ID |
| IRC_CAMP_TRACK_RESPONSE_PK | Unique | Default | TRACK_RESPONSE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
