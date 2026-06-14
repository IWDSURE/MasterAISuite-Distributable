# WLF_EXP_STATEMENTS

Table to strore XAPI statements

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfexpstatements-12093.html#wlfexpstatements-12093](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfexpstatements-12093.html#wlfexpstatements-12093)

## Primary Key

| Name | Columns |
|------|----------|
| LRN_EXP_STATEMENTS_PK | XAPI_RECORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XAPI_RECORD_ID | NUMBER |  | 18 | Yes | Statement Record Id |
| XAPI_STATEMENT_ID | VARCHAR2 | 255 |  | Yes | StatementId From Request |
| XAPI_TIMESTAMP | TIMESTAMP |  |  |  | TimeStamp From Request |
| XAPI_STORED | TIMESTAMP |  |  |  | TimeStamp stored by LRS |
| XAPI_USERID | VARCHAR2 | 255 |  |  | LoggedIn User |
| XAPI_ACTOR | VARCHAR2 | 255 |  |  | ACTOR |
| XAPI_VERB_ID | VARCHAR2 | 255 |  |  | VERB_ID |
| XAPI_VERB | VARCHAR2 | 255 |  |  | VERB |
| XAPI_OBJECT_ID | VARCHAR2 | 3000 |  |  | OBJECT_ID |
| XAPI_OBJECT_NAME | VARCHAR2 | 2000 |  |  | OBJECT_NAME |
| XAPI_STATEMENT | VARCHAR2 | 4000 |  |  | Statement  formed using actor,verb and object |
| XAPI_STATEMENT_BODY | VARCHAR2 | 4000 |  |  | Full Statement Body |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| STATUS | VARCHAR2 | 255 |  |  | Stores the process status for the statement |
| PROCESSED_TIMESTAMP | TIMESTAMP |  |  |  | Latest timestamp at which statement got processed |
| REQUEST_HEADERS | VARCHAR2 | 4000 |  |  | Request Headers coming in /statements POST/PUT request |
| RESULT | VARCHAR2 | 1000 |  |  | Property representing measured statement outcome |
| PROVIDER_ID | NUMBER |  | 18 |  | Provider of the statement |
| REASON_CODE | VARCHAR2 | 255 |  |  | Stores the Process failure reason code for the statement |
| PURPOSE | VARCHAR2 | 25 |  |  | Represents purpose of the object |
| REFERRER | VARCHAR2 | 255 |  |  | Represents the page that referred the current activity |
| REFERRED_POSITION | NUMBER |  | 10 |  | Represents the position of parent activity on the page from which current activity got referred |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_EXP_STATEMENTS_N1 | Non Unique | Default | XAPI_OBJECT_ID, XAPI_ACTOR |
| WLF_EXP_STATEMENTS_N2 | Non Unique | Default | TRUNC("PROCESSED_TIMESTAMP"), STATUS |
| WLF_EXP_STATEMENTS_N3 | Non Unique | Default | STATUS |
| WLF_EXP_STATEMENTS_N4 | Non Unique | Default | XAPI_VERB |
| WLF_EXP_STATEMENTS_N5 | Non Unique | Default | PURPOSE |
| WLF_EXP_STATEMENTS_N6 | Non Unique | Default | XAPI_USERID |
| WLF_EXP_STATEMENTS_U1 | Unique | Default | XAPI_RECORD_ID |
| WLF_EXP_STATEMENTS_U2 | Unique | Default | XAPI_STATEMENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
