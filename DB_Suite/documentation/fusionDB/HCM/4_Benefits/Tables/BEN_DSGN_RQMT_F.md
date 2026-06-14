# BEN_DSGN_RQMT_F

BEN_DSGN_RQMT_F  identifies for a plan, option in plan, or  option, any designation restrictions based on relationship to participant and/or number of dependents or beneficiaries designatable.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendsgnrqmtf-17511.html#bendsgnrqmtf-17511](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendsgnrqmtf-17511.html#bendsgnrqmtf-17511)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DSGN_RQMT_F_PK | DSGN_RQMT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DSGN_RQMT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RLSHP_TYP_CD | VARCHAR2 | 30 |  |  | RLSHP_TYP_CD |
| MN_DPNTS_RQD_NUM | NUMBER |  | 18 |  | Minimum number of required dependents. |
| MX_DPNTS_ALWD_NUM | NUMBER |  | 18 |  | Maximum number of dependents allowed. |
| NO_MN_NUM_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Number Defined Y or N. |
| NO_MX_NUM_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Number Defined Y or N. |
| CVR_ALL_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Cover all eligible Y or N. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| OPT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OPT_F. |
| GRP_RLSHP_CD | VARCHAR2 | 30 |  |  | Group relationship code. |
| DSGN_TYP_CD | VARCHAR2 | 30 |  |  | Designation type. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| DDR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| DDR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DDR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent table discriminator. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_DSGN_RQMT_F_N1 | Non Unique | Default | OIPL_ID |
| BEN_DSGN_RQMT_F_N2 | Non Unique | Default | PL_ID |
| BEN_DSGN_RQMT_F_N3 | Non Unique | Default | OPT_ID |
| BEN_DSGN_RQMT_F_PK | Unique | Default | DSGN_RQMT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
