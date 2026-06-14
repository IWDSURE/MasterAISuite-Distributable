# IRC_LI_RSC_SYNC_HISTORY

Stores the history of calls that were made as part of LinkedIn RSC integration

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscsynchistory-6904.html#irclirscsynchistory-6904](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscsynchistory-6904.html#irclirscsynchistory-6904)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_RSC_SYNC_HISTORY_PK | SYNC_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SYNC_HISTORY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated |
| ENTITY_ID | VARCHAR2 | 100 |  | Yes | Primary Key of the ORC Entity. Can be PERSON_ID, REQUISITION_ID, SUBMISSION_ID. |
| ENTITY_TYPE_CODE | VARCHAR2 | 20 |  | Yes | Indicates the type of ORC entity. The corresponding lookup type is ORA_IRC_LI_RSC_ENTITY_TYPE |
| ACTION_CODE | VARCHAR2 | 20 |  | Yes | Action to be excuted by the sync. The corresponding lookup type is ORA_IRC_LI_RSC_ACTION |
| STATUS_CODE | VARCHAR2 | 20 |  |  | The status of this sync action. The corresponding lookup type is ORA_IRC_LI_RSC_SYNC_STATUS |
| SYNC_ERROR | VARCHAR2 | 1000 |  |  | The error, if any, of the sync action. |
| BATCH_ID | NUMBER |  | 18 |  | Foreign key to IRC_LI_RSC_BATCH_HISTORY |
| ADDITIONAL_INFO | VARCHAR2 | 2000 |  |  | Additional info for the record being synced |
| QUEUE_ID | NUMBER |  | 18 |  | Queue id. This is from a queue table column |
| PROCESSOR_ID | NUMBER |  | 18 |  | Processor id of queue table column |
| ASSOCIATED_ENTITY_ID | VARCHAR2 | 100 |  |  | Assocated entity id from queue table column |
| RETRY_COUNT | NUMBER |  | 4 |  | Retry count from queue table column |
| PROCESS_AFTER_DATE | TIMESTAMP |  |  |  | Process after date from queue table column |
| Q_CREATION_DATE | TIMESTAMP |  |  |  | Creation date from queue table column |
| Q_CREATED_BY | VARCHAR2 | 64 |  |  | Created by from queue table column |
| Q_LAST_UPDATED_BY | VARCHAR2 | 64 |  |  | Last updated by from queue table column |
| Q_LAST_UPDATED_DATE | TIMESTAMP |  |  |  | Last updated date from queue table column |
| Q_LAST_UPDATED_LOGIN | VARCHAR2 | 32 |  |  | Last updated login from queue table column |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PAYLOAD | VARCHAR2 | 1000 |  |  | The OAC(Onsite Apply Configuration) data for requisition |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_RSC_SYNC_HISTORY_FK1 | Non Unique | Default | BATCH_ID |
| IRC_LI_RSC_SYNC_HISTORY_N1 | Non Unique | Default | ENTITY_ID |
| IRC_LI_RSC_SYNC_HISTORY_N2 | Non Unique | Default | CREATION_DATE |
| IRC_LI_RSC_SYNC_HISTORY_N3 | Non Unique | Default | ACTION_CODE, STATUS_CODE |
| IRC_LI_RSC_SYNC_HISTORY_PK | Unique | Default | SYNC_HISTORY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
