# BEN_APLD_DPNT_CVG_ELIG_PRFL_F

BEN_APLD_DPNT_CVG_ELIG_PRFL_F specifieswhich dependent coverage eligiblity profiles are being used by which programs, plan types in programs, plans in programs, or plans.  Although many  dependent coverage eligibility profiles may be specified,  the potentially covered dependent must satisfy all required profiles and one of any optional profiles.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benaplddpntcvgeligprflf-16599.html#benaplddpntcvgeligprflf-16599](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benaplddpntcvgeligprflf-16599.html#benaplddpntcvgeligprflf-16599)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_APLD_DPNT_CVG_ELIG_PK | APLD_DPNT_CVG_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APLD_DPNT_CVG_ELIG_PRFL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| APLD_DPNT_CVG_ELIG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| MNDTRY_FLAG | VARCHAR2 | 30 |  | Yes | Mandatory Y or N. |
| DPNT_CVG_ELIGY_PRFL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_DPNT_CVG_ELIGY_PRFL_F. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| PTIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PTIP_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Identifies associated compensation object. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_APLD_D_CVG_ELIG_N2 | Non Unique | Default | PGM_ID |
| BEN_APLD_D_CVG_ELIG_N3 | Non Unique | Default | PTIP_ID |
| BEN_APLD_D_CVG_ELIG_N4 | Non Unique | Default | DPNT_CVG_ELIGY_PRFL_ID |
| BEN_APLD_D_CVG_ELIG_N5 | Non Unique | Default | PL_ID |
| BEN_APLD_D_CVG_ELIG_PK | Unique | Default | APLD_DPNT_CVG_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
