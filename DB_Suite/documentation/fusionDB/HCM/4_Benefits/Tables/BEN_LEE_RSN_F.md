# BEN_LEE_RSN_F

BEN_LEE_RSN_F identifies the parameters which control program or plan enrollment activities resulting from a specific life event reason occurring; in the context it is used here, life event includes those resulting from participant life events.  Open and administrative enrollments information is identified on enrollment period. BEN_LEE_RSN_F defines when key enrollment activities occur and how enrollment start and end dates are determined.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benleersnf-17549.html#benleersnf-17549](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benleersnf-17549.html#benleersnf-17549)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LEE_RSN_F_PK | LEE_RSN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEE_RSN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| POPL_ENRT_TYP_CYCL_ID | NUMBER |  | 18 |  | Foreign key to BEN_POPL_ENRT_TYP_CYCL_F. |
| ENRT_PERD_DET_OVRLP_BCKDT_CD | VARCHAR2 | 30 |  |  | Enrollment period detect overlap backed out. |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. |
| CLS_ENRT_DT_TO_USE_CD | VARCHAR2 | 30 |  |  | Close enrollment date to use code. |
| DYS_AFTR_END_TO_DFLT_NUM | NUMBER |  | 18 |  | Days after end of the enrollment period to default. |
| ENRT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage end date code. |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage start date code. |
| ENRT_PERD_STRT_DT_CD | VARCHAR2 | 30 |  |  | Enrollment period start date code. |
| ENRT_PERD_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_PERD_END_DT_CD | VARCHAR2 | 30 |  |  | Enrollment period end date code. |
| ENRT_PERD_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ADDL_PROCG_DYS_NUM | NUMBER |  | 18 |  | Additional processing days. |
| DYS_NO_ENRL_NOT_ELIG_NUM | NUMBER |  | 18 |  | Days after the end of the enrollment period a person is not eligible. |
| DYS_NO_ENRL_CANT_ENRL_NUM | NUMBER |  | 18 |  | Days after the end of the enrollment period a person can still enroll. |
| RT_END_DT_CD | VARCHAR2 | 30 |  |  | Rate end date code. |
| RT_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | Rate start date code. |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENRT_PERD_DET_OVRLP_BCK_CD | VARCHAR2 | 30 |  |  | Enrollment period detect overlap backed out. |
| REINSTATE_CD | VARCHAR2 | 30 |  |  | Reinstate Code |
| REINSTATE_OVRDN_CD | VARCHAR2 | 30 |  |  | Reinstate Override Code |
| ENRT_PERD_STRT_DAYS | NUMBER |  | 18 |  | User defined number to calculate the enrollment period start date |
| ENRT_PERD_END_DAYS | NUMBER |  | 18 |  | User defined number to calculate the enrollment period start date |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LEE_RSN_F_N1 | Non Unique | Default | POPL_ENRT_TYP_CYCL_ID |
| BEN_LEE_RSN_F_N2 | Non Unique | Default | LER_ID |
| BEN_LEE_RSN_F_N7 | Non Unique | Default | ENRT_PERD_END_DT_RL |
| BEN_LEE_RSN_F_PK | Unique | Default | LEE_RSN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
