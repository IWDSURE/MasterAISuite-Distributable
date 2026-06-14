# IRC_CAMP_CONVERSIONS

Stores the conversions for a goal in a campaign. Conversions are Submissions and Referrals.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampconversions-7919.html#irccampconversions-7919](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampconversions-7919.html#irccampconversions-7919)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_CONVERSIONS_PK | CONVERSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONVERSION_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Stores the id of the conversion object. Will be a reference to either SUBMISSION_ID or PROSPECT_ID |
| GOAL_ID | NUMBER |  | 18 | Yes | Stores the goal for which conversion is recorded. Foreign key to IRC_CAMP_GOALS_B table |
| GOAL_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the goal type for which conversion is recorded. Lookup type - ORA_IRC_CAMPAIGN_GOAL_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_CONVERSIONS_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_CONVERSIONS_FK2 | Non Unique | Default | GOAL_ID |
| IRC_CAMP_CONVERSIONS_PK | Unique | Default | CONVERSION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
