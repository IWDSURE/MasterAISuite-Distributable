# BEN_DSGN_RQMT_RLSHP_TYP

BEN_DSGN_RQMT_RLSHP_TYP identifies for a desigation  requirement and plan, option in plan, or option, any designation  restrictions based on the designees' relationship to the participant.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendsgnrqmtrlshptyp-7717.html#bendsgnrqmtrlshptyp-7717](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendsgnrqmtrlshptyp-7717.html#bendsgnrqmtrlshptyp-7717)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DSGN_RQMT_RLSHP_TYP_PK | DSGN_RQMT_RLSHP_TYP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DSGN_RQMT_RLSHP_TYP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_DSGN_RQMT_RLSHP_TYP_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| RLSHP_TYP_CD | VARCHAR2 | 30 |  |  | Relationship type. |
| DSGN_RQMT_ID | NUMBER |  | 18 |  | Foreign key to BEN_DSGN_RQMT_F. |
| DRR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| DRR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| DRR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_DSGN_RQMT_RLSHP_TYP_N1 | Non Unique | Default | DSGN_RQMT_ID |
| BEN_DSGN_RQMT_RLSHP_TYP_PK | Unique | Default | DSGN_RQMT_RLSHP_TYP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
