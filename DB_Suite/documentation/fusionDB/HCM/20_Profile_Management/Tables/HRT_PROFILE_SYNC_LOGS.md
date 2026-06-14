# HRT_PROFILE_SYNC_LOGS

This table is used to store sync date and status

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesynclogs-26583.html#hrtprofilesynclogs-26583](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesynclogs-26583.html#hrtprofilesynclogs-26583)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_SYNC_LOGS_PK | PROFILE_SYNC_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_SYNC_LOG_ID | NUMBER |  | 18 | Yes | PROFILE_SYNC_LOG_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | ESS_REQUEST_ID |
| SYNC_DATE | TIMESTAMP |  |  |  | SYNC_DATE |
| SYNC_STATUS | VARCHAR2 | 20 |  |  | SYNC_STATUS |
| STACK_TRACE | CLOB |  |  |  | STACK_TRACE |
| MESSAGE_TYPE | VARCHAR2 | 20 |  |  | MESSAGE_TYPE |
| MESSAGE_TEXT | VARCHAR2 | 500 |  |  | MESSAGE_TEXT |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_SYNC_LOGS_PK | Unique | HRT_PROFILE_SYNC_LOGS_PK | PROFILE_SYNC_LOG_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
