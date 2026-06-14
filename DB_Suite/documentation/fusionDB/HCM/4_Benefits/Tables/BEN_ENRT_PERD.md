# BEN_ENRT_PERD

BEN_ENRT_PERD  identifies a specific instance of an enrollment period for a program or plan for a defined type of enrollment type cycle.  For example,  the Vision flex program open enrollment for plan year 2001.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtperd-15967.html#benenrtperd-15967](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtperd-15967.html#benenrtperd-15967)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENRT_PERD_PK | ENRT_PERD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENRT_PERD_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| YR_PERD_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_YR_PERD. |
| POPL_ENRT_TYP_CYCL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_POPL_ENRT_TYP_CYCL_F. |
| ENRT_PERD_DET_OVRLP_BCKDT_CD | VARCHAR2 | 30 |  |  | Enrollment period detect overlap backed out. |
| END_DT | DATE |  |  | Yes | End date. |
| STRT_DT | DATE |  |  | Yes | Start date. |
| CLS_ENRT_DT_TO_USE_CD | VARCHAR2 | 30 |  |  | Close enrollment date to use code. |
| DFLT_ENRT_DT | DATE |  |  |  | Default enrollment date. |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage start date code. |
| ENRT_CVG_STRT_DT | DATE |  |  |  | Enrollment coverage start date. |
| ENRT_CVG_END_DT | DATE |  |  |  | Enrollment coverage end date. |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage end date code. |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PROCG_END_DT | DATE |  |  |  | Processing end date. |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | Rate start date code. |
| RT_END_DT_CD | VARCHAR2 | 30 |  |  | Rate end date code. |
| RT_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ASND_LF_EVT_DT | DATE |  |  |  | Assigned life event date. |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. |
| WTHN_YR_PERD_ID | NUMBER |  | 18 |  | wthn yr perd id. |
| ASG_UPDT_EFF_DATE | DATE |  |  |  | Assignment Update effective Date |
| ENRT_PERD_DET_OVRLP_BCK_CD | VARCHAR2 | 30 |  |  | Enrollment period detect overlap backed out. |
| DATA_FREEZE_DATE | DATE |  |  |  | Data Freeze Date. |
| REINSTATE_CD | VARCHAR2 | 30 |  |  | Reinstate Code |
| REINSTATE_OVRDN_CD | VARCHAR2 | 30 |  |  | Reinstate Override Code |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ENRT_PERD_FK2 | Non Unique | Default | YR_PERD_ID |
| BEN_ENRT_PERD_N1 | Non Unique | Default | POPL_ENRT_TYP_CYCL_ID |
| BEN_ENRT_PERD_PK | Unique | Default | ENRT_PERD_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
