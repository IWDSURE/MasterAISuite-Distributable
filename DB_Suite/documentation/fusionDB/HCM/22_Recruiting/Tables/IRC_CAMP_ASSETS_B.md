# IRC_CAMP_ASSETS_B

Stores the assets for a campaign

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetsb-18954.html#irccampassetsb-18954](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetsb-18954.html#irccampassetsb-18954)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ASSETS_B_PK | ASSET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSET_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| SEND_IMMEDIATELY_FLAG | VARCHAR2 | 1 |  |  | Indicates if the Send Immediately flag for scheduled asset is enabled. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table. |
| ASSET_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the type of the asset. Lookup type - ORA_IRC_CAMP_ASSET_TYPE |
| ASSET_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the asset. |
| PARENT_ASSET_ID | NUMBER |  | 18 |  | Stores the ASSET_ID of the parent asset. |
| SCHEDULED_DATE | TIMESTAMP |  |  |  | Stores the scheduled date on which the asset should be processed |
| AUDIENCE_DERIVED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the audience is already derived for this asset |
| MESSAGE_DESIGN_ID | NUMBER |  | 18 |  | Foreign key reference to IRC_MSG_DESIGNS_B table. Stores reference to the email design. |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Specifies the targeted site for the Social Media Post |
| START_DELIVERY_DATE | TIMESTAMP |  |  |  | Stores start Delivery date for the asset |
| LAST_DELIVERY_DATE | TIMESTAMP |  |  |  | Stores last Delivery date for the asset |
| FOLLOWUP_DELAY | NUMBER |  | 2 |  | Delay after Sending the Primary Asset in Days |
| ASSET_FREQUENCY | NUMBER |  | 2 |  | Stores the scheduled frequency in Days. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PUBLISH_DEST_CODE | VARCHAR2 | 32 |  |  | Stores the destination of the post. Lookup type - ORA_HCO_CAMP_POST_DESTINATION. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ASSETS_B_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_ASSETS_B_FK2 | Non Unique | Default | MESSAGE_DESIGN_ID |
| IRC_CAMP_ASSETS_B_FK3 | Non Unique | Default | PARENT_ASSET_ID |
| IRC_CAMP_ASSETS_B_PK | Unique | Default | ASSET_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
