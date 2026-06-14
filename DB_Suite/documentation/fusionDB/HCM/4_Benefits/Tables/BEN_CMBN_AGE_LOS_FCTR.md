# BEN_CMBN_AGE_LOS_FCTR

BEN_CMBN_AGE_LOS_FCTR  identifies how to calculate a person's combined age and length of service for such  purposes as determining eligibility and calculating rates, in those  cases when combined age and length of service is a factor, such  as reductions in force where a person qualifies for severence  benefits if he or she has a combination of 75 points,for example,. is 50 years  old and has 25 years of service.  In addition it identifies a range  of combined ages and lengths-of-service,  again for eligibility and  rate purposes.  It is an intersection of BEN_AGE_FCTR  and BEN_LOS_FCTR.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencmbnagelosfctr-25147.html#bencmbnagelosfctr-25147](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencmbnagelosfctr-25147.html#bencmbnagelosfctr-25147)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CMBN_AGE_LOS_FCTR_PK | CMBN_AGE_LOS_FCTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| CMBN_AGE_LOS_FCTR_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_CMBN_AGE_LOS_FCTR_F. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the combination age and length of service factor. |  |
| LOS_FCTR_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_LOS_FCTR_F. |  |
| AGE_FCTR_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_AGE_FCTR_F. |  |
| CMBND_MIN_VAL | NUMBER |  |  |  | Combined minimum value. |  |
| CMBND_MAX_VAL | NUMBER |  |  |  | Combined maximum value. |  |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| CLA_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| CLA_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age and Length Of Service Attributes (BEN_CMBN_AGE_LOS_FCTR_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CMBN_AGE_LOS_FCTR_FK4 | Non Unique | Default | LOS_FCTR_ID |
| BEN_CMBN_AGE_LOS_FCTR_FK5 | Non Unique | Default | AGE_FCTR_ID |
| BEN_CMBN_AGE_LOS_FCTR_N1 | Non Unique | Default | NAME |
| BEN_CMBN_AGE_LOS_FCTR_PK1 | Unique | Default | CMBN_AGE_LOS_FCTR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
