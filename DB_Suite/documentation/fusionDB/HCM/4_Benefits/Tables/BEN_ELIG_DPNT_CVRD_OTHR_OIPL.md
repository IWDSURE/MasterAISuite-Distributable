# BEN_ELIG_DPNT_CVRD_OTHR_OIPL

BEN_ELIG_DPNT_CVRD_OTHR_OIPL_F  identifies which options in plans a person must be covered by or (most typical usage) or not covered by (least typical) in order to be eligible to participate in a compensation object. BEN_ELIG_DPNT_CVRD_OTHR_OIPL_Fv is the intersection of BEN_ELIGY_PRFL and BEN_OIPL_F.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligdpntcvrdothroipl-24021.html#beneligdpntcvrdothroipl-24021](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligdpntcvrdothroipl-24021.html#beneligdpntcvrdothroipl-24021)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_DPNT_CVRD_OTHR_O_PK | ELIG_DPNT_CVRD_OTHR_OIPL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_DPNT_CVRD_OTHR_OIPL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| OIPL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_OIPL_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_DPNT_CVRD_OTHR_OI_N1 | Non Unique | Default | OIPL_ID |
| BEN_ELIG_DPNT_CVRD_OTHR_OI_N2 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_DPNT_CVRD_OT_OIPL_PK | Unique | Default | ELIG_DPNT_CVRD_OTHR_OIPL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
