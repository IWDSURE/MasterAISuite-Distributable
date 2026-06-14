# BEN_LER_CHG_DPNT_CVG_F

BEN_LER_CHG_DPNT_CVG_F identifies the valid life events that allow a participant to add or remove dependents.Dependent eligibility profiles are then associated with the appropriate program, plan type in program, or plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerchgdpntcvgf-25040.html#benlerchgdpntcvgf-25040](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerchgdpntcvgf-25040.html#benlerchgdpntcvgf-25040)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_CHG_DPNT_CVG_F_PK | LER_CHG_DPNT_CVG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LER_CHG_DPNT_CVG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. |
| PTIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PTIP_F. |
| ADD_RMV_CVG_CD | VARCHAR2 | 30 |  | Yes | Add or remove coverage code. |
| CVG_EFF_END_CD | VARCHAR2 | 30 |  |  | Coverage effective end date. |
| CVG_EFF_STRT_CD | VARCHAR2 | 30 |  |  | Coverage effective start date. |
| LER_CHG_DPNT_CVG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LER_CHG_DPNT_CVG_CD | VARCHAR2 | 30 |  |  | Life event reason change dependent coverage code. |
| CVG_EFF_STRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| CVG_EFF_END_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | CTFN_DETERMINE_CD |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent table discriminator. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_CHG_DPNT_CVG_F_N2 | Non Unique |  | PTIP_ID |
| BEN_LER_CHG_DPNT_CVG_F_N3 | Non Unique |  | PGM_ID |
| BEN_LER_CHG_DPNT_CVG_F_N4 | Non Unique |  | PL_ID |
| BEN_LER_CHG_DPNT_CVG_F_N5 | Non Unique |  | LER_ID |
| BEN_LER_CHG_DPNT_CVG_F_PK | Unique | Default | LER_CHG_DPNT_CVG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
