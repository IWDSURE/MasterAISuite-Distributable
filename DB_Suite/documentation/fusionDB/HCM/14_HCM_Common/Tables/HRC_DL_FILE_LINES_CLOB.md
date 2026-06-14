# HRC_DL_FILE_LINES_CLOB

This table holds the line data as clob when the line text exceeds 4000 characters. Each row will be identified using FILE_LINE_ID

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfilelinesclob-28112.html#hrcdlfilelinesclob-28112](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfilelinesclob-28112.html#hrcdlfilelinesclob-28112)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_FILE_LINES_CLOB_PK | FILE_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILE_LINE_ID | NUMBER |  | 18 | Yes | FILE_LINE_ID |
| LINE_ID | NUMBER |  | 18 | Yes | LINE_ID |
| TEXT | CLOB |  |  |  | Line Text Clob Column |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_FILE_LINES_CLOB_U1 | Unique | Default | LINE_ID |
| hrc_dl_file_lines_clob_U1 | Unique | Default | FILE_LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
