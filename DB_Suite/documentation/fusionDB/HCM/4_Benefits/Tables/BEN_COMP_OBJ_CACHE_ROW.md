# BEN_COMP_OBJ_CACHE_ROW

BEN_COMP_OBJECT_CACHE_ROW holds the denormalized compensation information for a run of the Manage life events process.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencompobjcacherow-25219.html#bencompobjcacherow-25219](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencompobjcacherow-25219.html#bencompobjcacherow-25219)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_COMP_OBJ_CACHE_ROW_PK | COMP_OBJ_CACHE_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMP_OBJ_CACHE_ROW_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| COMP_OBJ_CACHE_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_COMP_OBJ_CACHE. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| PTIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PTIP_F. |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |
| PL_NIP | VARCHAR2 | 1 |  | Yes | Plan not in program. |
| ELIG_TRAN_STATE | VARCHAR2 | 100 |  |  | Eligibility transition state. |
| TRK_INELIG_PER_FLAG | VARCHAR2 | 1 |  | Yes | Track Ineligible Person Y or N. |
| PAR_PGM_ID | NUMBER |  | 18 |  | Foreign key top BEN_PGM_F. |
| PAR_PTIP_ID | NUMBER |  | 18 |  | Foreign key top BEN_PTIP_F. |
| PAR_PLIP_ID | NUMBER |  | 18 |  | Foreign key top BEN_PLIP_F. |
| PAR_PL_ID | NUMBER |  | 18 |  | Foreign key top BEN_PL_F. |
| FLAG_BIT_VAL | NUMBER |  | 18 |  | Bit value Y or N. |
| OIPLIP_FLAG_BIT_VAL | NUMBER |  | 18 |  | Option in plan in program bit value Y or N. |
| OIPLIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPLIP_F. |
| PAR_OPT_ID | NUMBER |  |  |  | Foreign key top BEN_OPT_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_COMP_OBJ_CACHE_ROW_PK | Unique | Default | COMP_OBJ_CACHE_ROW_ID |
| BEN_COMP_OBJ_CACHE_ROW_N1 | Non Unique | Default | COMP_OBJ_CACHE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
