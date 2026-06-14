# BEN_BENFTS_GRP

BEN_BENFTS_GRP identifies a name and description that may be assigned to one or more persons who share common benefits processing characteristics, typically in eligibility or in the variable rates assigned to them.   Using a benefits group can simplify tasks such as determining who is eligible to participate in a plan, or applying contribution rates to a  plan.  . For example, Vision Corporation defines Benefits Group 10 to categorize employees with lengths of service greater than five years in a particular subsidiary that Vision Corporation recently acquired.  Only these employees are eligible for the Company Car plan that Vision has discontinued for the rest of its employees. In another example, Vision Corporation defines Benefits Group 1 to categorize employees who are 61 to 65 years of age. A special contribution rate for Vision Corporation's self-insured Live Long Life Insurance plan applies to Benefits Group.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbenftsgrp-3302.html#benbenftsgrp-3302](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbenftsgrp-3302.html#benbenftsgrp-3302)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BENFTS_GRP_PK | BENFTS_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| BENFTS_GRP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENFTS_GRP_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the benefits group. |  |
| BNG_DESC | VARCHAR2 | 240 |  |  | Benefits group description. |  |
| BNG_ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield structure defining column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| BNG_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Group Attributes (BEN_BENFTS_GRP_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Entity Id |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BENFTS_GRP_PK | Unique | Default | BENFTS_GRP_ID |
| BEN_BNFTS_GRP_U1 | Unique | Default | NAME, BUSINESS_GROUP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
