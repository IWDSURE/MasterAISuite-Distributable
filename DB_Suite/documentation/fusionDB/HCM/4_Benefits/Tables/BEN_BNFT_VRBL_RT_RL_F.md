# BEN_BNFT_VRBL_RT_RL_F

BEN_BNFT_VRBL_RT_RL_F  identifies the Fast Formula(e)  to be used to calculate a rate for a benefit. . For example, life insurance coverage benefits may be calculated based on a formula which examines information in the person flexfields or other information or combinations of information not available in delivered rate criteria.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftvrblrtrlf-15389.html#benbnftvrblrtrlf-15389](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftvrblrtrlf-15389.html#benbnftvrblrtrlf-15389)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BNFT_VRBL_RT_RL_F_PK | BNFT_VRBL_RT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BNFT_VRBL_RT_RL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BNFT_VRBL_RT_RL_F. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ORDR_TO_APLY_NUM | NUMBER |  | 18 |  | Order to apply. |
| CVG_AMT_CALC_MTHD_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_CVG_AMT_CALC_MTHD_F. |
| FORMULA_ID | NUMBER |  | 18 | Yes | Foreign key to FF_FORMULAS_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BNFT_VRBL_RT_RL_F_N1 | Non Unique | Default | CVG_AMT_CALC_MTHD_ID |
| BEN_BNFT_VRBL_RT_RL_F_PK | Unique | Default | BNFT_VRBL_RT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
