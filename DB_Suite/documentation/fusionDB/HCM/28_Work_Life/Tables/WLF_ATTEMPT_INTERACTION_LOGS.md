# WLF_ATTEMPT_INTERACTION_LOGS

Table to store attempt interaction logs from player and server

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** WLF_ATTEMPT_INTERACTION_LOGS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattemptinteractionlogs-23011.html#wlfattemptinteractionlogs-23011](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattemptinteractionlogs-23011.html#wlfattemptinteractionlogs-23011)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ATTEMPT_INTERACTION_LO_PK | INTERACTION_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERACTION_LOG_ID | NUMBER |  | 18 | Yes | Primary key |
| CONTENT_LEARNING_ITEM_ID | NUMBER |  | 18 |  | Content LI ID |
| ATTEMPT_INTERACTION_ID | NUMBER |  | 18 |  | Interaction ID |
| LOG_TYPE | VARCHAR2 | 30 |  | Yes | Log type: SERVER, PLAYER |
| REQUEST_PAYLOAD | CLOB |  |  |  | Request Payload |
| RESPONSE_PAYLOAD | CLOB |  |  |  | Response Payload |
| REQUEST_TIMESTAMP | TIMESTAMP |  |  | Yes | Request Timestamp |
| RESPONSE_TIMESTAMP | TIMESTAMP |  |  |  | Response Timestamp |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ATTEMPT_INTERACT_LOGS_N1 | Non Unique | WLF_ATTEMPT_INTERACT_LOGS_N1 | ATTEMPT_INTERACTION_ID |
| WLF_ATTEMPT_INTERACT_LOGS_N2 | Non Unique | WLF_ATTEMPT_INTERACT_LOGS_N2 | CREATION_DATE |
| WLF_ATTEMPT_INTERACT_LOGS_U1 | Unique | WLF_ATTEMPT_INTERACT_LOGS_U1 | INTERACTION_LOG_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
