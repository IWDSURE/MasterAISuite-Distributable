# IRC_CAMP_AUDIENCE_STATUS

Table to store the current status of audience associated to different source IDs in different contexts.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudiencestatus-4142.html#irccampaudiencestatus-4142](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudiencestatus-4142.html#irccampaudiencestatus-4142)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_AUDIENCE_STATUS_PK | CAMP_AUDIENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_AUDIENCE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS table |
| AUDIENCE_SOURCE_ID | NUMBER |  | 18 |  | Stores specific source id assigned to audience e.g LearningItemId,JourneyId etc |
| AUDIENCE_SOURCE_CONTEXT | VARCHAR2 | 30 |  |  | Stores Audience Source Context e.g. ORA_LEARN_AUDIENCE or ORA_JOURNEY_AUDIENCE etc |
| STATUS | VARCHAR2 | 64 |  |  | Stores current status of the audience, who is ssociated to the particular audience source Id of learn or journcey e.g Not Started, Started etc |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_AUDIENCE_STATUS_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_AUDIENCE_STATUS_FK2 | Non Unique | Default | PERSON_ID |
| IRC_CAMP_AUDIENCE_STATUS_N1 | Non Unique | Default | AUDIENCE_SOURCE_CONTEXT, AUDIENCE_SOURCE_ID, CAMPAIGN_ID, STATUS |
| IRC_CAMP_AUDIENCE_STATUS_PK | Unique | Default | CAMP_AUDIENCE_ID |
| IRC_CAMP_AUDIENCE_STATUS_U1 | Unique | Default | AUDIENCE_SOURCE_CONTEXT, AUDIENCE_SOURCE_ID, CAMPAIGN_ID, PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
