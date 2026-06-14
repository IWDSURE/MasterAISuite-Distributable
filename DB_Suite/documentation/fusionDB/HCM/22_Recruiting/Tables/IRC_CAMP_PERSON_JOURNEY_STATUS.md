# IRC_CAMP_PERSON_JOURNEY_STATUS

Table to store the mapping of personId and journey status

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppersonjourneystatus-13894.html#irccamppersonjourneystatus-13894](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppersonjourneystatus-13894.html#irccamppersonjourneystatus-13894)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_PERSON_JOURNEY_ST_PK | CAMPAIGN_ID, PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Identifier of Campaign. Foreign key to irc_campaigns_b |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifier of Person |
| STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of Journey. Lookup type - ORA_HCO_JOURNEY_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_PERSON_JOURNEY_ST_PK | Unique | Default | CAMPAIGN_ID, PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
