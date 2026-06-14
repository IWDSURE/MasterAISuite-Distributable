# HRC_DL_MESSAGE_LINES

This table is used for logging ERRORS/WARNINGS occurred during TRANSFER,IMPORT,LOAD and VALIDATE processes. This also helps UI to provide ERROR/WARNING information about Each individual process for customers.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlmessagelines-20223.html#hrcdlmessagelines-20223](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlmessagelines-20223.html#hrcdlmessagelines-20223)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_MESSAGE_LINES_PK | MESSAGE_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_LINE_ID | NUMBER |  | 18 | Yes | MESSAGE_LINE_ID |
| MESSAGE_SOURCE_TABLE_NAME | VARCHAR2 | 30 |  | Yes | MESSAGE_SOURCE_TABLE_NAME |
| ORIGINATING_PROCESS | VARCHAR2 | 30 |  | Yes | ORIGINATING_SYSTEM |
| GENERATED_BY | VARCHAR2 | 30 |  | Yes | ORIGINATING_PROCESS_NAME |
| MESSAGE_TYPE | VARCHAR2 | 20 |  | Yes | MESSAGE_TYPE |
| MSG_TEXT | VARCHAR2 | 4000 |  | Yes | MSG_TEXT |
| MSG_ERROR_ID | NUMBER |  | 18 |  | MSG_ERROR_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 |  | DATA_SET_BUS_OBJ_ID |
| STACK_TRACE | VARCHAR2 | 4000 |  |  | STACK_TRACE |
| ERROR_STACK | CLOB |  |  |  | ERROR_STACK |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MESSAGE_SOURCE_LINE_ID | NUMBER |  | 18 | Yes | MESSAGE_SOURCE_LINE_ID |
| ERROR_INFO | VARCHAR2 | 4000 |  |  | Information to translate Error text in user language. |
| GROUP_BY_EXPR_VAL | VARCHAR2 | 4000 |  |  | Column to Group error message text. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| IS_LATEST_FLAG | VARCHAR2 | 1 |  |  | IS_LATEST_FLAG |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| UNTOKENIZED_MESSAGE | VARCHAR2 | 4000 |  |  | UNTOKENIZED_MESSAGE |
| MESSAGE_CAUSE | VARCHAR2 | 4000 |  |  | MESSAGE_CAUSE |
| MESSAGE_USER_ACTION | VARCHAR2 | 4000 |  |  | MESSAGE_USER_ACTION |
| MESSAGE_USER_DETAILS | VARCHAR2 | 4000 |  |  | MESSAGE_USER_DETAILS |
| UNTOKENIZED_MSG_USER_DETAILS | VARCHAR2 | 4000 |  |  | UNTOKENIZED_MSG_USER_DETAILS |
| ARCHIVE_ON_RETRY | VARCHAR2 | 1 |  |  | ARCHIVE_ON_RETRY |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_MESSAGE_LINES_N1 | Non Unique | Default | MESSAGE_SOURCE_LINE_ID, MESSAGE_SOURCE_TABLE_NAME, IS_LATEST_FLAG |
| HRC_DL_MESSAGE_LINES_N2 | Non Unique | Default | DATA_SET_BUS_OBJ_ID, IS_LATEST_FLAG |
| HRC_DL_MESSAGE_LINES_PK | Unique | Default | MESSAGE_LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
