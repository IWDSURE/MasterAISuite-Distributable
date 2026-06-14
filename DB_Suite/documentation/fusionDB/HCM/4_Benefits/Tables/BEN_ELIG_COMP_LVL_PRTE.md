# BEN_ELIG_COMP_LVL_PRTE

BEN_ELIG_COMP_LVL_PRTE_F specifies the minimum or maximum  compensation amount, or the minimum and maximum range of compensation required to be eligible or excluded from eligbility to participate in a program or plan.   Note that the currency used for determining person's compensation must be the same as the program or plan. . BEN_ELIG_COMP_LVL_PRTE_F  is the intersection of BEN_ELIGY_PRFL_F  and BEN_COMP_LVL_FCTR.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligcomplvlprte-27766.html#beneligcomplvlprte-27766](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligcomplvlprte-27766.html#beneligcomplvlprte-27766)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_COMP_LVL_PRTE_PK | ELIG_COMP_LVL_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_COMP_LVL_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_COMP_LVL_FCTR_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_COMP_LVL_PRTE_FK2 | Non Unique |  | COMP_LVL_FCTR_ID |
| BEN_ELIG_COMP_LVL_PRTE_N1 | Non Unique |  | ELIGY_PRFL_ID |
| BEN_ELIG_COMP_LVL_PRTE_PK | Unique | Default | ELIG_COMP_LVL_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
