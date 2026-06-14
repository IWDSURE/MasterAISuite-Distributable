# BEN_PRTN_ELIG_F

BEN_PRTN_ELIG_F identifies participation eligibility criteria for a program, plan types in program, plan in program, plan, or option in plan.  Criteria for participation eligibility are  defined as rules ,through an association with one or more BEN_ELIGY_PRFL_F, or using both approaches.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtneligf-18038.html#benprtneligf-18038](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtneligf-18038.html#benprtneligf-18038)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTN_ELIG_F_PK | PRTN_ELIG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTN_ELIG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PRTN_EFF_STRT_DT_CD | VARCHAR2 | 30 |  |  | Participation effective start date code. |
| PRTN_EFF_END_DT_CD | VARCHAR2 | 30 |  |  | Participation effective end date code. |
| PRTN_EFF_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PRTN_EFF_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| WAIT_PERD_VAL | NUMBER |  | 15 |  | Waiting period value. |
| WAIT_PERD_UOM | VARCHAR2 | 30 |  |  | Waiting period unit of measure. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| WAIT_PERD_DT_TO_USE_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| MX_POE_UOM | VARCHAR2 | 30 |  |  | Maximum period of enrollment unit of measure. |
| MX_POE_VAL | NUMBER |  | 18 |  | Maximum period of enrollment value. |
| MX_POE_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| WAIT_PERD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PTIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PTIP_F. |
| WAIT_PERD_DT_TO_USE_CD | VARCHAR2 | 30 |  |  | Waiting period date to use code. |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F. |
| MX_POE_DET_DT_CD | VARCHAR2 | 30 |  |  | Maximum period of enrollment determination date code. |
| MX_POE_DET_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| MX_POE_APLS_CD | VARCHAR2 | 30 |  |  | Maximum period of enrollment applies to. |
| TRK_SCR_FOR_INELG_FLAG | VARCHAR2 | 30 |  | Yes | Flag to determine if score should be stored for inelig people |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent table discriminator. |
| SNRTY_CONFIG_ID | NUMBER |  | 18 |  | Worker Seniority Date |
| CONFIG_ID_1 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_2 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_3 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_4 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_5 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_NUM_1 | NUMBER |  |  |  | New Genric Number Column |
| CONFIG_NUM_2 | NUMBER |  |  |  | New Genric Number Column |
| CONFIG_NUM_3 | NUMBER |  |  |  | New Genric Number Column |
| CONFIG_NUM_4 | NUMBER |  |  |  | New Genric Number Column |
| CONFIG_NUM_5 | NUMBER |  |  |  | New Genric Number Column |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | New Genric Character Column |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | New Genric Character Column |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | New Genric Character Column |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | New Genric Character Column |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | New Genric Character Column |
| CONFIG_DATE_1 | DATE |  |  |  | New Genric Date Column |
| CONFIG_DATE_2 | DATE |  |  |  | New Genric Date Column |
| CONFIG_DATE_3 | DATE |  |  |  | New Genric Date Column |
| CONFIG_DATE_4 | DATE |  |  |  | New Genric Date Column |
| CONFIG_DATE_5 | DATE |  |  |  | New Genric Date Column |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRNT_ELIG_F_N5 | Non Unique | Default | PTIP_ID |
| BEN_PRNT_ELIG_F_N7 | Non Unique | Default | PLIP_ID |
| BEN_PRTN_ELIG_F_N1 | Non Unique | Default | OIPL_ID |
| BEN_PRTN_ELIG_F_N2 | Non Unique | Default | PGM_ID |
| BEN_PRTN_ELIG_F_N3 | Non Unique | Default | PL_ID |
| BEN_PRTN_ELIG_F_PK | Unique | Default | PRTN_ELIG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
