# BEN_BENEFIT_RELATIONS_F

BEN_BENEFIT_RELATIONS_F stores benefit relationship details.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbenefitrelationsf-28145.html#benbenefitrelationsf-28145](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbenefitrelationsf-28145.html#benbenefitrelationsf-28145)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BENEFIT_RELATIONS_F_PK | BENEFIT_RELATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| BENEFIT_RELATION_ID | NUMBER |  | 18 | Yes | BENEFIT_RELATION_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BENEFIT_RELATION_NAME | VARCHAR2 | 240 |  | Yes | BENEFIT_RELATION_NAME |  |
| BENEFIT_REL_SYSTEM_CD | VARCHAR2 | 30 |  | Yes | BENEFIT_REL_SYSTEM_CD |  |
| PRIMARY_REL | VARCHAR2 | 30 |  | Yes | PRIMARY_REL |  |
| STATUS | VARCHAR2 | 20 |  | Yes | STATUS |  |
| ORIGINAL_SOURCE | VARCHAR2 | 40 |  |  | ORIGINAL_SOURCE |  |
| UPDATED_SOURCE | VARCHAR2 | 40 |  |  | UPDATED_SOURCE |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | LEGAL_ENTITY_ID |  |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |  |
| REL_PRMRY_ASG_ID | NUMBER |  | 18 |  | REL_PRMRY_ASG_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| BRN_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | BRN_ATTRIBUTE_CATEGORY | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE1 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE2 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE3 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE4 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE5 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE6 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE7 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE8 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE9 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE10 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE11 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE12 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE13 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE14 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE15 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE16 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE17 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE18 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE19 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE20 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE21 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE22 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE23 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE24 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE25 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE26 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE27 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE28 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE29 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | BRN_ATTRIBUTE30 | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| BRN_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Relations Attributes (BEN_BENEFIT_RELATIONS_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BENEFIT_RELATIONS_F_FK1 | Non Unique | Default | PERSON_ID |
| BEN_BENEFIT_RELATIONS_F_FK2 | Non Unique | Default | LEGAL_ENTITY_ID |
| BEN_BENEFIT_RELATIONS_F_FK3 | Non Unique | Default | REL_PRMRY_ASG_ID |
| BEN_BENEFIT_RELATIONS_F_PK | Unique | Default | BENEFIT_RELATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
