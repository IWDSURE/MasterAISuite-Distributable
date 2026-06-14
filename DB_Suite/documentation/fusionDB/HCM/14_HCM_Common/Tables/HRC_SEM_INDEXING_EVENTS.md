# HRC_SEM_INDEXING_EVENTS

Table to store data related to indexing events

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemindexingevents-17233.html#hrcsemindexingevents-17233](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemindexingevents-17233.html#hrcsemindexingevents-17233)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_INDEXING_EVENTS_PK | INDEXING_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INDEXING_EVENT_ID | NUMBER |  |  | Yes | ID field that is associated with IndexingEvent |  |
| SERVER | VARCHAR2 | 80 |  |  | Name of the server where the activity in run |  |
| ACTION | VARCHAR2 | 40 |  |  | Action associated with IndexingEvent |  |
| STATUS | VARCHAR2 | 40 |  |  | Status associated with IndexingEvent |  |
| ENTITY | VARCHAR2 | 1024 |  |  | Entity associated with IndexingEvent |  |
| START_DATE | TIMESTAMP |  |  |  | START_DATE associated with IndexingEvent |  |
| END_DATE | TIMESTAMP |  |  |  | END_DATE associated with IndexingEvent |  |
| ADMIN_CONFIGURATION | VARCHAR2 | 1024 |  |  | ADMIN_CONFIGURATION associated with IndexingEvent | Obsolete |
| ADMIN_CONFIGURATION_CLOB | CLOB |  |  |  | This column contains the admin configuration clob. |  |
| DOCS_IN_STREAM_COUNT | NUMBER |  |  |  | DOCS_IN_STREAM_COUNT associated with IndexingEvent |  |
| DOCS_INDEXED_COUNT | NUMBER |  |  |  | DOCS_INDEXED_COUNT associated with IndexingEvent |  |
| DOCS_DELETED_COUNT | NUMBER |  |  |  | DOCS_DELETED_COUNT associated with IndexingEvent |  |
| DOCS_ERRORED_COUNT | NUMBER |  |  |  | DOCS_ERRORED_COUNT associated with IndexingEvent |  |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | ERROR_MESSAGE associated with IndexingEvent |  |
| INDEX_SIZE | NUMBER |  |  |  | INDEX_SIZE associated with IndexingEvent |  |
| TOTAL_TIME | NUMBER |  |  |  | TOTAL_TIME associated with IndexingEvent |  |
| DB_TIME | NUMBER |  |  |  | DB_TIME associated with IndexingEvent |  |
| UCM_TIME | NUMBER |  |  |  | UCM_TIME associated with IndexingEvent |  |
| PEAK_MEMORY | NUMBER |  |  |  | PEAK_MEMORY associated with IndexingEvent |  |
| DISK_DELTA | NUMBER |  |  |  | DISK_DELTA associated with IndexingEvent |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_INDEXING_EVENTS_N1 | Non Unique | Default | ENTITY, ACTION |
| HRC_SEM_INDEXING_EVENTS_N2 | Non Unique | Default | START_DATE |
| HRC_SEM_INDEXING_EVENTS_U1 | Unique | FUSION_TS_TX_DATA | INDEXING_EVENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
