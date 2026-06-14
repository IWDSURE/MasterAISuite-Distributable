# IRC_CAMP_POST_VIEWS

Stores the page view information for an social post in a campaign

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppostviews-24325.html#irccamppostviews-24325](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppostviews-24325.html#irccamppostviews-24325)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_POST_VIEWS_PK | POST_VIEW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POST_VIEW_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CHANNEL_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_CAMP_ASSET_CHANNEL table. |
| TIME_OF_CLICK | TIMESTAMP |  |  | Yes | Indicates the time at which URL was rendered. |
| SOURCE | VARCHAR2 | 1000 |  |  | Stores referral information from where link is clicked from. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_POST_VIEWS_FK1 | Non Unique | Default | CHANNEL_ID |
| IRC_CAMP_POST_VIEWS_PK | Unique | Default | POST_VIEW_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
