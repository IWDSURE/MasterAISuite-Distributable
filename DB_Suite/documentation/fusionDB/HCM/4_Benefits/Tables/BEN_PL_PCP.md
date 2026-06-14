# BEN_PL_PCP

BEN_PL_PCP identifies all  care provider  limitations specific to each plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplpcp-25435.html#benplpcp-25435](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplpcp-25435.html#benplpcp-25435)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_PCP_PK | PL_PCP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PL_PCP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| PL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| PCP_STRT_DT_CD | VARCHAR2 | 30 |  |  | Primary Care Provider start date code. |  |
| PCP_DSGN_CD | VARCHAR2 | 30 |  |  | Primary Care Provider designation code. |  |
| PCP_DPNT_DSGN_CD | VARCHAR2 | 30 |  |  | Primary Care Provider dependent designation code. |  |
| PCP_RPSTRY_FLAG | VARCHAR2 | 30 |  | Yes | Primary Care Provider Repository Y or N. |  |
| PCP_CAN_KEEP_FLAG | VARCHAR2 | 30 |  | Yes | Primary Care Provider Can Keep Y or N. |  |
| PCP_RADIUS | NUMBER |  |  |  | Primary Care Provider radius. |  |
| PCP_RADIUS_UOM | VARCHAR2 | 30 |  |  | Primary Care Provider radius unit of measure. |  |
| PCP_RADIUS_WARN_FLAG | VARCHAR2 | 30 |  | Yes | Primary Care Provider Radius Warn Y or N. |  |
| PCP_NUM_CHGS | NUMBER |  |  |  | Primary Care Provider number of changes allowed. |  |
| PCP_NUM_CHGS_UOM | VARCHAR2 | 30 |  |  | Primary Care Provider number of changes allowed unit of measure. |  |
| PCP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| PCP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Primary Care Provider Attributes (BEN_PL_PCP_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_PCP_FK1 | Non Unique |  | BUSINESS_GROUP_ID |
| BEN_PL_PCP_N1 | Non Unique |  | PL_ID |
| BEN_PL_PCP_PK | Unique | Default | PL_PCP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
