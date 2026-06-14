# IRC_CAMP_JOURNEY_METRICS

Table to store the Journey Audience metrics

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampjourneymetrics-7317.html#irccampjourneymetrics-7317](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampjourneymetrics-7317.html#irccampjourneymetrics-7317)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_JOURNEY_METRICS_PK | CAMPAIGN_ID, STATUS, CONTEXT |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Identifier of campaign id.Foreign key to irc_campaigns_b |
| STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of Journey. Lookup type - ORA_HCO_JOURNEY_STATUS |
| CONTEXT | VARCHAR2 | 30 |  | Yes | Audience Metrics or overview Metrics |
| JOURNEY_ID | NUMBER |  | 18 | Yes | Identifier Of journey |
| ELIG_PRFL_ID | NUMBER |  | 18 |  | Identifier of eligibility profile.Foreign key to irc_camp_elig_mapping |
| COUNT | NUMBER |  | 9 |  | Count of Audience |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_JOURNEY_METRICS_FK1 | Non Unique | Default | ELIG_PRFL_ID |
| IRC_CAMP_JOURNEY_METRICS_PK | Unique | Default | CAMPAIGN_ID, STATUS, CONTEXT |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
