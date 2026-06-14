# CMP_STOCK_PROFILES

Stores stock profile data used for stock reporting usually in the form of a third party.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstockprofiles-25752.html#cmpstockprofiles-25752](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstockprofiles-25752.html#cmpstockprofiles-25752)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_STOCK_PROFILES_PK | STOCK_DEFAULTING_CODE, START_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STOCK_DEFAULTING_CODE | VARCHAR2 | 30 |  | Yes | STOCK_DEFAULTING_CODE |
| STATUS_CODE | VARCHAR2 | 30 |  |  | STATUS_CODE |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| GRANT_PRICE | NUMBER |  |  |  | GRANT_PRICE |
| GRANT_TYPE | VARCHAR2 | 30 |  |  | GRANT_TYPE |
| GRANT_NAME | VARCHAR2 | 100 |  |  | GRANT_NAME |
| TRADING_SYMBOL | VARCHAR2 | 30 |  |  | TRADING_SYMBOL |
| GRANT_REASON_CODE | VARCHAR2 | 30 |  |  | GRANT_REASON_CODE |
| GRANT_NUMBER | VARCHAR2 | 30 |  |  | GRANT_NUMBER |
| GRANT_ID | VARCHAR2 | 30 |  |  | GRANT_ID |
| CLASS_TYPE | VARCHAR2 | 30 |  |  | CLASS_TYPE |
| EXPIRATION_DATE | DATE |  |  |  | EXPIRATION_DATE |
| OTHER_WORKER_INFORMATION | VARCHAR2 | 64 |  |  | OTHER_WORKER_INFORMATION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_STOCK_PROFILES_PK | Unique | Default | STOCK_DEFAULTING_CODE, START_DATE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
