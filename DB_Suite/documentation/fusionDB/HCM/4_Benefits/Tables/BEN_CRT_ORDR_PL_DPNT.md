# BEN_CRT_ORDR_PL_DPNT

BEN_CRT_ORDR_PL_DPNT identifies the persons who are the beneficiaries of 
orders issued by legislative bodies for a person and a plan or a plan type. 
For example, if a person is required by a legislative action to designate his or her child under a medical plan, the child is the court order covered person.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencrtordrpldpnt-30187.html#bencrtordrpldpnt-30187](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencrtordrpldpnt-30187.html#bencrtordrpldpnt-30187)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CRT_ORDR_PL_DPNT_PK | CRT_ORDR_PL_DPNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CRT_ORDR_PL_DPNT_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ORGANIZATION_UNITS. |
| CONTACT_PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F. |
| CRT_ORDR_ID | NUMBER |  | 18 | Yes | This column indicates Foreign key to BEN_CRT_ORDR_F. |
| PL_TYP_ID | NUMBER |  | 18 |  | This column indicates Foreign key to BEN_PL_TYP_F. |
| PL_ID | NUMBER |  | 18 |  | This column indicates Foreign key to BEN_PL_F. |
| RLSHP_TYP_CD | VARCHAR2 | 30 |  |  | This column indicates Relationship type. |
| ORDR_END_DATE | DATE |  |  |  | This column indicates Court order ending date. |
| ORDR_START_DATE | DATE |  |  |  | This column indicates Court order starting date. |
| PRVNT_DEENRT_FLAG | VARCHAR2 | 30 |  |  | This column indicates Prevent De-Enrollment. |
| CRD_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | This column indicates Descriptive Flexfield structure defining column. |
| CRD_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRD_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| CRD_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_6 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_7 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_8 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_9 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_10 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_6 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_7 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_8 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_9 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_10 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_6 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_7 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_8 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_9 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_10 | DATE |  |  |  | Template date field for future use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CRT_ORDR_PL_DPNT_N1 | Non Unique | Default | CONTACT_PERSON_ID |
| BEN_CRT_ORDR_PL_DPNT_N2 | Non Unique | Default | CRT_ORDR_ID |
| BEN_CRT_ORDR_PL_DPNT_N3 | Non Unique | Default | PL_ID |
| BEN_CRT_ORDR_PL_DPNT_PK | Unique | Default | CRT_ORDR_PL_DPNT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
