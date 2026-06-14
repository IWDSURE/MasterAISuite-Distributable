# BEN_DPNT_CVRD_ANTHR_OIPL_CVG_F

BEN_DPNT_CVRD_ANTHR_OIPL_CVG_F  identifies under which other options in plans a person must have or have had coverage in order to be eligible for coverage under this dependent eligbility profile(most common)or options in plans under which the person may not have or have had coverage in or to  qualify (less common). . BEN_DPNT_CVRD_ANTHR_OIPL_CVG_F  is the  intersection of BEN_DPNT_CVG_ELIGY_PRFL_F  and BEN_OIPL_F.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendpntcvrdanthroiplcvgf-7774.html#bendpntcvrdanthroiplcvgf-7774](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendpntcvrdanthroiplcvgf-7774.html#bendpntcvrdanthroiplcvgf-7774)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DPNT_CVRD_ANT_CV_PK | DPNT_CVRD_ANTHR_OIPL_CVG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DPNT_CVRD_ANTHR_OIPL_CVG_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_DPNT_CVRD_ANTHR_OIPL_CVG_F. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CVG_DET_DT_CD | VARCHAR2 | 30 |  |  | Coverage determination date code. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| OIPL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_OIPL_F. |
| DPNT_CVG_ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_DPNT_CVG_ELIGY_PRFL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_DC_ANTHR_CV_PK | Unique | Default | DPNT_CVRD_ANTHR_OIPL_CVG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| BEN_DC_ANTHR_C_N1 | Non Unique | Default | OIPL_ID |
| BEN_DC_ANTHR_C_N2 | Non Unique | Default | DPNT_CVG_ELIGY_PRFL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
