# HRC_SDL_MESSAGE_LOGS

This table stores details of errors or warnings logged at the spreadsheet level when run in a debug mode

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlmessagelogs-18728.html#hrcsdlmessagelogs-18728](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlmessagelogs-18728.html#hrcsdlmessagelogs-18728)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_MESSAGE_LOGS_PK | LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOG_ID | NUMBER |  | 18 | Yes | LOG_ID |
| SOURCE_TABLE_NAME | VARCHAR2 | 30 |  |  | SOURCE_TABLE_NAME |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| USER_GUID | VARCHAR2 | 64 |  |  | USER_GUID |
| GENERATED_BY | VARCHAR2 | 30 |  | Yes | GENERATED_BY |
| MESSAGE_TYPE | VARCHAR2 | 100 |  |  | MESSAGE_TYPE |
| MSG_TEXT | VARCHAR2 | 4000 |  |  | MSG_TEXT |
| MSG_TEXT_DETAILS | VARCHAR2 | 4000 |  |  | MSG_TEXT_DETAILS |
| ERROR_STACK | CLOB |  |  |  | ERROR_STACK |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_MESSAGE_LOGS_U1 | Unique | Default | LOG_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
