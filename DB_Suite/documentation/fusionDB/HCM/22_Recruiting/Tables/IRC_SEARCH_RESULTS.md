# IRC_SEARCH_RESULTS

Table to store the denormalized entity rows from IRC_SEARCHES.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchresults-10399.html#ircsearchresults-10399](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchresults-10399.html#ircsearchresults-10399)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEARCH_DETAILS_PK | SEARCH_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_RESULT_ID | NUMBER |  |  | Yes | Primary key for the table. |
| SEARCH_ID | NUMBER |  |  | Yes | Foregin key reference to IRC_SEARCHES. |
| RETRIEVED_ENTITY_ID | NUMBER |  |  | Yes | The entity id flattened from the SEARCH_RESULT column in IRC_SEARCHES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEARCH_DETAILS_U1 | Unique | Default | SEARCH_RESULT_ID |
| IRC_SEARCH_RESULTS_N1 | Non Unique | Default | SEARCH_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
