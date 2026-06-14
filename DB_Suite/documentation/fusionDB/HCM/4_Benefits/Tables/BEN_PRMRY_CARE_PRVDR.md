# BEN_PRMRY_CARE_PRVDR

BEN_PRMRY_CARE_PRVDR identifies the care providers, physicians, and chiropractors, for a participant enrolled in a plan or option in plan or for a dependent covered by a participant.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprmrycareprvdr-24434.html#benprmrycareprvdr-24434](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprmrycareprvdr-24434.html#benprmrycareprvdr-24434)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRMRY_CARE_PRVDR_PK | PRMRY_CARE_PRVDR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PRMRY_CARE_PRVDR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| PRMRY_CARE_PRVDR_TYP_CD | VARCHAR2 | 30 |  | Yes | This column holds Primary Care Provider type. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the Primary Care Provider. |  |
| EXT_IDENT | VARCHAR2 | 90 |  |  | This column holds External identifier. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| ELIG_CVRD_DPNT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_CVRD_DPNT_F. |  |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_ENRT_RSLT_F. |  |
| ENDED_PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PER_IN_LER. |  |
| ENDED_CVG_THRU_DT | DATE |  |  |  | This column holds Ended coverage through date. |  |
| PRVS_CVG_STRT_DT | DATE |  |  |  | This column holds Previous coverage start date. |  |
| PRVS_CVG_THRU_DT | DATE |  |  |  | Previous coverage through date. |  |
| CVG_STRT_DT | DATE |  |  |  | This column holds Coverage start date. |  |
| CVG_THRU_DT | DATE |  |  |  | This column holds Coverage through date. |  |
| PPR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| PPR_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Primary Care Provider Attributes (BEN_PRMRY_CARE_PRVDR_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CVRD_FLAG | VARCHAR2 | 30 |  |  | This column holds Covered Y or N. |  |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | Associate with EPE as part of selection. |  |
| ELIG_DPNT_ID | NUMBER |  | 18 |  | Associate with elig dependents as part of selection. |  |
| PCP_NUMBER | VARCHAR2 | 400 |  |  | This column holds the primary care provider number. |  |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRMRY_CARE_PRVDR_FK2 | Non Unique | Default | ELIG_PER_ELCTBL_CHC_ID |
| BEN_PRMRY_CARE_PRVDR_FK3 | Non Unique | Default | ELIG_DPNT_ID |
| BEN_PRMRY_CARE_PRVDR_N1 | Non Unique | Default | ELIG_CVRD_DPNT_ID |
| BEN_PRMRY_CARE_PRVDR_N2 | Non Unique | Default | PRTT_ENRT_RSLT_ID |
| BEN_PRMRY_CARE_PRVDR_PK1 | Unique | Default | PRMRY_CARE_PRVDR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
