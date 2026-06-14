# BEN_ENRT_PERD_FOR_PL_F

BEN_ENRT_PERD_FOR_PL_F  identifies the plans in program for which the enrollment period has been defined.  Enrollment periods may be specified for programs or plans not in programs.  When the enrollment period is defined for a program, the user is allowed to specify to which plans in the program the enrollment period applies.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtperdforplf-15048.html#benenrtperdforplf-15048](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtperdforplf-15048.html#benenrtperdforplf-15048)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENRT_PERD_FOR_PL_F_PK | ENRT_PERD_FOR_PL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENRT_PERD_FOR_PL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage start date code. |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage end date code. |
| ENRT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | Rate start date code. |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| RT_END_DT_CD | VARCHAR2 | 30 |  |  | Rate end date code. |
| RT_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_PERD_ID | NUMBER |  | 18 |  | Foreign key to BEN_ENRT_PERD_F. |
| LEE_RSN_ID | NUMBER |  | 18 |  | Foreign key to BEN_LEE_RSN_F. |
| PL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ENRT_PERD_FOR_PL_F_FK1 | Non Unique | Default | ENRT_PERD_ID |
| BEN_ENRT_PERD_FOR_PL_F_N1 | Non Unique | Default | LEE_RSN_ID |
| BEN_ENRT_PERD_FOR_PL_F_N2 | Non Unique | Default | PL_ID |
| BEN_ENRT_PERD_FOR_PL_F_PK | Unique | Default | ENRT_PERD_FOR_PL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
