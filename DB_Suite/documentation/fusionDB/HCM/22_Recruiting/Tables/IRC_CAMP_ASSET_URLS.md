# IRC_CAMP_ASSET_URLS

Stores the list of URL's that need to be tracked in an asset

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampasseturls-11238.html#irccampasseturls-11238](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampasseturls-11238.html#irccampasseturls-11238)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ASSET_URLS_PK | ASSET_URL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSET_URL_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGN_ASSETS_B table. |
| URL | VARCHAR2 | 1000 |  |  | Stores the URL whose clicks are tracked |
| GOAL_ID | NUMBER |  | 18 |  | Stores the goal to which the url points to. Foreign key to IRC_CAMPAIGN_GOALS_B table. |
| GOAL_RESPONSE_ID | NUMBER |  | 18 |  | Stores the goal response to which the url points to. Foreign key to IRC_CAMP_GOAL_RESP_B table. |
| REQUISITION_ID | NUMBER |  | 18 |  | Stores the Requisition to which the url points to.Foreign key to IRC_CAMPAIGN_ASSETS_B table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ASSET_URLS_FK1 | Non Unique | Default | ASSET_ID |
| IRC_CAMP_ASSET_URLS_FK2 | Non Unique | Default | GOAL_ID |
| IRC_CAMP_ASSET_URLS_FK3 | Non Unique | Default | GOAL_RESPONSE_ID |
| IRC_CAMP_ASSET_URLS_FK4 | Non Unique | Default | REQUISITION_ID |
| IRC_CAMP_ASSET_URLS_PK | Unique | Default | ASSET_URL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
