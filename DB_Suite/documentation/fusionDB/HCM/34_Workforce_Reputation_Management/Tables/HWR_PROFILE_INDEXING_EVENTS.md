# HWR_PROFILE_INDEXING_EVENTS

Table to store data related to profile indexing events.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprofileindexingevents-8959.html#hwrprofileindexingevents-8959](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprofileindexingevents-8959.html#hwrprofileindexingevents-8959)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PROFILE_INDEXING_EVEN_PK | INDEXING_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INDEXING_EVENT_ID | NUMBER |  |  | Yes | ID field associated with the indexing event |
| ACTION | VARCHAR2 | 40 |  |  | Action associated with event. SNAPSHOT |
| STATUS | VARCHAR2 | 40 |  |  | Status of the event. DONE, RUNNING |
| ENTITY | VARCHAR2 | 80 |  |  | Entity the event is for oracle:apps:hcm:hwr:globalprofile |
| START_DATE | DATE |  |  |  | When the indexing event started. |
| END_DATE | DATE |  |  |  | The date when the indexing event ended. |
| SNAPSHOT | CLOB |  |  |  | Snapshot manifest of the files in repo |
| DOCS_IN_STREAM_COUNT | NUMBER |  |  |  | Number of documents in stream for the event. |
| DOCS_IN_INDEX | NUMBER |  |  |  | Number of document in the main index |
| INDEX_SIZE | NUMBER |  |  |  | Total size of the snapshot on disk in KB |
| TOTAL_TIME | NUMBER |  |  | Yes | TOTAL_TIME column to track the total time of the indexing event. |
| ERROR_MESSAGE | CLOB |  |  |  | ERROR message associated with the event. |
| SERVER_NAME | VARCHAR2 | 1024 |  |  | Name of the sever this action ran on |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PROFILE_INDEXING_EV_N1 | Non Unique | FUSION_TS_TX_DATA | START_DATE |
| HWR_PROFILE_INDEXING_EV_U1 | Unique | FUSION_TS_TX_DATA | INDEXING_EVENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
