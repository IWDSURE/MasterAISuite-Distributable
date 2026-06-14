# BEN_BNFTS_BAL_F

BEN_BENFTS_BAL_F  identifies a name and unit of measure for balance type  information which is not readily derivable from information contained in  the system or which may be provided by a third party agent, such as an outside payroll, timekeeping system, participant recordkeeper or an actuary.   For example, hours worked or compensation history. . You may associate a benefits balance with a person and then record  the value for that person.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftsbalf-17587.html#benbnftsbalf-17587](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftsbalf-17587.html#benbnftsbalf-17587)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BNFTS_BAL_F_PK | BNFTS_BAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| BNFTS_BAL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  |  | Name of the benefits balance. |  |
| BNFTS_BAL_USG_CD | VARCHAR2 | 30 |  |  | Balance usage. |  |
| BNFTS_BAL_DESC | VARCHAR2 | 240 |  |  | Balance description. |  |
| UOM | VARCHAR2 | 30 |  |  | Unit of measure. |  |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Non-monentary unit of measure. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |  |
| STATUS | VARCHAR2 | 20 |  |  | STATUS |  |
| BNB_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| BNB_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Benefit Balance Attributes (BEN_BNFTS_BAL_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BNFTS_BAL_F_N1 | Non Unique |  | NAME |
| BEN_BNFTS_BAL_F_PK | Unique | Default | BNFTS_BAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
