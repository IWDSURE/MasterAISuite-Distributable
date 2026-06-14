# BEN_LER_POPL_ACTN_TYP_F

BEN_LER_POPL_ACTN_TYP_F identifies the length of time a person will have to satisfy the requirements of an action type and may be defined for program or plans in programs or plans not in programs against a life event.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerpoplactntypf-26742.html#benlerpoplactntypf-26742](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerpoplactntypf-26742.html#benlerpoplactntypf-26742)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_POPL_ACTN_TYP_F_PK | LER_POPL_ACTN_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LER_POPL_ACTN_TYP_ID | NUMBER |  | 18 | Yes | LER_POPL_ACTN_TYP_ID | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID | Active |
| LER_ID | NUMBER |  | 18 | Yes | LER_ID |  |
| PTIP_ID | NUMBER |  | 18 |  | PTIP_ID |  |
| PL_ID | NUMBER |  | 18 |  | PL_ID |  |
| OIPL_ID | NUMBER |  | 18 |  | OIPL_ID |  |
| ACTN_TYP_ID | NUMBER |  | 18 | Yes | ACTN_TYP_ID | Active |
| ACTN_TYP_CD | VARCHAR2 | 30 |  | Yes | ACTN_TYP_CD |  |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | RQD_FLAG |  |
| ACTN_TYP_DUE_DT_CD | VARCHAR2 | 30 |  |  | ACTN_TYP_DUE_DT_CD | Active |
| ACTN_TYP_DUE_DT_RL | NUMBER |  | 18 |  | ACTN_TYP_DUE_DT_RL | Active |
| SSPND_FLAG | VARCHAR2 | 30 |  | Yes | SSPND_FLAG |  |
| ACTN_TYP_LVL_CD | VARCHAR2 | 30 |  | Yes | ACTN_TYP_LVL_CD |  |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | COMP_OBJ_TYPE |  |
| ASMT_TO_USE_CD | VARCHAR2 | 30 |  |  | ASMT_TO_USE_CD |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_POPL_ACTN_TYP_F_N1 | Non Unique | Default | LER_ID |
| BEN_LER_POPL_ACTN_TYP_F_N2 | Non Unique | Default | PTIP_ID |
| BEN_LER_POPL_ACTN_TYP_F_N3 | Non Unique | Default | PL_ID |
| BEN_LER_POPL_ACTN_TYP_F_N4 | Non Unique | Default | OIPL_ID |
| BEN_LER_POPL_ACTN_TYP_F_PK | Unique | Default | LER_POPL_ACTN_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
