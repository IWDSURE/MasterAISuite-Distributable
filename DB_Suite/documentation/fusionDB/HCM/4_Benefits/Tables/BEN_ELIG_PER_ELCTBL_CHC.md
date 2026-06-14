# BEN_ELIG_PER_ELCTBL_CHC

BEN_ELIG_PER_ELCTBL_CHC identifies the plans or options in plans a person make elect as the result of a life event with consideration given to any current elections that must remain in force.  It also identifies any possible flexible credit values may be available and any automatic enrollments that were assigned as a result of the life event.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligperelctblchc-9151.html#beneligperelctblchc-9151](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligperelctblchc-9151.html#beneligperelctblchc-9151)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_PER_ELCTBL_CHC_PK | ELIG_PER_ELCTBL_CHC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 |  | Payroll Card Definition Id- Foreign key to  pay_dir_card_definitions |  |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | Payroll Component Definition Id- Foreign key to pay_dir_card_comp_defs_f |  |
| PAYROLL_MAPPING_LEVEL | VARCHAR2 | 30 |  |  | Will determine if Payroll Component Info should be captured at Plan Level or OIPL Level |  |
| CIR_BENEFIT_ID | NUMBER |  | 18 |  | Benefits Reference id which will be stored in payroll tables |  |
| MAPPING_ID | NUMBER |  | 18 |  | Payroll Mapping Id- Foreign key to PAY_GI_MAPPINGS |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_6 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_7 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_8 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_9 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_10 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |  |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Kry to BEN_BENEFIT_RELATIONS_F |  |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | This column indicates Enrollment coverage start date code. |  |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | This column indicates Foreign key to FF_FORMULAS_F. |  |
| ROLL_CRS_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates Roll Credits Y or N. |  |
| CRNTLY_ENRD_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates Currently enrolled Y or N. |  |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates Default Y or N. |  |
| ELCTBL_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates Electable Y or N. |  |
| MNDTRY_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates Mandatory Y or N. |  |
| DPNT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | This column indicates Dependent coverage start date code. |  |
| DPNT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | This column holds Foreign key to FF_FORMULAS_F. |  |
| ENRT_CVG_STRT_DT | DATE |  |  |  | This column indicates Enrollment coverage start date. |  |
| ALWS_DPNT_DSGN_FLAG | VARCHAR2 | 30 |  | Yes | Allows dependent designation Y or N. |  |
| DPNT_DSGN_CD | VARCHAR2 | 30 |  |  | This column indicates Dependent designation code. |  |
| LER_CHG_DPNT_CVG_CD | VARCHAR2 | 30 |  |  | Life event reason change dependent coverage code. |  |
| ERLST_DEENRT_DT | DATE |  |  |  | This column indicates Earliest de-enrollment date. |  |
| PROCG_END_DT | DATE |  |  |  | This column indicates Processing end date. |  |
| COMP_LVL_CD | VARCHAR2 | 30 |  | Yes | This column indicates Compensation level. |  |
| AUTO_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates  Automatically Enroll Y or N. |  |
| CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates Certification required Y or N. |  |
| PL_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PL_F. |  |
| OIPL_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_OIPL_F. |  |
| PGM_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PGM_F. |  |
| PLIP_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PLIP_F. |  |
| PTIP_ID | NUMBER |  | 18 |  | This column holds foreign Key to BEN_PTIP_F. |  |
| PL_TYP_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PL_TYP_F. |  |
| CMBN_PTIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PTIP_F. |  |
| CMBN_PTIP_OPT_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PTIP_OPT_F. |  |
| SPCL_RT_PL_ID | NUMBER |  | 18 |  | This column holds Foreing key to BEN_PL_F. |  |
| SPCL_RT_OIPL_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_OIPL_F. |  |
| MUST_ENRL_ANTHR_PL_ID | NUMBER |  | 18 |  | This column indicates Foreign key to BEN_PL_F. |  |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_ENRT_RSLT_F. |  |
| BNFT_PRVDR_POOL_ID | NUMBER |  | 18 |  | Foreign key to BEN_BNFT_PRVDR_POOL_F. |  |
| PER_IN_LER_ID | NUMBER |  | 18 | Yes | This column indicates holds foreign Key to BEN_PER_IN_LER. |  |
| YR_PERD_ID | NUMBER |  | 18 |  | This column holds Foreing key to BEN_YR_PERD. |  |
| INT_ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | Foreing key to BEN_ELIG_PER_ELCTBL_CHC. |  |
| PIL_ELCTBL_CHC_POPL_ID | NUMBER |  | 18 |  | Foreign key to BEN_PIL_ELCTBL_CHC_POPL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| EPE_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| EPE_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Electable Choice Details Attributes (BEN_ELIG_PER_ELCTBL_CHC_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column indicates PROGRAM_APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column indicates PROGRAM_NAME |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CMBN_PLIP_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_CMBN_PLIP_F. |  |
| OIPLIP_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_OIPLIP_F. |  |
| PL_ORDR_NUM | NUMBER |  | 18 |  | This column indicates Plan order number. |  |
| PLIP_ORDR_NUM | NUMBER |  | 18 |  | This column indicates Plan in program order number. |  |
| PTIP_ORDR_NUM | NUMBER |  | 18 |  | This column indicates Plan type in program order number. |  |
| OIPL_ORDR_NUM | NUMBER |  | 18 |  | This column indicates Option in plan order number. |  |
| IN_PNDG_WKFLOW_FLAG | VARCHAR2 | 30 |  |  | This column indicates Pending work flow Y or N. |  |
| CRYFWD_ELIG_DPNT_CD | VARCHAR2 | 30 |  |  | This column holds Carry forward eligible dependents. |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to per_all_Assignments_f |  |
| COMMENTS | VARCHAR2 | 2000 |  |  | This column holds additional COMMENTS |  |
| ELIG_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates ELIG FLAG |  |
| ELIG_OVRID_DT | DATE |  |  |  | This column indicates ELIG OVRID DT |  |
| ELIG_OVRID_PERSON_ID | NUMBER |  | 18 |  | This column indicates  ELIG OVRID PERSON ID |  |
| INELIG_RSN_CD | VARCHAR2 | 30 |  |  | This column indicates INELIG_RSN_CD |  |
| APPROVAL_STATUS_CD | VARCHAR2 | 30 |  |  | This column indicates Approval Status Code. |  |
| FONM_CVG_STRT_DT | DATE |  |  |  | Processing Date for Coverage and Rates |  |
| ENDED_PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | This column indicates ENDED_PRTT_ENRT_RSLT_ID |  |
| SVNGS_PLN_FLAG | VARCHAR2 | 30 |  |  | This column indicates SVNGS_PLN_FLAG |  |
| MISC_PLN_FLAG | VARCHAR2 | 30 |  |  | This column indicates MISC_PLN_FLAG |  |
| OPT_ID | NUMBER |  | 18 |  | This column holds foreign key to OPT_ID |  |
| IMPTD_INCM_CALC_CD | VARCHAR2 | 30 |  |  | This column indicates IMPTD_INCM_CALC_CD |  |
| BNF_DSGN_CD | VARCHAR2 | 30 |  |  | This column indicates  BNF_DSGN_CD |  |
| CVRD_FLAG | VARCHAR2 | 30 |  |  | ???Y??? when the choice is selected. Need to be carried backward from enrollment results, if default is run and elections are made. This always need to be in sync with enrollment results created for the life event. |  |
| CVRD_ENRT_BNFT_ID | NUMBER |  | 18 |  | This column indicates CVRD_ENRT_BNFT_ID |  |
| INTERIM_ENRT_BNFT_ID | NUMBER |  | 18 |  | This column indicates INTERIM_ENRT_BNFT_ID |  |
| CVRD_PRIMARY_ENRT_RT_ID | NUMBER |  | 18 |  | This column indicates CVRD_PRIMARY_ENRT_RT_ID |  |
| CVRD_SECONDARY_ENRT_RT_ID | NUMBER |  | 18 |  | This column indicates CVRD_SECONDARY_ENRT_RT_ID |  |
| MIN_NUM_DPNT_REQD | NUMBER |  | 18 |  | To display meaningful messages and provide more information on selection pages |  |
| MIN_NUM_BNF_REQD | NUMBER |  | 18 |  | To display meaningful messages and provide more information on selection pages |  |
| ADMIN_CATEGORY_CD | VARCHAR2 | 30 |  |  | This column will be used for page rendering |  |
| SS_CATEGORY_CD | VARCHAR2 | 30 |  |  | This column will be used for page rendering |  |
| PCP_DPNT_DSGN_CD | VARCHAR2 | 30 |  |  | This code will lets know if the pcp designation is required for a dependent or not. |  |
| SUSP_IF_CTFN_NOT_PRVD_FLAG | VARCHAR2 | 30 |  |  | This will be 'Yes' if there is atleast one action item for the choice with suspend flag checked otherwise 'No'. This should be populated as part of choice certification process in benmngle. |  |
| INTERIM_FLAG | VARCHAR2 | 30 |  |  | This column indicates Interim flag |  |
| PCP_DSGN_CD | VARCHAR2 | 30 |  |  | This column indicates PCP Designation Code |  |
| IMP_COMPUTE_CVG_AS_ON_DT_CD | VARCHAR2 | 30 |  |  | This field holds compute coverage as on code of imputed shell plan. |  |
| IMP_COMPUTE_CVG_AS_ON_DT_RL | NUMBER |  | 18 |  | This field holds formula id when compute coverage as on code of imputed shell plan is of formula type. |  |
| IMP_COMPUTE_CVG_AS_ON_DATE | DATE |  |  |  | This field holds evaulated compute coverage as on date of imputed shell plan. |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_TEXT_1 | VARCHAR2 | 4000 |  |  | Template character field for future use. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_ELIG_PER_ELCTBL_CHC_FK1 | Non Unique | Default | BENEFIT_RELATION_ID |  |
| BEN_ELIG_PER_EL_CHC_FK14 | Non Unique | Default | PER_IN_LER_ID | Obsolete |
| BEN_ELIG_PER_EL_CHC_FK15 | Non Unique | Default | YR_PERD_ID |  |
| BEN_ELIG_PER_EL_CHC_FK16 | Non Unique | Default | BUSINESS_GROUP_ID |  |
| BEN_ELIG_PER_EL_CHC_FK17 | Non Unique | Default | PIL_ELCTBL_CHC_POPL_ID |  |
| BEN_ELIG_PER_EL_CHC_FK18 | Non Unique | Default | INT_ELIG_PER_ELCTBL_CHC_ID |  |
| BEN_ELIG_PER_EL_CHC_FK19 | Non Unique | Default | ENDED_PRTT_ENRT_RSLT_ID |  |
| BEN_ELIG_PER_EL_CHC_N11 | Non Unique | Default | MUST_ENRL_ANTHR_PL_ID |  |
| BEN_ELIG_PER_EL_CHC_N12 | Non Unique | Default | SPCL_RT_PL_ID |  |
| BEN_ELIG_PER_EL_CHC_N13 | Non Unique | Default | SPCL_RT_OIPL_ID |  |
| BEN_ELIG_PER_EL_CHC_N14 | Non Unique | Default | BNFT_PRVDR_POOL_ID |  |
| BEN_ELIG_PER_EL_CHC_N15 | Non Unique | Default | CMBN_PTIP_ID |  |
| BEN_ELIG_PER_EL_CHC_N16 | Non Unique | Default | CMBN_PTIP_OPT_ID |  |
| BEN_ELIG_PER_EL_CHC_N17 | Non Unique | Default | CMBN_PLIP_ID |  |
| BEN_ELIG_PER_EL_CHC_N18 | Non Unique | Default | ASSIGNMENT_ID |  |
| BEN_ELIG_PER_EL_CHC_N19 | Non Unique | Default | PL_TYP_ID, PL_ID, OIPL_ID |  |
| BEN_ELIG_PER_EL_CHC_N2 | Non Unique | Default | OIPL_ID |  |
| BEN_ELIG_PER_EL_CHC_N20 | Non Unique | Default | PGM_ID, PER_IN_LER_ID |  |
| BEN_ELIG_PER_EL_CHC_N21 | Non Unique | Default | PER_IN_LER_ID, PL_ID, PGM_ID, OIPL_ID |  |
| BEN_ELIG_PER_EL_CHC_N3 | Non Unique | Default | PGM_ID | Obsolete |
| BEN_ELIG_PER_EL_CHC_N4 | Non Unique | Default | PL_ID, PER_IN_LER_ID |  |
| BEN_ELIG_PER_EL_CHC_N5 | Non Unique | Default | PRTT_ENRT_RSLT_ID |  |
| BEN_ELIG_PER_EL_CHC_N7 | Non Unique | Default | PL_TYP_ID | Obsolete |
| BEN_ELIG_PER_EL_CHC_N8 | Non Unique | Default | PLIP_ID |  |
| BEN_ELIG_PER_EL_CHC_N9 | Non Unique | Default | PTIP_ID |  |
| BEN_ELIG_PER_EL_CHC_PK1 | Unique | Default | ELIG_PER_ELCTBL_CHC_ID |  |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
