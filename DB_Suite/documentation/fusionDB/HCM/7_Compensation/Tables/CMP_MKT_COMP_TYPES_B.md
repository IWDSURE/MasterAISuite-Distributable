# CMP_MKT_COMP_TYPES_B

Table stores the Compensation Types for Market Survey data.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomptypesb-3083.html#cmpmktcomptypesb-3083](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomptypesb-3083.html#cmpmktcomptypesb-3083)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_COMP_TYPE_PK | COMP_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMP_TYPE_ID | NUMBER |  | 18 | Yes | Primary Table Key |
| COMP_TYPE_SEQ_NUM | NUMBER |  |  | Yes | Sequence column |
| COMP_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Code  for the Compensation Type |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| MARKET_TARGET | VARCHAR2 | 30 |  |  | Market Target for the Compensation Type |
| GROUP_CODE | VARCHAR2 | 30 |  | Yes | Comp Type Group Code |
| DATA_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Comp Type Data Type Code |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Comp Type Status Code |
| SEED_DATA | VARCHAR2 | 1 |  |  | Seed data Flag |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_COMP_TYPES_B_U1 | Unique | Default | COMP_TYPE_CODE, BUSINESS_GROUP_ID |
| CMP_MKT_COMP_TYPE_U1 | Unique | Default | COMP_TYPE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
