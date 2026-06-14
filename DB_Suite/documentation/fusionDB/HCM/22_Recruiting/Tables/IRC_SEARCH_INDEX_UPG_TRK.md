# IRC_SEARCH_INDEX_UPG_TRK

Table used for tracking upgrade of search indexes.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchindexupgtrk-15066.html#ircsearchindexupgtrk-15066](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchindexupgtrk-15066.html#ircsearchindexupgtrk-15066)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEARCH_INDEX_UPG_TRK_PK | UPGRADE_TRK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| UPGRADE_TRK_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| UPGRADE_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_SEARCH_INDEX_UPGRADES. |
| ENTITY_SUB_TYPE | VARCHAR2 | 32 |  |  | The sub entity type (ex: EXTERNAL) for which the index must be upgraded. |
| UPGRADE_STATUS | VARCHAR2 | 32 |  | Yes | Status of the index upgrade. |
| UPGRADE_START_DATE | TIMESTAMP |  |  |  | Timestamp for when the upgrade has started. |
| UPGRADE_END_DATE | TIMESTAMP |  |  |  | Timestamp for when the upgrade has completed. |
| UPGRADE_FAILURE_REASON | CLOB |  |  |  | The upgrade failure reason. |
| ASYNC_TASK_ID | VARCHAR2 | 256 |  |  | Holds task id returned for  OSCS asynch operation. |
| LATEST_INDEX_VERSION | VARCHAR2 | 32 |  |  | Specifies the latest version of OSCS Index. |
| LATEST_INDEX_NAME | VARCHAR2 | 256 |  |  | Specifies the latest name of OSCS Index. |
| UPGRADE_RETRY_COUNT | NUMBER |  | 9 |  | Specifies the number of times upgrade operation has been retried. |
| REINDEX_ATTEMPTED_COUNT | NUMBER |  | 9 |  | Specifies the number of times re-index operation is attempted but returned 429 response code. |
| INDEX_TO_BE_PURGED | VARCHAR2 | 256 |  |  | Specifies the name of the old index to be purged after a specified period determined by profile options. |
| INDEX_PURGE_STATUS | VARCHAR2 | 32 |  |  | Status of index purge. Ex. COMPLETED, PENDING. |
| INDEX_PURGE_DATE | TIMESTAMP |  |  |  | Timestamp for when the index is purged. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEARCH_INDEX_UPG_TRK_FK1 | Non Unique | Default | UPGRADE_ID, UPGRADE_STATUS |
| IRC_SEARCH_INDEX_UPG_TRK_PK | Unique | Default | UPGRADE_TRK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
