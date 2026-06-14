# IRC_CAMP_ASSET_SEGMENTS

Stores the segment definition for an asset in a campaign.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetsegments-14160.html#irccampassetsegments-14160](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetsegments-14160.html#irccampassetsegments-14160)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ASSET_SEGMENTS_PK | ASSET_SEGMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSET_SEGMENT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGN_ASSETS_B table. |
| GOAL_RESPONSE_ID | NUMBER |  | 18 |  | Foreign key to IRC_CAMP_GOAL_RESP_B table. Stores the response segment for deriving audience. |
| SEGMENT_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the segment type for deriving audience. Lookup type - ORA_IRC_CAMP_SEGMENT_TYPES |
| CRITERIA_TYPE_CODE | VARCHAR2 | 30 |  |  | Indicates whether to include or exclude the audience segment. Lookup type - ORA_IRC_CAMP_CRITERIA_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ASSET_SEGMENTS_FK1 | Non Unique | Default | ASSET_ID |
| IRC_CAMP_ASSET_SEGMENTS_FK2 | Non Unique | Default | GOAL_RESPONSE_ID |
| IRC_CAMP_ASSET_SEGMENTS_PK | Unique | Default | ASSET_SEGMENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
