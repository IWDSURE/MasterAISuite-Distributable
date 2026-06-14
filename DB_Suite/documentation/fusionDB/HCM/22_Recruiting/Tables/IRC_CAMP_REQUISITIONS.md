# IRC_CAMP_REQUISITIONS

Stores the static list of Requisitions associated with a campaign during campaign creation.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamprequisitions-21716.html#irccamprequisitions-21716](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamprequisitions-21716.html#irccamprequisitions-21716)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_REQUISITIONS_PK | CAMPAIGN_REQUISITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMPAIGN_REQUISITION_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_REQUISITIONS_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_REQUISITIONS_FK2 | Non Unique | Default | REQUISITION_ID |
| IRC_CAMP_REQUISITIONS_PK | Unique | Default | CAMPAIGN_REQUISITION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
