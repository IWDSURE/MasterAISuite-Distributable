# CMP_TCS_STMT_PERD_TL

Setup  Translatable Table that stores the statement Period details. Captures the period start date, end date, display date, availability date, exchange rate rate and the welcome text and welcome page flag.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtperdtl-20409.html#cmptcsstmtperdtl-20409](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtperdtl-20409.html#cmptcsstmtperdtl-20409)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_PERD_TL_PK | STMT_PERD_ID, LANGUAGE, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| WELCOME_TITLE | VARCHAR2 | 240 |  |  | WELCOME_TITLE |
| WELCOME_TEXT | CLOB |  |  |  | WELCOME_TEXT |
| DISPLAY_PERIOD | VARCHAR2 | 240 |  |  | DISPLAY_PERIOD |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_PERD_TL_UK1 | Unique | FUSION_TS_TX_DATA | STMT_PERD_ID, LANGUAGE, BUSINESS_GROUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
