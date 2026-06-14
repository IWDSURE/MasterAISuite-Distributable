# IRC_CAND_POOL_SYNC_TRACKING

Table used for traceability purpose for Rule Based Candidate Pool Sync in Database

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolsynctracking-29985.html#irccandpoolsynctracking-29985](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolsynctracking-29985.html#irccandpoolsynctracking-29985)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_POOL_SYNC_TRACK_PK | SYNC_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SYNC_TRACKING_ID | NUMBER |  | 18 | Yes | Primary key for this table, System generated |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | Column to store the Sync Job ESS request Id |
| POOL_ID | NUMBER |  | 18 | Yes | Foreign key to hrt_pools_b |
| STATUS | VARCHAR2 | 30 |  | Yes | Status column to represent the current state of sync process for particular pool |
| CAND_PROCESSED_COUNT | NUMBER |  |  |  | Column to store the total number candidate update or created as part of sync process |
| CAND_REMOVED_COUNT | NUMBER |  |  |  | Column to store the total number candidate removed as part of sync process |
| ERROR_MSG | VARCHAR2 | 1000 |  |  | Column to store error message if sync fails for a pool |
| LAST_SYNC_DATE | TIMESTAMP |  |  | Yes | Column to store the last Sync Date Time |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_POOL_SYNC_TRACK_FK1 | Non Unique | Default | POOL_ID |
| IRC_CAND_POOL_SYNC_TRACK_PK | Unique | Default | SYNC_TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
