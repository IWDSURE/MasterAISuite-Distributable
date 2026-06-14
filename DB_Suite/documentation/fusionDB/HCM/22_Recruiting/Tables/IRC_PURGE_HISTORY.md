# IRC_PURGE_HISTORY

The table is use to store history of recruiting purging job execution information for each entity

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpurgehistory-31321.html#ircpurgehistory-31321](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpurgehistory-31321.html#ircpurgehistory-31321)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PURGE_HISORY_PK | PURGE_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PURGE_HISTORY_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | The process id of the ESS job that purged the entity |
| ENTITY_ID | NUMBER |  | 18 | Yes | This stores entity name that was purged. |
| ACTIVE_DAYS | NUMBER |  | 6 | Yes | Number of active days kept in the entity. |
| BATCH_SIZE | NUMBER |  | 10 | Yes | The number of rows to be purged in each batch for each entity type. |
| EXECUTION_ORDER | NUMBER |  | 3 | Yes | The priority order of the entity that was purged. |
| ENTITIES_PURGED_COUNT | NUMBER |  | 18 |  | The number of entities that were purged. |
| START_TIME | TIMESTAMP |  |  |  | Start time of the purge process for a entity. |
| END_TIME | TIMESTAMP |  |  |  | End time of the purge process for a entity. |
| STATUS | VARCHAR2 | 30 |  |  | This stores the status of the purge process e.g. IN_PROGRESS, COMPLETED, CANCELED, FAILED etc. |
| ERROR_CODE | VARCHAR2 | 64 |  |  | This is use to store error codes, which could be oracle error code or custom error codes. |
| ERROR_MESSAGE | CLOB |  |  |  | The error message returned by PL/SQL. This could be both oracle error message and custom error message. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PURGE_HISTORY_N1 | Non Unique | Default | ENTITY_ID |
| IRC_PURGE_HISTORY_N2 | Non Unique | Default | ESS_REQUEST_ID |
| IRC_PURGE_HISTORY_PK | Unique | Default | PURGE_HISTORY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
