# IRC_LI_RSC_SYNC_QUEUE

Stores the events that are to be synchronized as part of LinkedIn RSC integration

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscsyncqueue-17984.html#irclirscsyncqueue-17984](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscsyncqueue-17984.html#irclirscsyncqueue-17984)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_RSC_SYNC_QUEUE_PK | QUEUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUEUE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated |
| PROCESSOR_ID | NUMBER |  | 18 |  | This column is used to hold the thread ID for the multi tasking scenrio for RSC Sync |
| ENTITY_ID | VARCHAR2 | 100 |  | Yes | Primary key of the ORC Entitty.  Can be CANDIDATE_ID, REQUISTION_ID, SUBMISSION_ID. |
| ASSOCIATED_ENTITY_ID | VARCHAR2 | 100 |  |  | Primary key of the associated ORC Entity. Can be Person_ID. |
| ENTITY_TYPE_CODE | VARCHAR2 | 20 |  | Yes | Indicates the type of ORC entity. The corresponding lookup type is ORA_IRC_LI_RSC_ENTITY_TYPE |
| ACTION_CODE | VARCHAR2 | 20 |  | Yes | Action to be excuted by the sync. The corresponding lookup type is ORA_IRC_LI_RSC_ACTION |
| RETRY_COUNT | NUMBER |  | 4 | Yes | Indicates the number of times this row was processed |
| PROCESS_AFTER_DATE | TIMESTAMP |  |  |  | Indicates if the processing of this record should occur after a specified date or not. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_RSC_SYNC_QUEUE_N3 | Non Unique | Default | PROCESSOR_ID |
| IRC_LI_RSC_SYNC_QUEUE_N4 | Non Unique | Default | ACTION_CODE, ENTITY_TYPE_CODE, CREATION_DATE |
| IRC_LI_RSC_SYNC_QUEUE_N5 | Non Unique | Default | ENTITY_TYPE_CODE, ENTITY_ID |
| IRC_LI_RSC_SYNC_QUEUE_PK | Unique | Default | QUEUE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
