# IRC_CAMPAIGNS_B

Base table for Campaign Management. Stores the basic properties of a Campaign

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaignsb-27588.html#irccampaignsb-27588](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaignsb-27588.html#irccampaignsb-27588)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMPAIGNS_B_PK | CAMPAIGN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| HCM_LIST_ID | NUMBER |  | 18 |  | Identifier of HCM Audience List. |
| HCM_LIST_EXTRACTION_DATE | TIMESTAMP |  |  |  | Stores the date and time on which the HCM List was extracted. |
| RESPONSE_OPTION | VARCHAR2 | 30 |  |  | Stores the response option of the get response purpose code of a campaign. Lookup type - ORA_IRC_CAMP_RESPONSE_OPTIONS |
| ELIG_OBJ_ID | NUMBER |  | 18 |  | Stores the eligibility Object Id. Foreign Key to ben_elig_obj_f table |
| ELIG_PRFL_ID | NUMBER |  | 18 |  | Foreign key to IRC_CAMP_ELIG_MAPPING table. Stores the Eligibility Profile id. |
| CAMPAIGN_CODE | VARCHAR2 | 30 |  | Yes | Unique code to determine a campaign for a campaign type. |
| CAMPAIGN_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the campaign. Lookup type - ORA_IRC_CAMP_STATUS |
| PURPOSE_CODE | VARCHAR2 | 30 |  |  | Stores the purpose of the campaign. Lookup type - ORA_IRC_CAMP_PURPOSE |
| TARGET_GOAL_VALUE | NUMBER |  | 10 |  | Stores the target metric for the campaign to compare against the outcome i.e responses or conversions |
| CAMPAIGN_LANGUAGE_CODE | VARCHAR2 | 30 |  |  | Stores the language in which the campaign will be run i.e when deriving names of the objects like Requisitions etc while sending emails. Will be defaulted to the language of the creator of the campaign. |
| CAMPAIGN_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the type of Campaign as lookup code. Lookup type - ORA_IRC_CAMPAIGN_TYPE |
| SEARCH_REQUISITIONS_FLAG | VARCHAR2 | 1 |  |  | Indicates whether to use saved search for deriving requisitions or getting the static list from IRC_CAMP_REQUISITIONS table. Default value 'N' |
| REQ_SAVED_SEARCH_ID | NUMBER |  | 18 |  | Foreign key to IRC_SAVED_SEARCHES table. Stores the saved search criteria for deriving requisitions associated for a campaign. |
| AUDIENCE_SAVED_SEARCH_ID | NUMBER |  | 18 |  | Foreign key to IRC_SAVED_SEARCHES table. Stores the saved search criteria for deriving audience. |
| AUDIENCE_POPULATED_FLAG | VARCHAR2 | 1 |  |  | Indicates if audience is generated for this campaign. Default value 'N' |
| AUD_REHIRE_ELIG_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Specifies if the candidates who are not eligible to be re-hired are ignored for this campaign audience |
| AUD_EMAIL_LIMIT_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Specifies if email cap is enabled on this campaign audience |
| ACTIVATED_ON_DATE | TIMESTAMP |  |  |  | Stores the date and time on which the campaign was activated |
| CANCELLED_ON_DATE | TIMESTAMP |  |  |  | Stores the date and time on which the campaign was cancelled |
| CLOSED_ON_DATE | TIMESTAMP |  |  |  | Stores the date and time on which the campaign was closed |
| VANITY_CONFIG_ID | NUMBER |  | 18 |  | Vanity Config Id. Foreign Key to IRC_CAMP_VANITY_CONFIG table |
| TEAM_ID | NUMBER |  | 18 |  | Identifier of communications teams table. Foreign key to irc_camp_comm_teams_b |
| JOURNEY_ID | NUMBER |  | 18 |  | Identifier of Journey |
| EXCLUDE_JOURNEY_AUD_FLAG | VARCHAR2 | 1 |  |  | Indicates to filter out from final audience, if person has already been assigned to bussiness object item (Journey or Learn). |
| JOURNEY_COMMUNICATION_GOAL | VARCHAR2 | 30 |  |  | Stores the communication goal of journey campaign. Lookup type - ORA_HCO_CAMP_JOURNEY_COMM_GOAL |
| JOURNEY_ASSIGNED_DATE | TIMESTAMP |  |  |  | Date on which the journey was assigned |
| AUDIENCE_COUNT | NUMBER |  | 18 |  | Stores the audience count of the campaign |
| CAMPAIGN_MEDIUM_CODE | VARCHAR2 | 32 |  | Yes | Stores the medium of the campaign. Lookup type - ORA_HCO_CAMP_MEDIUM_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CAMPAIGN_DURATION_CODE | VARCHAR2 | 30 |  |  | This value is coming from the lookup type: ORA_HCO_CAMPAIGN_DURATION_CODE. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMPAIGNS_B_FK1 | Non Unique | Default | REQ_SAVED_SEARCH_ID |
| IRC_CAMPAIGNS_B_FK2 | Non Unique | Default | AUDIENCE_SAVED_SEARCH_ID |
| IRC_CAMPAIGNS_B_FK3 | Non Unique | Default | VANITY_CONFIG_ID |
| IRC_CAMPAIGNS_B_FK4 | Non Unique | Default | ELIG_PRFL_ID |
| IRC_CAMPAIGNS_B_FK5 | Non Unique | Default | TEAM_ID |
| IRC_CAMPAIGNS_B_FK6 | Non Unique | Default | ELIG_OBJ_ID |
| IRC_CAMPAIGNS_B_FK7 | Non Unique | Default | HCM_LIST_ID |
| IRC_CAMPAIGNS_B_N1 | Non Unique | Default | CAMPAIGN_TYPE_CODE, CAMPAIGN_CODE |
| IRC_CAMPAIGNS_B_PK | Unique | Default | CAMPAIGN_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
