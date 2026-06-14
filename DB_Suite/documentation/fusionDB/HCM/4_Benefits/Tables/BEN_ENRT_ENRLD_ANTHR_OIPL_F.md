# BEN_ENRT_ENRLD_ANTHR_OIPL_F

BEN_ENRT_ENRLD_ANTHR_OIPL_F identifies in which options in plans a person  must or will be enrolled in if he or she elects to enroll in the option in plan associated.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtenrldanthroiplf-9339.html#benenrtenrldanthroiplf-9339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtenrldanthroiplf-9339.html#benenrtenrldanthroiplf-9339)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENRT_ENRD_ANT_OIPL_PK | ENRT_ENRLD_ANTHR_OIPL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENRT_ENRLD_ANTHR_OIPL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| ENRL_DET_DT_CD | VARCHAR2 | 30 |  |  | Enrollment determination date code. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| OTHR_OIPL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_OIPL_F. |
| OIPL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_OIPL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ENRT_ENRD_ANT_OIPLL_N2 | Non Unique | Default | OIPL_ID |
| BEN_ENRT_ENRD_ANT_OIPL_N1 | Non Unique | Default | OTHR_OIPL_ID |
| BEN_ENRT_ENRD_ANT_OIPL_PK | Unique | Default | ENRT_ENRLD_ANTHR_OIPL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
