# BEN_PRTT_ENRT_RSLT

BEN_PRTT_ENRT_RSLT identifies the plans or option in plans in which a participant is enrolled, either through explicit election or due to system default/automatic enrollments.  It always identifies a plan and the life event reason ,which, in this context may be an open enrollment, that caused the enrollment.  Where applicable , the elected program and option are identified.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttenrtrslt-9498.html#benprttenrtrslt-9498](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttenrtrslt-9498.html#benprttenrtrslt-9498)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTT_ENRT_RSLT_PK | PRTT_ENRT_RSLT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 | Yes | System generated Primary key PRTT_ENRT_RSLT_ID |  |
| CIR_BENEFIT_ID | NUMBER |  | 18 |  | Benefits Reference id which will be stored in payroll tables |  |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_NUM_6 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_7 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_8 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_9 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_10 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| BENEFIT_RELATION_ID | NUMBER |  | 18 | Yes | This column holds BENEFIT_RELATION_ID |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | This column holds LEGAL_ENTITY_ID |  |
| ENDED_PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds ENDED_PER_IN_LER_ID |  |
| ENDED_CVG_THRU_DT | DATE |  |  |  | This column holds ENDED_CVG_THRU_DT |  |
| ENRT_CVG_STRT_DT | DATE |  |  | Yes | This column holds Enrollment coverage start date. |  |
| PRVS_CVG_STRT_DT | DATE |  |  |  | This column holds PRVS_CVG_STRT_DT |  |
| PRVS_CVG_THRU_DT | DATE |  |  |  | This column holds PRVS_CVG_THRU_DT |  |
| ORGNL_ENRT_DT | DATE |  |  |  | This column holds Original enrollment date. |  |
| ERLST_DEENRT_DT | DATE |  |  |  | This column holds Earliest de-enrollment date. |  |
| ENRT_OVRID_THRU_DT | DATE |  |  |  | This column holds Enrollment override through date. |  |
| ENRT_CVG_THRU_DT | DATE |  |  | Yes | This column holds Enrollment coverage through date. |  |
| ELECTION_DATE | DATE |  |  |  | This column holds ELECTION_DATE |  |
| INTERIM_FLAG | VARCHAR2 | 30 |  |  | This column holds INTERIM_FLAG value |  |
| SSPNDD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Suspended Y or N. |  |
| PRVS_SSPNDD_FLAG | VARCHAR2 | 30 |  |  | This column holds PRVS_SSPNDD_FLAG |  |
| PRTT_IS_CVRD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Participant Is Covered Y or N. |  |
| BNFT_AMT | NUMBER |  |  |  | This column holds Amount value. |  |
| BNFT_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | This column holds Non-monetary unit of measure. |  |
| BNFT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Benefit type. |  |
| UOM | VARCHAR2 | 30 |  |  | This column holds Unit of measure. |  |
| ENRT_MTHD_CD | VARCHAR2 | 30 |  | Yes | This column holds Enrollment method. |  |
| ENRT_OVRIDN_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Enrollment Overriden Y or N. |  |
| ENRT_OVRID_RSN_CD | VARCHAR2 | 30 |  |  | This column holds Enrollment override reason. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to PER_PEOPLE_F. |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | This column holds Foreign Key to PER_ALL_ASSIGNMENTS_F. |  |
| PGM_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PGM_F. |  |
| PL_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to BEN_PL_F. |  |
| OIPL_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_OIPL_F. |  |
| PTIP_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PTIP_F. |  |
| PL_TYP_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PL_TYP_F. |  |
| LER_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to BEN_LER_F. |  |
| PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PER_IN_LER. |  |
| RPLCS_SSPNDD_RSLT_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PRTT_ENRT_RSLT_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to HR_ORGANIZATION_UNITS |  |
| PEN_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
| PEN_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Result Attributes (BEN_PRTT_ENRT_RSLT_DFF) |
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
| NO_LNGR_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | This column holds No Longer Eligible Y or N. |  |
| BNFT_ORDR_NUM | NUMBER |  | 18 |  | This column holds Order number. |  |
| PRTT_ENRT_RSLT_STAT_CD | VARCHAR2 | 30 |  |  | This column holds Participant enrollment result status. |  |
| COMP_LVL_CD | VARCHAR2 | 30 |  |  | This column holds Compensation level. |  |
| PL_ORDR_NUM | NUMBER |  | 18 |  | This column holds Plan order number. |  |
| PLIP_ORDR_NUM | NUMBER |  | 18 |  | This column holds Plan in program order number. |  |
| PTIP_ORDR_NUM | NUMBER |  | 18 |  | This column holds Plan type in program order number. |  |
| OIPL_ORDR_NUM | NUMBER |  | 18 |  | This column holds Option in plan order number. |  |
| OPT_ID | NUMBER |  | 18 |  | This column holds foreign key to OPT_ID |  |
| SVNGS_PLN_FLAG | VARCHAR2 | 30 |  | Yes | This column holds SVNGS_PLN_FLAG |  |
| MISC_PLN_FLAG | VARCHAR2 | 30 |  | Yes | This column holds MISC_PLN_FLAG |  |
| IMPTD_INCM_CALC_CD | VARCHAR2 | 30 |  |  | This column holds IMPTD_INCM_CALC_CD |  |
| ADMIN_CATEGORY_CD | VARCHAR2 | 30 |  |  | This column holds This will be used for page rendering |  |
| SS_CATEGORY_CD | VARCHAR2 | 30 |  |  | This will be used for page rendering |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |  |
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
| TYPE_ID | NUMBER |  | 18 |  | This column is Foreign Key to BEN_TYPES. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRTT_ENRT_RSLT_FK1 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_PRTT_ENRT_RSLT_FK3 | Non Unique | Default | PER_IN_LER_ID |
| BEN_PRTT_ENRT_RSLT_FK5 | Non Unique | Default | ENDED_PER_IN_LER_ID |
| BEN_PRTT_ENRT_RSLT_FK6 | Non Unique | Default | OPT_ID |
| BEN_PRTT_ENRT_RSLT_N1 | Non Unique | Default | PGM_ID |
| BEN_PRTT_ENRT_RSLT_N10 | Non Unique | Default | RPLCS_SSPNDD_RSLT_ID |
| BEN_PRTT_ENRT_RSLT_N2 | Non Unique | Default | PERSON_ID |
| BEN_PRTT_ENRT_RSLT_N3 | Non Unique | Default | PL_ID |
| BEN_PRTT_ENRT_RSLT_N4 | Non Unique | Default | PTIP_ID |
| BEN_PRTT_ENRT_RSLT_N5 | Non Unique | Default | LER_ID |
| BEN_PRTT_ENRT_RSLT_N6 | Non Unique | Default | ASSIGNMENT_ID |
| BEN_PRTT_ENRT_RSLT_N7 | Non Unique | Default | OIPL_ID |
| BEN_PRTT_ENRT_RSLT_N9 | Non Unique | Default | PL_TYP_ID |
| BEN_PRTT_ENRT_RSLT_PK1 | Unique | Default | PRTT_ENRT_RSLT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
