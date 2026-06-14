# IRC_CAMP_AUDIENCE_SOURCE

Table to store the campaign and related audience source associations.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudiencesource-4906.html#irccampaudiencesource-4906](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudiencesource-4906.html#irccampaudiencesource-4906)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_AUDIENCE_SOURCE_PK | AUDIENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUDIENCE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| REFRESH_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the audience refresh is allowed or not. Default value is ‘N’ |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table |
| AUDIENCE_SOURCE_TYPE | VARCHAR2 | 64 |  | Yes | Stores the audience source type. It can be Hcm List, Eligibility profile etc. |
| AUDIENCE_SOURCE_ID | NUMBER |  | 18 | Yes | Identifier of audience sources i.e. Hcm List Id, Eligibility Profile Id |
| AUDIENCE_CRITERIA | CLOB |  |  |  | Stores the campaign audience criteria in JSON. |
| AUDIENCE_EXTRACTION_DATE | TIMESTAMP |  |  |  | Stores the date and time on which the Audience was extracted from the source |
| AUDIENCE_COUNT | NUMBER |  | 8 |  | Stores the audience count of the campaign |
| CUSTOM_TOKENS | CLOB |  |  |  | Stores the tokens that are extracted from the excel sheet after transforming and The mappings |
| COLUMN_MAPPING | CLOB |  |  |  | Stores the file column mappings |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Stores the uploaded List description |
| AUDIENCE_EXTRACTION_STATUS | VARCHAR2 | 30 |  |  | Stores the audience extraction status.Valid values ORA_PENDING,ORA_IN_PROGRESS,ORA_COMPLETED,ORA_CANCELLED. |
| STATUS | VARCHAR2 | 30 |  |  | Stores whether record is active or not. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_AUDIENCE_SOURCE_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_AUDIENCE_SOURCE_PK | Unique | Default | AUDIENCE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
