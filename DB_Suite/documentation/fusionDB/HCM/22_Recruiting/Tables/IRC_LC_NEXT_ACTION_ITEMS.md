# IRC_LC_NEXT_ACTION_ITEMS

IRC_LC_NEXT_ACTION_ITEMS table stores all configured actions for the given next action.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcnextactionitems-30445.html#irclcnextactionitems-30445](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcnextactionitems-30445.html#irclcnextactionitems-30445)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_NEXT_ACTION_ITEMS_PK | NEXT_ACTION_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NEXT_ACTION_ITEM_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| NEXT_ACTION_ITEM_CODE | VARCHAR2 | 256 |  | Yes | Next Action Item Code is used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments |
| NEXT_ACTION_ID | NUMBER |  | 18 | Yes | Action Id of the next action. Foreign key to IRC_LC_NEXT_ACTIONS table. |
| ACTION_ID | NUMBER |  | 18 | Yes | Action Id of the next action associated to the Routing step. Foreign key to IRC_LC_ACTIONS_B table. |
| SETTING_ID | NUMBER |  | 18 |  | Setting Id of the next Action. Foreign key to IRC_LC_SETTINGS table. |
| ALLOW_COMMENT_FLAG | VARCHAR2 | 1 |  | Yes | Flag to determine if comment are allowed on the action |
| SEQUENCE_NUMBER | NUMBER |  | 18 | Yes | Sequence for the next action of the Routing Step associated to the Routing step |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_NEXT_ACTION_ITEMS_FK1 | Non Unique | Default | NEXT_ACTION_ID |
| IRC_LC_NEXT_ACTION_ITEMS_FK2 | Non Unique | Default | ACTION_ID |
| IRC_LC_NEXT_ACTION_ITEMS_FK3 | Non Unique | Default | SETTING_ID |
| IRC_LC_NEXT_ACTION_ITEMS_PK | Unique | Default | NEXT_ACTION_ITEM_ID |
| IRC_LC_NEXT_ACTION_ITEMS_U1 | Unique | Default | NEXT_ACTION_ITEM_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
