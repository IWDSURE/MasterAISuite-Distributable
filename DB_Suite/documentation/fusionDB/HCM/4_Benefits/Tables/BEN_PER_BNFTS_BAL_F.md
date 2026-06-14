# BEN_PER_BNFTS_BAL_F

BEN_PER_BNFTS_BAL_F  identifies the value of a benefits balance for a person.  For example, you may record the previous 30 years of benefits base pay for each participant.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperbnftsbalf-31376.html#benperbnftsbalf-31376](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperbnftsbalf-31376.html#benperbnftsbalf-31376)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_BNFTS_BAL_F_PK | PER_BNFTS_BAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PER_BNFTS_BAL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| VAL | NUMBER |  |  |  | This column holds benefits balance value. |  |
| BNFTS_BAL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BNFTS_BAL_F. |  |
| PERSON_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to PER_ALL_PEOPLE_F. |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | This column indicates the ASSIGNMENT_ID. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This column indicates the LEGAL_ENTITY_ID. |  |
| UOM | VARCHAR2 | 30 |  |  | This column holds unit of measure. |  |
| PBB_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| PBB_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Benefit Balance Attributes (BEN_PER_BNFTS_BAL_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_BNFTS_BAL_F_FK1 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_PER_BNFTS_BAL_F_N1 | Non Unique | Default | BNFTS_BAL_ID |
| BEN_PER_BNFTS_BAL_F_N2 | Non Unique | Default | PERSON_ID |
| BEN_PER_BNFTS_BAL_F_PK | Unique | Default | PER_BNFTS_BAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
