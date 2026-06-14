# IRC_CAMP_BO_ASSOC_ITEMS

Table to store the campaign associated business object items.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampboassocitems-16703.html#irccampboassocitems-16703](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampboassocitems-16703.html#irccampboassocitems-16703)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_BO_ASSOC_ITEMS_PK | CAMP_BO_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_BO_ITEM_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAMP_BO_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_BO_ASSOCIATIONS |
| BO_ID | NUMBER |  | 18 | Yes | Identifier of business objects i.e. Learning Item Id, Journey Id. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_BO_ASSOC_ITEMS_FK1 | Non Unique | Default | CAMP_BO_ID |
| IRC_CAMP_BO_ASSOC_ITEMS_N1 | Non Unique | Default | BO_ID |
| IRC_CAMP_BO_ASSOC_ITEMS_PK | Unique | Default | CAMP_BO_ITEM_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
