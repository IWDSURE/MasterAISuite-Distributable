# CMP_CWB_XCHG

Stores currency conversion rates for a plan period. For example, it will hold conversion rates of local currencies to the corporate currency.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbxchg-9933.html#cmpcwbxchg-9933](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbxchg-9933.html#cmpcwbxchg-9933)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_XCHG_PK | PERIOD_ID, CURRENCY |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| CURRENCY | VARCHAR2 | 30 |  | Yes | CURRENCY | Active |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |  |
| XCHG_RATE | NUMBER |  |  |  | XCHG_RATE | Active |
| XCHG_RATE_DATE | DATE |  |  |  | XCHG_RATE_DATE |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_XCHG_PK | Unique | Default | PERIOD_ID, CURRENCY |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
