# HRT_PROFILE_LOGS

Table to store model profile log

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilelogs-16935.html#hrtprofilelogs-16935](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilelogs-16935.html#hrtprofilelogs-16935)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_LOGS_PK | PROFILE_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_LOG_ID | NUMBER |  | 18 | Yes | PROFILE_LOG_ID |
| PROFILE_ID | NUMBER |  | 18 | Yes | PROFILE_ID |
| TABLE_NAME | VARCHAR2 | 30 |  | Yes | TABLE_NAME |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| KEY_COL_NAME | VARCHAR2 | 30 |  |  | KEY_COL_NAME |
| KEY_COL_VALUE | VARCHAR2 | 240 |  |  | KEY_COL_VALUE |
| ALTERNATE_COL_NAME | VARCHAR2 | 30 |  |  | ALTERNATE_COL_NAME |
| ALTERNATE_COL_VALUE | VARCHAR2 | 240 |  |  | ALTERNATE_COL_VALUE |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | ACTION_TYPE |
| ACTION_DATE | TIMESTAMP |  |  | Yes | ACTION_DATE |
| VERSION_NUMBER | VARCHAR2 | 100 |  |  | VERSION_NUMBER |
| PROFILE_DATA | CLOB |  |  |  | PROFILE_DATA |
| MODULE | VARCHAR2 | 64 |  |  | MODULE |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_LOGS_PK | Unique | Default | PROFILE_LOG_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
