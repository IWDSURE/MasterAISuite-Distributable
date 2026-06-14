# CMP_CWB_POST_PARM_HDR

Stores Post Process Run Paramater information.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostparmhdr-10734.html#cmpcwbpostparmhdr-10734](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostparmhdr-10734.html#cmpcwbpostparmhdr-10734)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_POST_PARM_HDR_PK | RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ID | NUMBER |  | 18 | Yes | RUN_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| POST_ELEMENT_FLAG | VARCHAR2 | 1 |  |  | POST_ELEMENT_FLAG |
| POST_SALARY_FLAG | VARCHAR2 | 1 |  |  | POST_SALARY_FLAG |
| POST_SINGLE_COMP_FLAG | VARCHAR2 | 1 |  |  | POST_SINGLE_COMP_FLAG |
| POST_STOCK_FLAG | VARCHAR2 | 1 |  |  | POST_STOCK_FLAG |
| POST_PROMOTION_FLAG | VARCHAR2 | 1 |  |  | POST_PROMOTION_FLAG |
| POST_RANK_FLAG | VARCHAR2 | 1 |  |  | POST_RANK_FLAG |
| GRANT_COLUMN_NAME | VARCHAR2 | 100 |  |  | GRANT_COLUMN_NAME |
| ORIGINAL_GRANT_DATE | DATE |  |  |  | ORIGINAL_GRANT_DATE |
| ORIGINAL_GRANT_PRICE | NUMBER |  |  |  | ORIGINAL_GRANT_PRICE |
| ORIGINAL_SHARES_GRANTED | NUMBER |  |  |  | ORIGINAL_SHARES_GRANTED |
| ORIGINAL_VALUE_AT_GRANT | NUMBER |  |  |  | ORIGINAL_VALUE_AT_GRANT |
| GRANT_ID | VARCHAR2 | 30 |  |  | GRANT_ID |
| GRANT_TYPE | VARCHAR2 | 30 |  |  | GRANT_TYPE |
| GRANT_NAME | VARCHAR2 | 100 |  |  | GRANT_NAME |
| GRANT_NUMBER | VARCHAR2 | 30 |  |  | GRANT_NUMBER |
| TRADING_SYMBOL | VARCHAR2 | 30 |  |  | TRADING_SYMBOL |
| REASON_CODE | VARCHAR2 | 30 |  |  | REASON_CODE |
| CLASS_TYPE | VARCHAR2 | 30 |  |  | CLASS_TYPE |
| EXPIRATION_DATE | DATE |  |  |  | EXPIRATION_DATE |
| MISC | VARCHAR2 | 100 |  |  | MISC |
| OPTION_PCT_VESTED_INIT | NUMBER |  |  |  | OPTION_PCT_VESTED_INIT |
| OPTION_VESTING_ROUNDING | VARCHAR2 | 30 |  |  | OPTION_VESTING_ROUNDING |
| PRM_DATE_BEHAVIOR | VARCHAR2 | 30 |  |  | PRM_DATE_BEHAVIOR |
| PRM_STATIC_DATE | DATE |  |  |  | PRM_STATIC_DATE |
| PRM_CHG_BEHAVIOR | VARCHAR2 | 30 |  |  | PRM_CHG_BEHAVIOR |
| RANK_DATE | DATE |  |  |  | RANK_DATE |
| EXPR_COND | VARCHAR2 | 2000 |  |  | Expression Condition |
| MANAGER_INCLUSION_IDS | VARCHAR2 | 1000 |  |  | MANAGER_INCLUSION_IDS - List of  Manager PersonEventId numbers used to  Manager Hierarchy Inclusion. |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| MANAGER_LEVEL | VARCHAR2 | 10 |  |  | MANAGER_LEVEL |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| POSTED_FLAG | VARCHAR2 | 1 |  |  | POSTED_FLAG |
| VEST_DATE | DATE |  |  |  | VEST_DATE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_POST_PARM_HDR_PK | Unique | Default | RUN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
