# CMP_TCS_STMT_PERD

Setup Table that stores the statement Period details. Captures the period start date, end date, display date, availability date, exchange rate rate and the welcome text and welcome page flag.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtperd-21856.html#cmptcsstmtperd-21856](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtperd-21856.html#cmptcsstmtperd-21856)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_PERD_PK | STMT_PERD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_PERD_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| STMT_ID | NUMBER |  | 18 | Yes | Foreign Key to CMP_TCS_STMT |
| START_DATE | DATE |  |  | Yes | period start date |
| END_DATE | DATE |  |  | Yes | period end date |
| AVAILABILITY_DATE | DATE |  |  |  | availability date |
| XCHG_RATE_DATE | DATE |  |  |  | XCHG_RATE_DATE |
| HIDE_WELCOME_FLAG | VARCHAR2 | 1 |  |  | HIDE_WELCOME_FLAG |
| STMT_GENERATED_FLAG | VARCHAR2 | 1 |  |  | status code |
| FEEDBACK_ENABLED_FLAG | VARCHAR2 | 1 |  |  | FEEDBACK_ENABLED_FLAG |
| PERD_FEEDBACK_FLAG | VARCHAR2 | 1 |  |  | Period Feedback Enabled Flag |
| STMT_PERSON_COUNT | NUMBER |  |  |  | Number of Employees having this statement |
| STMT_DATA_COUNT | NUMBER |  |  |  | Number of Statments generated |
| STMT_XML_COUNT | NUMBER |  |  |  | Number of Statements Completed |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_PERD_N1 | Non Unique | Default | STMT_ID, START_DATE, END_DATE |
| CMP_TCS_STMT_PERD_UK1 | Unique | Default | STMT_PERD_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
