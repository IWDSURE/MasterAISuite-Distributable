# IRC_CAMP_ASSET_URLS_B

Stores the list of URL's that need to be tracked in an asset.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampasseturlsb-24822.html#irccampasseturlsb-24822](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampasseturlsb-24822.html#irccampasseturlsb-24822)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ASSET_URLS_B_PK | ASSET_URL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSET_URL_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| DEEP_LINK_ID | NUMBER |  | 18 |  | Foreign key to irc_camp_deep_links_b table. |
| ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to irc_camp_assets_b table. |
| GOAL_ID | NUMBER |  | 18 |  | Stores the goal to which the url points to. Foreign key to irc_camp_goals_b table. |
| GOAL_RESPONSE_ID | NUMBER |  | 18 |  | Stores the goal response to which the url points to. Foreign key to irc_camp_goal_resp_b table. |
| REQUISITION_ID | NUMBER |  | 18 |  | Stores the Requisition to which the url points to.Foreign key to irc_requisitions_b table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ASSET_URLS_B_FK1 | Non Unique | Default | ASSET_ID |
| IRC_CAMP_ASSET_URLS_B_FK2 | Non Unique | Default | GOAL_ID |
| IRC_CAMP_ASSET_URLS_B_FK3 | Non Unique | Default | GOAL_RESPONSE_ID |
| IRC_CAMP_ASSET_URLS_B_FK4 | Non Unique | Default | REQUISITION_ID |
| IRC_CAMP_ASSET_URLS_B_FK5 | Non Unique | Default | DEEP_LINK_ID |
| IRC_CAMP_ASSET_URLS_B_PK | Unique | Default | ASSET_URL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
