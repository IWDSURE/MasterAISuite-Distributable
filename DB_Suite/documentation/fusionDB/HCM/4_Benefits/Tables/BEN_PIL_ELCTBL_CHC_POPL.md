# BEN_PIL_ELCTBL_CHC_POPL

BEN_PIL_ELCTBL_CHC_POPL identifies the persons and the programs or plans not in program for which they have electable choices as a result of a life event.  It contains information such as  the enrollment period start and end dates, default assigned date and theelections made date.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpilelctblchcpopl-16527.html#benpilelctblchcpopl-16527](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpilelctblchcpopl-16527.html#benpilelctblchcpopl-16527)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PIL_ELCTBL_CHC_POPL_PK | PIL_ELCTBL_CHC_POPL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PIL_ELCTBL_CHC_POPL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| DFLT_ENRT_DT | DATE |  |  |  | This column holds Default enrollment date. |  |
| DFLT_ASND_DT | DATE |  |  |  | This column holds Default assigned date. |  |
| ELCNS_MADE_DT | DATE |  |  |  | This column holds Elections made date. |  |
| CLS_ENRT_DT_TO_USE_CD | VARCHAR2 | 30 |  |  | Close enrollment date to use code. |  |
| ENRT_TYP_CYCL_CD | VARCHAR2 | 30 |  |  | This column holds Enrollment type cycle. |  |
| ENRT_PERD_END_DT | DATE |  |  |  | This column holds Enrollment period end date. |  |
| ENRT_PERD_STRT_DT | DATE |  |  |  | This column holds Enrollment period start date. |  |
| PROCG_END_DT | DATE |  |  |  | This column holds Processing end date. |  |
| PIL_ELCTBL_POPL_STAT_CD | VARCHAR2 | 30 |  |  | Person in life event electable program or plan status. |  |
| ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | This column holds Activity reference period. |  |
| UOM | VARCHAR2 | 30 |  |  | This column holds Unit of measure. |  |
| AUTO_ASND_DT | DATE |  |  |  | This column holds Automatically assigned date. |  |
| LEE_RSN_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_LEE_RSN_F. |  |
| ENRT_PERD_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_ENRT_PERD. |  |
| PER_IN_LER_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to BEN_PER_IN_LER. |  |
| PGM_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PGM_F. |  |
| PL_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| PEL_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| PEL_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Attributes (BEN_PIL_ELCTBL_CHC_POPL_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_NAME value |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CBR_ELIG_PERD_STRT_DT | DATE |  |  |  | Cobra eligibility period start date. |  |
| CBR_ELIG_PERD_END_DT | DATE |  |  |  | Cobra eligibility period end date. |  |
| BDGT_ACC_CD | VARCHAR2 | 30 |  |  | This column holds BDGT_ACC_CD value |  |
| POP_CD | VARCHAR2 | 30 |  |  | This column holds value of POP_CD |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | This column holds Assignment Id |  |
| REINSTATE_CD | VARCHAR2 | 30 |  |  | This column holds Reinstate Code |  |
| REINSTATE_OVRDN_CD | VARCHAR2 | 30 |  |  | This column holds Reinstate Override Code |  |
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
| CONFIG_ID_3 | DATE |  |  |  | Template ID field for future use. |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_TEXT_1 | VARCHAR2 | 4000 |  |  | Template character field for future use. |  |
| SIGNATURE | CLOB |  |  |  | This column holds the hex equivalent of the signature. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PIL_ELCTBL_CHC_POPL_FK4 | Non Unique | Default | ENRT_PERD_ID |
| BEN_PIL_ELCTBL_CHC_POPL_FK5 | Non Unique | Default | PER_IN_LER_ID |
| BEN_PIL_ELCTBL_CHC_POPL_N1 | Non Unique | Default | LEE_RSN_ID |
| BEN_PIL_ELCTBL_CHC_POPL_N2 | Non Unique | Default | PL_ID |
| BEN_PIL_ELCTBL_CHC_POPL_N3 | Non Unique | Default | PGM_ID |
| BEN_PIL_ELCTBL_CHC_POPL_PK1 | Unique | Default | PIL_ELCTBL_CHC_POPL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
