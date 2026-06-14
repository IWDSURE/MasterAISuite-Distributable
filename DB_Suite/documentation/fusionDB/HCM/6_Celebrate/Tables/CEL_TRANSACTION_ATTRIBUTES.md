# CEL_TRANSACTION_ATTRIBUTES

Stores additional attributes for attempted transactions such as points transactions.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celtransactionattributes-29136.html#celtransactionattributes-29136](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celtransactionattributes-29136.html#celtransactionattributes-29136)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_TRANSACTION_ATTRIBUTES_PK | TXN_TYPE, TXN_REFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TXN_TYPE | VARCHAR2 | 30 |  | Yes | Transaction type |
| TXN_REFERENCE_ID | NUMBER |  | 18 | Yes | Unique identifier of a transaction |
| PERSON_ID | NUMBER |  | 18 |  | Unique identifier of a person |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Code for status of the transaction |
| REFERENCE_ID1 | NUMBER |  | 18 |  | First reference identifier |
| REFERENCE_ID2 | NUMBER |  | 18 |  | Second reference identifier |
| REFERENCE_ID3 | NUMBER |  | 18 |  | Third reference identifier |
| REFERENCE_ID4 | NUMBER |  | 18 |  | Fourth reference identifier |
| REFERENCE_ID5 | NUMBER |  | 18 |  | Fifth reference identifier |
| NUMBER_VALUE1 | NUMBER |  |  |  | First number value |
| NUMBER_VALUE2 | NUMBER |  |  |  | Second number value |
| NUMBER_VALUE3 | NUMBER |  |  |  | Third number value |
| NUMBER_VALUE4 | NUMBER |  |  |  | Fourth number value |
| NUMBER_VALUE5 | NUMBER |  |  |  | Fifth number value |
| TEXT_VALUE1 | VARCHAR2 | 240 |  |  | First text value |
| TEXT_VALUE2 | VARCHAR2 | 240 |  |  | Second text value |
| TEXT_VALUE3 | VARCHAR2 | 240 |  |  | Third text value |
| TEXT_VALUE4 | VARCHAR2 | 240 |  |  | Fourth text value |
| TEXT_VALUE5 | VARCHAR2 | 240 |  |  | Fifth text value |
| DATE_VALUE1 | DATE |  |  |  | First date value |
| DATE_VALUE2 | DATE |  |  |  | Second date value |
| DATE_VALUE3 | DATE |  |  |  | Third date value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_TRANSACTION_ATTRIBUTES_N1 | Non Unique | Default | PERSON_ID, TXN_TYPE |
| CEL_TRANSACTION_ATTRIBUTES_PK | Unique | Default | TXN_TYPE, TXN_REFERENCE_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
