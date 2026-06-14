# IRC_CANDIDATE_SEARCH_TRACKING

This table stores when a candidate retrieved by a search query

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandidatesearchtracking-30427.html#irccandidatesearchtracking-30427](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandidatesearchtracking-30427.html#irccandidatesearchtracking-30427)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_SEARCH_TRACKING_PK | CANDIDATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CANDIDATE_ID | NUMBER |  | 18 | Yes | Storing the candidateId of the person who was retrieved by the search. |
| LAST_RETRIEVED_DATE | DATE |  |  |  | Date of the recent search where the  candidate was seen in the results. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_SEARCH_TRACKING_U1 | Unique | FUSION_TS_TX_DATA | CANDIDATE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
