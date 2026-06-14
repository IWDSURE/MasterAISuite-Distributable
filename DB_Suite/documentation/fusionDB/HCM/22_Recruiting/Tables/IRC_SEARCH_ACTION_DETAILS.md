# IRC_SEARCH_ACTION_DETAILS

The details table for the search actiosn which contains the rows of selected and targetted entitites in denormalised form.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchactiondetails-13112.html#ircsearchactiondetails-13112](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchactiondetails-13112.html#ircsearchactiondetails-13112)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEARCH_ACTION_DETAILS_PK | ACTION_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_DETAIL_ID | NUMBER |  |  | Yes | The primary key of the table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEARCH_ID | NUMBER |  |  | Yes | Foreign referenced SEARCH_ID from IRC_SEARCHES. |
| ACTION_ID | NUMBER |  |  | Yes | Foreign referenced ACTION_ID  from IRC_SEARCH_ACTIONS. |
| SELECTED_ENTITY_ID | NUMBER |  |  | Yes | The entity ID which is selected for performing the action. |
| TARGET_ENTITY_ID | NUMBER |  |  |  | The entity ID which is used to complete the action. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEARCH_ACTION_DET_N1 | Non Unique | Default | SEARCH_ID, ACTION_ID |
| IRC_SEARCH_ACTION_DET_U1 | Unique | Default | ACTION_DETAIL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
