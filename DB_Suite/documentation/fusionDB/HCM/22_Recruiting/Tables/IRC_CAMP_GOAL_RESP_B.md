# IRC_CAMP_GOAL_RESP_B

Stores the responses for a campaign goal

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampgoalrespb-27440.html#irccampgoalrespb-27440](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampgoalrespb-27440.html#irccampgoalrespb-27440)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_GOAL_RESP_B_PK | GOAL_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_RESPONSE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| GOAL_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGN_GOALS_B table. |
| DESTINATION_URL | VARCHAR2 | 1000 |  |  | Destination URL candidate should be taken to when he clicks on the response link in email |
| USE_DEFAULT_URL_FLAG | VARCHAR2 | 1 |  |  | Indicates to take the candidate to a default page when he clicks on the response link in email. Mutually exclusive with DESTINATION_URL column. |
| INCLUDE_IN_TARGET_FLAG | VARCHAR2 | 1 |  |  | Indicates whether to count the responses for this goal towards the target goal value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_GOAL_RESP_B_FK1 | Non Unique | Default | GOAL_ID |
| IRC_CAMP_GOAL_RESP_B_PK | Unique | Default | GOAL_RESPONSE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
