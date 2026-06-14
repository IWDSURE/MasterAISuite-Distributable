# BEN_LER_CHG_OIPL_ENRT_F

BEN_LER_CHG_OIPL_ENRT_F identifies the impact of a life event reason on the election changes a person may or may not make for an option in a plan.  Each record specifies whether the parameters defined apply to persons who are currently participating in the option in plan or if, as a result of the life event, they are newly eligible to enroll.  . For example, if a person is newly eligible to enroll in the Acme medical plan because of a change of residence postal code life event, they can choose the following options  employee only, employee plus spouse and family.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerchgoiplenrtf-30117.html#benlerchgoiplenrtf-30117](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerchgoiplenrtf-30117.html#benlerchgoiplenrtf-30117)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_CHG_OIPL_ENRT_F_PK | LER_CHG_OIPL_ENRT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LER_CHG_OIPL_ENRT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| OIPL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_OIPL_F. |
| LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_LER_F. |
| AUTO_ENRT_MTHD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| CRNT_ENRT_PRCLDS_CHG_FLAG | VARCHAR2 | 30 |  | Yes | Current enrollment precludes change Y or N. |
| ENRT_CD | VARCHAR2 | 30 |  |  | Enrollment code. |
| ENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DFLT_ENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DFLT_ENRT_CD | VARCHAR2 | 30 |  |  | Default enrollment code. |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Default Y or N. |
| STL_ELIG_CANT_CHG_FLAG | VARCHAR2 | 30 |  | Yes | Still Eligible Cannot Change Y or N. |
| AUTO_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Automatically Enroll Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DFLT_TO_ASN_PNDG_CTFN_CD | VARCHAR2 | 30 |  |  | DFLT_TO_ASN_PNDG_CTFN_CD |
| DFLT_TO_ASN_PNDG_CTFN_RL | NUMBER |  | 18 |  | DFLT_TO_ASN_PNDG_CTFN_RL |
| UNSSPND_RT_CD | VARCHAR2 | 30 |  |  | UNSSPND_RT_CD |
| UNSSPND_ENRT_CD | VARCHAR2 | 30 |  |  | UNSSPND_ENRT_CD |
| UNSSPND_ENRT_RL | NUMBER |  | 18 |  | UNSSPND_ENRT_RL |
| UNSSPND_RT_RL | NUMBER |  | 18 |  | UNSSPND_RT_RL |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_CHGO_ENRT_F_N1 | Non Unique | Default | OIPL_ID |
| BEN_LER_CHGO_ENRT_F_N2 | Non Unique | Default | LER_ID |
| BEN_LER_CHGO_ENRT_F_PK | Unique | Default | LER_CHG_OIPL_ENRT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
