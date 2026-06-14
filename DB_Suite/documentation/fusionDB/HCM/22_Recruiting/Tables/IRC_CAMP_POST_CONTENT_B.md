# IRC_CAMP_POST_CONTENT_B

Stores the content of a post created in post campaigns.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppostcontentb-9149.html#irccamppostcontentb-9149](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppostcontentb-9149.html#irccamppostcontentb-9149)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_POST_CONTENT_B_PK | POST_CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POST_CONTENT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to irc_camp_assets_b table. |
| PRIMARY_LINK_TYPE_CODE | VARCHAR2 | 32 |  |  | Stores the link type for primary post button. Lookup type - ORA_IRC_CAMP_POST_LINK_TYPE. |
| PRIMARY_ASSET_URL_ID | NUMBER |  | 18 |  | Tracking URL for primary action. Foreign key to irc_camp_asset_urls_b table. |
| SECONDARY_LINK_TYPE_CODE | VARCHAR2 | 32 |  |  | Stores the link type for secondary post button. Lookup type - ORA_IRC_CAMP_POST_LINK_TYPE. |
| SECONDARY_ASSET_URL_ID | NUMBER |  | 18 |  | Tracking URL for secondary action. Foreign key to irc_camp_asset_urls_b table. |
| IMAGE_URL | VARCHAR2 | 1000 |  | Yes | Stores location of the thumbnail url for the post banner. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_POST_CONTENT_B_FK1 | Non Unique | Default | ASSET_ID |
| IRC_CAMP_POST_CONTENT_B_FK2 | Non Unique | Default | PRIMARY_ASSET_URL_ID |
| IRC_CAMP_POST_CONTENT_B_FK3 | Non Unique | Default | SECONDARY_ASSET_URL_ID |
| IRC_CAMP_POST_CONTENT_B_PK | Unique | Default | POST_CONTENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
