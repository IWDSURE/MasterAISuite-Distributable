# IRC_CAMP_ASSET_AUDIENCE

Stores the list of audience for an asset

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetaudience-19654.html#irccampassetaudience-19654](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetaudience-19654.html#irccampassetaudience-19654)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ASSET_AUDIENCE_PK | ASSET_AUDIENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSET_AUDIENCE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Stores the PERSON_ID of the audience. Foreign key to IRC_CANDIDATES table. |
| ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGN_ASSETS_B table. |
| PROCESSING_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the processing status of the audience when integrating with email delivery engine.
Lookup type - ORA_IRC_CAMP_ASSET_AUD_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ASSET_AUDIENCE_FK1 | Non Unique | Default | PERSON_ID |
| IRC_CAMP_ASSET_AUDIENCE_FK2 | Non Unique | Default | ASSET_ID |
| IRC_CAMP_ASSET_AUDIENCE_PK | Unique | Default | ASSET_AUDIENCE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
