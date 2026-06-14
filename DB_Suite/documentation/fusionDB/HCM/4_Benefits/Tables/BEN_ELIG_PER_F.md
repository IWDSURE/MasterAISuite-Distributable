# BEN_ELIG_PER_F

BEN_ELIG_PER_F captures information about persons found eligible, and in some cases ineligible, for a program or plan.  Typically, being eligible to participate means that the person can make an election or be enrolled, however, there are some circumstances where enrollment is not appropriate for a plan  and being eligible does not mean that the participant can enroll at the same time as when they are eligible.  The broadest definition of participation eligibility is that the person satisfies the plan defined criteria for receiving benefits from the plan at some time.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligperf-14270.html#beneligperf-14270](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligperf-14270.html#beneligperf-14270)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_PER_F_PK | ELIG_PER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ELIG_PER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| DPNT_OTHR_PL_CVRD_RL_FLAG | VARCHAR2 | 30 |  | Yes | Dependent covered in other plan rule Y or N. |  |
| PRTN_OVRIDN_THRU_DT | DATE |  |  |  | Participation overriden through date. |  |
| PL_KEY_EE_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Plan Key Employee Y or N. |  |
| PL_HGHLY_COMPD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Plan Highly Compensated Y or N. |  |
| ELIG_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Eligible Y or N. |  |
| COMP_REF_AMT | NUMBER |  |  |  | Eligible compensation reference amount. |  |
| CMBN_AGE_N_LOS_VAL | NUMBER |  |  |  | Eligible combined age and length of service value. |  |
| COMP_REF_UOM | VARCHAR2 | 30 |  |  | Eligible compensation reference unit of measure. |  |
| AGE_VAL | NUMBER |  |  |  | This column holds Eligible age value. |  |
| LOS_VAL | NUMBER |  |  |  | This column holds Eligible length of service value. |  |
| PRTN_END_DT | DATE |  |  |  | This column holds Participation end date. |  |
| PRTN_STRT_DT | DATE |  |  |  | This column holds Participation start date. |  |
| WV_CTFN_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Waive certification type. |  |
| HRS_WKD_VAL | NUMBER |  |  |  | This column holds Eligible hours worked. |  |
| HRS_WKD_BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | This column holds Eligible hours worked boundary period. |  |
| PRTN_OVRIDN_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Participation Overriden Y or N. |  |
| NO_MX_PRTN_OVRID_THRU_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Participation Override Through Y or N. |  |
| PRTN_OVRIDN_RSN_CD | VARCHAR2 | 30 |  |  | This column holds Participation override reason. |  |
| AGE_UOM | VARCHAR2 | 30 |  |  | This column holds Eligible age unit of measure. |  |
| LOS_UOM | VARCHAR2 | 30 |  |  | Eligible length of service unit of measure. |  |
| OVRID_SVC_DT | DATE |  |  |  | This column holds Override service date. |  |
| FRZ_LOS_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Freeze Length of Service Y or N. |  |
| FRZ_AGE_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Freeze Age Y or N. |  |
| FRZ_CMP_LVL_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Freeze Compensation Level Y or N. |  |
| FRZ_PCT_FL_TM_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Freeze Percent Full Time Y or N. |  |
| FRZ_HRS_WKD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Freeze Hours Worked Y or N. |  |
| FRZ_COMB_AGE_AND_LOS_FLAG | VARCHAR2 | 30 |  | Yes | Freeze Combination Age And Length of Service Y or N. |  |
| DSTR_RSTCN_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Distribution restriction Y or N. |  |
| PCT_FL_TM_VAL | NUMBER |  |  |  | This column holds Eligible percent full time value. |  |
| WV_PRTN_RSN_CD | VARCHAR2 | 30 |  |  | This column holds Waive participation reason. |  |
| PL_WVD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Plan Waived Y or N. |  |
| PL_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PL_F. |  |
| PGM_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PGM_F. |  |
| LER_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_LER_F. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to PER_PEOPLE_F. |  |
| MUST_ENRL_ANTHR_PL_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| PEP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| PEP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Plan Attributes (BEN_ELIG_PER_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column holds Populated with FND_GLOBAL_PROG.APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | Concurrent Program Name -- Name of the concurrent program that last updated this row ( Populated with  FND_GLOBAL_CONC.PROGRAM_NAME). |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| RT_COMP_REF_AMT | NUMBER |  |  |  | This column holds Rate compensation reference amount. |  |
| RT_CMBN_AGE_N_LOS_VAL | NUMBER |  |  |  | Rate combination age and length of service value. |  |
| RT_COMP_REF_UOM | VARCHAR2 | 30 |  |  | Rate compensation reference unit of measure. |  |
| RT_AGE_VAL | NUMBER |  |  |  | This column holds Rate age value. |  |
| RT_LOS_VAL | NUMBER |  |  |  | This column holds Rate length of service value. |  |
| RT_HRS_WKD_VAL | NUMBER |  |  |  | This column holds Rate hours worked value. |  |
| RT_HRS_WKD_BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | This column holds Rate hours worked boundary period. |  |
| RT_AGE_UOM | VARCHAR2 | 30 |  |  | This column holds Rate age unit of measure. |  |
| RT_LOS_UOM | VARCHAR2 | 30 |  |  | This column holds Rate length of service unit of measure. |  |
| RT_PCT_FL_TM_VAL | NUMBER |  |  |  | This column holds Rate percent full time value. |  |
| RT_FRZ_LOS_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Rate Freeze Length of Service Y or N. |  |
| RT_FRZ_AGE_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Rate Freeze Age Y or N. |  |
| RT_FRZ_CMP_LVL_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Rate Freeze Compensation Level Y or N. |  |
| RT_FRZ_PCT_FL_TM_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Rate Freeze Percent Full Time Y or N. |  |
| RT_FRZ_HRS_WKD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Rate Freeze Hours Worked Y or N. |  |
| RT_FRZ_COMB_AGE_AND_LOS_FLAG | VARCHAR2 | 30 |  | Yes | Rate Freeze Combination Age And Length of Service Y or N. |  |
| INELG_RSN_CD | VARCHAR2 | 30 |  |  | This column holds Ineligible reason. |  |
| ONCE_R_CNTUG_CD | VARCHAR2 | 30 |  |  | This column holds Once or continuing. |  |
| WAIT_PERD_CMPLTN_DT | DATE |  |  |  | This column holds Waiting period completion date. |  |
| PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PER_IN_LER. |  |
| PLIP_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PLIP_F. |  |
| PTIP_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PTIP_F. |  |
| PL_ORDR_NUM | NUMBER |  | 18 |  | This column holds Plan order number. |  |
| PLIP_ORDR_NUM | NUMBER |  | 18 |  | This column holds Plan in program order number. |  |
| PTIP_ORDR_NUM | NUMBER |  | 18 |  | This column holds Plan type in program order number. |  |
| WAIT_PERD_STRT_DT | DATE |  |  |  | This column holds Waiting Period Start Date |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_ELIG_PER_F_FK1 | Non Unique | Default | BUSINESS_GROUP_ID |  |
| BEN_ELIG_PER_F_FK2 | Non Unique | Default | BENEFIT_RELATION_ID |  |
| BEN_ELIG_PER_F_FK6 | Non Unique | Default | PER_IN_LER_ID |  |
| BEN_ELIG_PER_F_N1 | Non Unique | Default | PL_ID |  |
| BEN_ELIG_PER_F_N2 | Non Unique | Default | PLIP_ID |  |
| BEN_ELIG_PER_F_N3 | Non Unique | Default | PERSON_ID | Obsolete |
| BEN_ELIG_PER_F_N4 | Non Unique | Default | PGM_ID |  |
| BEN_ELIG_PER_F_N5 | Non Unique | Default | PTIP_ID |  |
| BEN_ELIG_PER_F_N6 | Non Unique | Default | LER_ID |  |
| BEN_ELIG_PER_F_N7 | Non Unique | Default | MUST_ENRL_ANTHR_PL_ID |  |
| BEN_ELIG_PER_F_N8 | Non Unique | Default | PERSON_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, PL_ID |  |
| BEN_ELIG_PER_F_PK | Unique | Default | ELIG_PER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
