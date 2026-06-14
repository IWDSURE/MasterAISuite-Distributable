# IRC_CAMP_AUDIENCE

Stores the complete list of audience for a campaign.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudience-24923.html#irccampaudience-24923](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudience-24923.html#irccampaudience-24923)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_AUDIENCE_PK | AUDIENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUDIENCE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the assignment ID of the person.Foreign Key to PER_ALL_ASSIGNMENTS_M. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the Audience Status. Lookup type - ORA_HCO_CAMP_AUD_STATUS |
| PERSON_ID | NUMBER |  | 18 | Yes | Stores the PERSON_ID of the audience. Foreign key to IRC_CANDIDATES table. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table. |
| LAUNCH_ID | NUMBER |  | 18 |  | Foreign key to IRC_CMT_LAUNCHES table. |
| AUDIENCE_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the type of the audience. Lookup type - ORA_IRC_CAMP_AUDIENCE_TYPE |
| UNSUBSCRIBED_TOKEN_ID | NUMBER |  | 18 |  | Stores the reference to the token generated for the unsubscribe link that will be sent for this person via this campaign. |
| UNSUBSCRIBED_FLAG | VARCHAR2 | 1 |  |  | Stores if the candidate unsubscribed from marketing emails through this campaign. |
| WORKER_JOURNEY_ID | NUMBER |  | 18 |  | Stores the latest instance of the allocation of the journey to the person. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_AUDIENCE_FK1 | Non Unique | Default | PERSON_ID |
| IRC_CAMP_AUDIENCE_FK3 | Non Unique | Default | LAUNCH_ID |
| IRC_CAMP_AUDIENCE_FK4 | Non Unique | Default | ASSIGNMENT_ID |
| IRC_CAMP_AUDIENCE_N1 | Non Unique | Default | CAMPAIGN_ID, UNSUBSCRIBED_FLAG |
| IRC_CAMP_AUDIENCE_PK | Unique | Default | AUDIENCE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
