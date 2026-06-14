# BEN_PL_TYP_F

BEN_PL_TYP_F categorizes plans according to the type of compensation benefit provided.  A plan can have only one plan type associated with it.  For example, Flex, Medical, Dental, Vision, Employee Group Life Insurance, Disability, Savings, Health Care Flexible Spending Account or dependent Care Flexible Spending Account.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpltypf-18646.html#benpltypf-18646](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpltypf-18646.html#benpltypf-18646)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_TYP_F_PK | PL_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PL_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the plan type. |  |
| MX_ENRL_ALWD_NUM | NUMBER |  | 18 |  | Maximum enrollment allowed in the plan type. |  |
| MN_ENRL_RQD_NUM | NUMBER |  | 18 |  | Minimum enrollment required in the plan type. |  |
| PL_TYP_STAT_CD | VARCHAR2 | 30 |  |  | Plan type status. |  |
| OPT_TYP_CD | VARCHAR2 | 30 |  |  | Option type. |  |
| IVR_IDENT | VARCHAR2 | 90 |  |  | Interactive Voice Response identifier. |  |
| NO_MX_ENRL_NUM_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Enroll Number Defined Y or N. |  |
| NO_MN_ENRL_NUM_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Enroll Number Defined Y or N. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| PTP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| PTP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Type Attributes (BEN_PL_TYP_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| OPT_DSPLY_FMT_CD | VARCHAR2 | 30 |  |  | Option display format. |  |
| COMP_TYP_CD | VARCHAR2 | 30 |  |  | Compensation type. |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code |  |
| SHORT_NAME | VARCHAR2 | 30 |  |  | short Name |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further identifies the legislation of startup data. |  |
| GLOBAL_FLAG | VARCHAR2 | 30 |  |  | Indicates exposure to legal entities. |  |
| SS_CATEGORY_CD | VARCHAR2 | 30 |  |  | This will give the records from BEN_BENEFIT_CATEGORY Table with USAGE_CD = ‘SS’ |  |
| ADMIN_CATEGORY_CD | VARCHAR2 | 30 |  |  | This will give the records from BEN_BENEFIT_CATEGORY Table with USAGE_CD = ‘ADMIN’ |  |
| CARRIER_PLAN_TYPE_NAME | VARCHAR2 | 240 |  |  | Carrier plan type name. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_TYP_F_N1 | Non Unique | Default | NAME |
| BEN_PL_TYP_F_PK | Unique | Default | PL_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
