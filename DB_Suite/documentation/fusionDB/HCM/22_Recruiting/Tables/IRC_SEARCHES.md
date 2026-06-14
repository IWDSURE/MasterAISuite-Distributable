# IRC_SEARCHES

This table stores all the search related details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearches-10700.html#ircsearches-10700](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearches-10700.html#ircsearches-10700)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEARCHES_PK | SEARCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SEARCH_QUERY_TYPE | VARCHAR2 | 30 |  |  | This fiels is to determine what kind of data is stored in SEARCH_QUERY column. |
| DENORMALIZATION_COMPLETED | VARCHAR2 | 2 |  |  | A flag to indicate whether the search and its corresponding action data have been denormalized for reporting. |
| OWNER_PERSON_ID | NUMBER |  | 18 |  | CandidateId of the person who ran the search. |
| SEARCH_QUERY | CLOB |  |  |  | Stores the details of filters null of the search done. |
| SEARCH_RESULT | CLOB |  |  |  | Stores the list of CandidateIds in search result |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CANDIDATE_TRACKING_UPDATED | VARCHAR2 | 1 |  |  | Stores whether this row has processed to update the candidate last retrieved date in IRC_CANDIDATE_SEARCH_TRACKING table |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEARCHES_N1 | Non Unique | FUSION_TS_TX_IDX | CANDIDATE_TRACKING_UPDATED |
| IRC_SEARCHES_N2 | Non Unique | FUSION_TS_TX_IDX | DENORMALIZATION_COMPLETED |
| IRC_SEARCHES_U1 | Unique | FUSION_TS_TX_IDX | SEARCH_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
