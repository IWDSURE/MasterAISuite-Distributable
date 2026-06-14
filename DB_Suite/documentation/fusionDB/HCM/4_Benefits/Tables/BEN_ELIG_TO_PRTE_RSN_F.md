# BEN_ELIG_TO_PRTE_RSN_F

BEN_ELIG_TO_PRTE_RSN_F identifies the impact of a life event reason on eligibility for a program, plan type in program,plan in program, plan, or option in plan.  A life event reason may be identified as causing immediate eligibility or ineligibility without checking any applicable eligibility profiles.  Examples of life events that may make a person immediately ineligible are termination of employment and death.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligtoprtersnf-8052.html#beneligtoprtersnf-8052](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligtoprtersnf-8052.html#beneligtoprtersnf-8052)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_TO_PRTE_RSN_F_PK | ELIG_TO_PRTE_RSN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_TO_PRTE_RSN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_LER_F. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| IGNR_PRTN_OVRID_FLAG | VARCHAR2 | 30 |  | Yes | Ignore Participation Override Y or N. |
| ELIG_INELIG_CD | VARCHAR2 | 30 |  | Yes | Eligible or ineligible code. |
| PRTN_OVRIDBL_FLAG | VARCHAR2 | 30 |  | Yes | Participation overridable Y or N. |
| PEO_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| PEO_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PEO_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PRTN_EFF_STRT_DT_CD | VARCHAR2 | 30 |  |  | Participation effective start date code. |
| PRTN_EFF_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PRTN_EFF_END_DT_CD | VARCHAR2 | 30 |  |  | Participation effective end date code. |
| PRTN_EFF_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| WAIT_PERD_UOM | VARCHAR2 | 30 |  |  | Waiting period unit of measure. |
| WAIT_PERD_VAL | NUMBER |  | 18 |  | Waiting period value. |
| WAIT_PERD_DT_TO_USE_CD | VARCHAR2 | 30 |  |  | Waiting period date to use code. |
| WAIT_PERD_DT_TO_USE_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| MX_POE_UOM | VARCHAR2 | 30 |  |  | Maximum period of enrollment unit of measure. |
| MX_POE_VAL | NUMBER |  | 18 |  | Maximum period of enrollment value. |
| MX_POE_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| WAIT_PERD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| MX_POE_DET_DT_CD | VARCHAR2 | 30 |  |  | Maximum period of enrollment determination date code. |
| MX_POE_DET_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PTIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PTIP_F. |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F. |
| MX_POE_APLS_CD | VARCHAR2 | 30 |  |  | Maximum period of enrollment applies to. |
| VRFY_FMLY_MMBR_CD | VARCHAR2 | 30 |  |  | Verify family member code |
| VRFY_FMLY_MMBR_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Identifies parent object |
| SNRTY_CONFIG_ID | NUMBER |  | 18 |  | Worker Seniority Date |
| CONFIG_ID_1 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_2 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_3 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_4 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_ID_5 | NUMBER |  | 18 |  | New Generic Column |
| CONFIG_NUM_1 | NUMBER |  |  |  | New Generic Column |
| CONFIG_NUM_2 | NUMBER |  |  |  | New Generic Column |
| CONFIG_NUM_3 | NUMBER |  |  |  | New Generic Column |
| CONFIG_NUM_4 | NUMBER |  |  |  | New Generic Column |
| CONFIG_NUM_5 | NUMBER |  |  |  | New Generic Column |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | New Generic Column |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | New Generic Column |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | New Generic Column |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | New Generic Column |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | New Generic Column |
| CONFIG_DATE_1 | DATE |  |  |  | New Generic Column |
| CONFIG_DATE_2 | DATE |  |  |  | New Generic Column |
| CONFIG_DATE_3 | DATE |  |  |  | New Generic Column |
| CONFIG_DATE_4 | DATE |  |  |  | New Generic Column |
| CONFIG_DATE_5 | DATE |  |  |  | New Generic Column |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_TO_PRTE_RSN_F_N1 | Non Unique | Default | OIPL_ID |
| BEN_ELIG_TO_PRTE_RSN_F_N2 | Non Unique | Default | PL_ID |
| BEN_ELIG_TO_PRTE_RSN_F_N3 | Non Unique | Default | PGM_ID |
| BEN_ELIG_TO_PRTE_RSN_F_N4 | Non Unique | Default | LER_ID |
| BEN_ELIG_TO_PRTE_RSN_F_N5 | Non Unique | Default | PTIP_ID |
| BEN_ELIG_TO_PRTE_RSN_F_N6 | Non Unique | Default | PLIP_ID |
| BEN_ELIG_TO_PRTE_RSN_F_PK | Unique | Default | ELIG_TO_PRTE_RSN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
