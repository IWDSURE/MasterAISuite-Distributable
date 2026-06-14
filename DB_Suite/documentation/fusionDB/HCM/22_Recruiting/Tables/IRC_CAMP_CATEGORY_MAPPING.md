# IRC_CAMP_CATEGORY_MAPPING

Table to store the categories associated with campaigns.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampcategorymapping-6594.html#irccampcategorymapping-6594](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampcategorymapping-6594.html#irccampcategorymapping-6594)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_CATEGORY_MAPPING_PK | CAMP_CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_CATEGORY_ID | NUMBER |  | 18 | Yes | Primary key for this table. Sysytem generated. |
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMPAIGNS_B table |
| CATEGORY_CODE | VARCHAR2 | 30 |  | Yes | Stores the category associated with the campaign as a lookup code. The corresponding lookup type is ORA_HCO_COMM_CATEGORY. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_CATEGORY_MAPPING_FK1 | Non Unique | Default | CAMPAIGN_ID |
| IRC_CAMP_CATEGORY_MAPPING_PK | Unique | Default | CAMP_CATEGORY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
