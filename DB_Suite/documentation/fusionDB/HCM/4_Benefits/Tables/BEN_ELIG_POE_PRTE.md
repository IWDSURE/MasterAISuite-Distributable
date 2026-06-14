# BEN_ELIG_POE_PRTE

BEN_ELIG_POE_PRTE stores period of enrollment criteria.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligpoeprte-10780.html#beneligpoeprte-10780](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligpoeprte-10780.html#beneligpoeprte-10780)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_POE_PRTE_PK | ELIG_POE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_POE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Start Date |
| END_DATE | DATE |  |  |  | End date |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| MN_POE_NUM | NUMBER |  | 18 |  | Minimum Number |
| MX_POE_NUM | NUMBER |  | 18 |  | Maximum number |
| NO_MN_POE_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum flag |
| NO_MX_POE_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Flag |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding Code |
| RNDG_RL | NUMBER |  | 18 |  | Rounding Rule |
| POE_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Non Mandatory Units of Measure |
| CBR_DSBLTY_APLS_FLAG | VARCHAR2 | 30 |  | Yes | CBR_DSBLTY_APLS_FLAG |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_POE_PRTE_U1 | Unique | Default | ELIG_POE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
