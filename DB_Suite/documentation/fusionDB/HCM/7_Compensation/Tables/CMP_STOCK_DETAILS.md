# CMP_STOCK_DETAILS

Stores stock grant data used for stock reporting usually in the form of a third party. It hold information such as grant type, number of shares, grant price, expiration, among others.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstockdetails-8525.html#cmpstockdetails-8525](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstockdetails-8525.html#cmpstockdetails-8525)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_STOCK_DETAILS_PK | STOCK_DETAILS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STOCK_DETAILS_ID | NUMBER |  | 18 | Yes | STOCK_DETAILS_ID |
| GRANT_ID | VARCHAR2 | 30 |  |  | GRANT_ID |
| GRANT_NUMBER | VARCHAR2 | 30 |  |  | GRANT_NUMBER |
| GRANT_NAME | VARCHAR2 | 100 |  |  | GRANT_NAME |
| GRANT_TYPE | VARCHAR2 | 30 |  |  | GRANT_TYPE |
| ORIGINAL_GRANT_DATE | DATE |  |  |  | ORIGINAL_GRANT_DATE |
| ORIGINAL_SHARES_GRANTED | NUMBER |  |  |  | ORIGINAL_SHARES_GRANTED |
| ORIGINAL_GRANT_PRICE | NUMBER |  |  |  | ORIGINAL_GRANT_PRICE |
| ORIGINAL_VALUE_AT_GRANT | NUMBER |  |  |  | ORIGINAL_VALUE_AT_GRANT |
| EXERCISE_PRICE | NUMBER |  |  |  | EXERCISE_PRICE |
| TOTAL_SHARES | NUMBER |  |  |  | TOTAL_SHARES |
| VESTED_SHARES | NUMBER |  |  |  | VESTED_SHARES |
| UNVESTED_SHARES | NUMBER |  |  |  | UNVESTED_SHARES |
| EXERCISABLE_SHARES | NUMBER |  |  |  | EXERCISABLE_SHARES |
| EXERCISED_SHARES | NUMBER |  |  |  | EXERCISED_SHARES |
| CANCELLED_SHARES | NUMBER |  |  |  | CANCELLED_SHARES |
| TRADING_SYMBOL | VARCHAR2 | 30 |  |  | TRADING_SYMBOL |
| EXPIRATION_DATE | DATE |  |  |  | EXPIRATION_DATE |
| REASON_CODE | VARCHAR2 | 30 |  |  | REASON_CODE |
| CLASS_TYPE | VARCHAR2 | 30 |  |  | CLASS_TYPE |
| MISC | VARCHAR2 | 100 |  |  | MISC |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| WORKER_NUMBER | VARCHAR2 | 30 |  |  | WORKER_NUMBER |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | ELEMENT_ENTRY_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| VEST_DATE | DATE |  |  |  | VEST_DATE |
| EXERCISE_DATE | DATE |  |  |  | EXERCISE_DATE |
| CANCELLATION_DATE | DATE |  |  |  | CANCELLATION_DATE |
| MISC1_CHAR | VARCHAR2 | 240 |  |  | Miscellaneous Text 1 |
| MISC2_CHAR | VARCHAR2 | 240 |  |  | Miscellaneous Text 2 |
| MISC3_CHAR | VARCHAR2 | 240 |  |  | Miscellaneous Text 3 |
| MISC4_CHAR | VARCHAR2 | 240 |  |  | Miscellaneous Text 4 |
| MISC5_CHAR | VARCHAR2 | 240 |  |  | Miscellaneous Text 5 |
| MISC1_VAL | NUMBER |  |  |  | Miscellaneous Number 1 |
| MISC2_VAL | NUMBER |  |  |  | Miscellaneous Number 2 |
| MISC3_VAL | NUMBER |  |  |  | Miscellaneous Number 3 |
| MISC4_VAL | NUMBER |  |  |  | Miscellaneous Number 4 |
| MISC5_VAL | NUMBER |  |  |  | Miscellaneous Number 5 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_STOCK_DETAILS_N1 | Non Unique | Default | PERSON_ID |
| CMP_STOCK_DETAILS_N2 | Non Unique | Default | WORKER_NUMBER |
| CMP_STOCK_DETAILS_N3 | Non Unique | Default | ELEMENT_ENTRY_ID |
| CMP_STOCK_DETAILS_PK | Unique | Default | STOCK_DETAILS_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
