# BEN_ELIGY_PRFL

BEN_ELIGY_PRFL_F  identifies one or more fixed eligibility factors or rules which collectively define a profile of eligibility which must be satisfied in order for a person to be found eligible for a compensation  object. Profiles are provided so that those compensation objects  which have the same eligibility requirements may share one definition, as opposed to requiring the user to maintain redundant definitions. Eligibility profile criteria are compared to the criteria for a person to  determine whether the person is eligible to participate in a compensation object.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligyprfl-24836.html#beneligyprfl-24836](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligyprfl-24836.html#beneligyprfl-24836)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIGY_PRFL_PK | ELIGY_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | System generated Primary key column. |  |
| START_DATE | DATE |  |  |  | Start date. |  |
| END_DATE | DATE |  |  |  | End date. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the eligibility profile. |  |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description. |  |
| STAT_CD | VARCHAR2 | 30 |  | Yes | Eligibility profile status. |  |
| PROFILE_TYPE | VARCHAR2 | 15 |  |  | PROFILE_TYPE |  |
| REGN_ID | NUMBER |  | 18 |  | REGN_ID |  |
| DPNT_CVG_ELIG_DET_RL | NUMBER |  | 18 |  | DPNT_CVG_ELIG_DET_RL |  |
| DPNT_STUD_FLAG | VARCHAR2 | 30 |  |  | DPNT_STUD_FLAG |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| ELP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| ELP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligibility Profile Attributes (BEN_ELIGY_PRFL_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ASG_TYP_CD | VARCHAR2 | 30 |  |  | Assignment type. |  |
| ASMT_TO_USE_CD | VARCHAR2 | 30 |  |  | Assignment to use. |  |
| ELIG_ENRLD_PLIP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Enrolled Plan in Program Y or N. |  |
| ELIG_CBR_QUALD_BNF_FLAG | VARCHAR2 | 30 |  | Yes | Eligible COBRA Qualified Beneficiary Y or N. |  |
| ELIG_ENRLD_PTIP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Enrolled Plan Type in Program Y or N. |  |
| ELIG_DPNT_CVRD_PLIP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Dependent Covered Plan in Program Y or N. |  |
| ELIG_DPNT_CVRD_PTIP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Dependent Covered Plan Type in Program Y or N. |  |
| ELIG_DPNT_CVRD_PGM_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Dependent Covered Program Y or N. |  |
| ELIG_JOB_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Job Y or N. |  |
| ELIG_HRLY_SLRD_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Hourly Salaried Y or N. |  |
| ELIG_PSTL_CD_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Postal Code Y or N. |  |
| ELIG_LBR_MMBR_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Labor Member Y or N. |  |
| ELIG_LGL_ENTY_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Legal Entity Y or N. |  |
| ELIG_BENFTS_GRP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Benefits Group Y or N. |  |
| ELIG_WK_LOC_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Work Location Y or N. |  |
| ELIG_BRGNG_UNIT_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Bargaining Unit Y or N. |  |
| ELIG_AGE_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Age Y or N. |  |
| ELIG_LOS_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Length of Service Y or N. |  |
| ELIG_PER_TYP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Person Type Y or N. |  |
| ELIG_FL_TM_PT_TM_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Full Time Plan Type Time Y or N. |  |
| ELIG_EE_STAT_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Employee Status Y or N. |  |
| ELIG_GRD_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Grade Y or N. |  |
| ELIG_PCT_FL_TM_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Percent Full Time Y or N. |  |
| ELIG_ASNT_SET_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Assignment Set Y or N. |  |
| ELIG_HRS_WKD_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Hours Worked Y or N. |  |
| ELIG_COMP_LVL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Compensation Level Y or N. |  |
| ELIG_ORG_UNIT_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Organization Unit Y or N. |  |
| ELIG_LOA_RSN_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Leave of Absence Reason Y or N. |  |
| ELIG_PYRL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Payroll Y or N. |  |
| ELIG_SCHEDD_HRS_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Scheduled Hours Y or N. |  |
| ELIG_PY_BSS_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Pay Basis Y or N. |  |
| ELIGY_PRFL_RL_FLAG | VARCHAR2 | 30 |  | Yes | Eligibility Profile Rule Y or N. |  |
| ELIG_CMBN_AGE_LOS_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Combination Age Length of Service Y or N. |  |
| CNTNG_PRTN_ELIG_PRFL_FLAG | VARCHAR2 | 30 |  | Yes | Continuing participation Eligibility Y or N. |  |
| ELIG_PRTT_PL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Participant Plan Y or N. |  |
| ELIG_PPL_GRP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible People Group Y or N. |  |
| ELIG_SVC_AREA_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Service Area Y or N. |  |
| ELIG_PTIP_PRTE_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Plan Type in Program Participate Y or N. |  |
| ELIG_NO_OTHR_CVG_FLAG | VARCHAR2 | 30 |  | Yes | Eligible No Other Coverage Y or N. |  |
| ELIG_ENRLD_PL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Enrolled Plan Y or N. |  |
| ELIG_ENRLD_OIPL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Enrolled Option in Plan Y or N. |  |
| ELIG_ENRLD_PGM_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Enrolled Program Y or N. |  |
| ELIG_DPNT_CVRD_PL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Dependent Covered Plan Y or N. |  |
| ELIG_LVG_RSN_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Leaving Reason Y or N. |  |
| ELIG_OPTD_MDCR_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Opted Medicare Y or N. |  |
| ELIG_DPNT_OTHR_PTIP_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Dependent Other Plan Type in Program Y or N. |  |
| ELIG_TBCO_USE_FLAG | VARCHAR2 | 30 |  | Yes | Eligible Tobacco Use Y or N. |  |
| ELIG_GNDR_FLAG | VARCHAR2 | 30 |  | Yes | Eligible gender Y or N. |  |
| ELIG_DSBLTY_CTG_FLAG | VARCHAR2 | 30 |  | Yes | Eligible disability Y or N. |  |
| ELIG_DSBLTY_DGR_FLAG | VARCHAR2 | 30 |  | Yes | Eligible disability degree Y or N. |  |
| ELIG_DSBLTY_RSN_FLAG | VARCHAR2 | 30 |  | Yes | Eligible disability reason Y or N. |  |
| ELIG_MRTL_STS_FLAG | VARCHAR2 | 30 |  | Yes | Eligible marital status Y or N. |  |
| ELIG_PRBTN_PERD_FLAG | VARCHAR2 | 30 |  | Yes | Eligible probation period Y or N. |  |
| ELIG_SP_CLNG_PRG_PT_FLAG | VARCHAR2 | 30 |  | Yes | Eligible spinal point progression Y or N. |  |
| ELIG_SUPPL_ROLE_FLAG | VARCHAR2 | 30 |  | Yes | Eligible supplemental role Y or N. |  |
| ELIG_QUAL_TITL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible qualified title Y or N. |  |
| ELIG_PSTN_FLAG | VARCHAR2 | 30 |  | Yes | Elible position Y or N. |  |
| BNFT_CAGR_PRTN_CD | VARCHAR2 | 30 |  | Yes | Collective agreement participation. |  |
| ELIG_DSBLD_FLAG | VARCHAR2 | 30 |  | Yes | Eligible disability Y or N. |  |
| ELIG_TTL_CVG_VOL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible total coverage Y or N. |  |
| ELIG_TTL_PRTT_FLAG | VARCHAR2 | 30 |  | Yes | Eligible total particiation Y or N. |  |
| ELIG_COMPTNCY_FLAG | VARCHAR2 | 30 |  | Yes | Eligible competency Y or N. |  |
| ELIG_HLTH_CVG_FLAG | VARCHAR2 | 30 |  | Yes | Eligible health coverage Y or N. |  |
| ELIG_ANTHR_PL_FLAG | VARCHAR2 | 30 |  | Yes | Eligible another plan Y or N. |  |
| ELIG_PERF_RTNG_FLAG | VARCHAR2 | 30 |  | Yes | Eligible performance rating Y or N. |  |
| ELIG_QUA_IN_GR_FLAG | VARCHAR2 | 30 |  | Yes | Eligible quartile in grade Y or N. |  |
| ELIG_CRIT_VALUES_FLAG | VARCHAR2 | 30 |  | Yes | Eligible User Defined Criteria Y or N |  |
| DPNT_RLSHP_FLAG | VARCHAR2 | 30 |  |  | Dependent Relationship flag |  |
| DPNT_DSGNT_CRNTLY_ENRLD_FLAG | VARCHAR2 | 30 |  |  | Dependent ... currently enrolled flag |  |
| DPNT_CVRD_IN_ANTHR_PL_FLAG | VARCHAR2 | 30 |  |  | Dependent covered in another plan flag |  |
| DPNT_MLTRY_FLAG | VARCHAR2 | 30 |  |  | Dependent Military flag |  |
| ELIG_JOBFUNC_FLAG | VARCHAR2 | 30 |  |  | Eligibile Job Function Flag Y/N |  |
| ELIG_JOBFAM_FLAG | VARCHAR2 | 30 |  |  | Eligibile Job Family Flag Y/N |  |
| ELIG_MGR_FLAG | VARCHAR2 | 30 |  |  | Eligibile Manager Flag Y/N |  |
| ELIG_BU_FLAG | VARCHAR2 | 30 |  |  | Eligibile Business Unit Flag Y/N |  |
| ELIG_HIREDT_FLAG | VARCHAR2 | 30 |  |  | Eligibile Hire date flag Y/N |  |
| ELIG_RELIGION_FLAG | VARCHAR2 | 30 |  |  | Religion Flag Y/N |  |
| ELIG_GEO_FLAG | VARCHAR2 | 30 |  |  | City/State Flag Y/N |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIGY_PRFL_PK | Unique | Default | ELIGY_PRFL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
