# IRC_CAMPAIGN_TRACKING

Stores the click tracking data for an asset in a campaign

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaigntracking-3018.html#irccampaigntracking-3018](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaigntracking-3018.html#irccampaigntracking-3018)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMPAIGN_TRACKING_PK | CAMPAIGN_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMPAIGN_TRACKING_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Indicates the person who you are tracking the data for. Foreign key to IRC_CANDIDATES table. |
| ASSET_URL_ID | NUMBER |  | 18 |  | Foreign key to IRC_CAMPAIGN_ASSET_URLS_B table. |
| REQUISITION_ID | NUMBER |  | 18 |  | Indicates the Requisition that was clicked. Foreign key to IRC_REQUISITIONS_B table |
| TIME_OF_CLICK | TIMESTAMP |  |  |  | Indicates the time at which URL was clicked. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_CAMPAIGN_TRACKING_FK1 | Non Unique | Default | PERSON_ID |  |
| IRC_CAMPAIGN_TRACKING_FK2 | Non Unique | Default | ASSET_URL_ID | Obsolete |
| IRC_CAMPAIGN_TRACKING_FK3 | Non Unique | Default | REQUISITION_ID |  |
| IRC_CAMPAIGN_TRACKING_N1 | Non Unique | Default | ASSET_URL_ID, PERSON_ID |  |
| IRC_CAMPAIGN_TRACKING_PK | Unique | Default | CAMPAIGN_TRACKING_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
