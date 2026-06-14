# BEN_PL_BNF_

BEN_PL_BNF is the person or organization designated by a participant in a plan as the beneficiary of plan benefits.  . For e.g.,  a person may designate his or her spouse as beneficiary of his or her life insurance benefits.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplbnf-28069.html#benplbnf-28069](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplbnf-28069.html#benplbnf-28069)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_BNF_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PL_BNF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_BNF_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PRMRY_CNTNGNT_CD | VARCHAR2 | 30 |  |  | This column holds Primary or contingent beneficiary. |
| PCT_DSGD_NUM | NUMBER |  | 15 |  | This column holds Percent designated. |
| AMT_DSGD_VAL | NUMBER |  |  |  | This column holds Amount designated value. |
| AMT_DSGD_UOM | VARCHAR2 | 30 |  |  | This column holds Amount designated unit of measure. |
| ADDL_INSTRN_TXT | VARCHAR2 | 2000 |  |  | This column holds Additional instructions. |
| DSGN_THRU_DT | DATE |  |  |  | This column holds Designation through date. |
| DSGN_STRT_DT | DATE |  |  |  | This column holds Designation start date. |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_ENRT_RSLT_F. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | This column holds Foreign key to HR_ORGANIZATION_UNITS. |
| BNF_PERSON_ID | NUMBER |  | 18 |  | This column holds Foreign Key to PER_ALL_PEOPLE_F. |
| TTEE_PERSON_ID | NUMBER |  | 18 |  | This column holds Foreign key to PER_PEOPLE_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign Key to HR_ORGANIZATION_UNITS |
| PBN_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| PBN_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBN_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PBN_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_APP_NAME |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_NAME value |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PER_IN_LER. |
| ENDED_PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds ENDED_PER_IN_LER_ID |
| ENDED_CVG_THRU_DT | DATE |  |  |  | This column holds ENDED_CVG_THRU_DT |
| PRVS_CVG_STRT_DT | DATE |  |  |  | This column holds PRVS_CVG_STRT_DT |
| PRVS_CVG_THRU_DT | DATE |  |  |  | This column holds PRVS_CVG_THRU_DT |
| ORGNL_OIPL_DSGN_STRT_DT | DATE |  |  |  | Original Beneficiary Designation Start Date At Option In Plan Level |
| ORGNL_PLAN_DSGN_STRT_DT | DATE |  |  |  | Original Beneficiary Designation Start Date At Plan Level |
| CVRD_FLAG | VARCHAR2 | 30 |  |  | This column holds CVRD_FLAG value |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | This will be used to mark the plan beneficiaries. |
| CVRD_PERCENTAGE | NUMBER |  | 22 |  | This column holds CVRD_PERCENTAGE |
| CVRD_CNTNGT_PERCENTAGE | NUMBER |  | 22 |  | This column holds CVRD_CNTNGT_PERCENTAGE |
| CVRD_AMT | NUMBER |  |  |  | This column holds CVRD_AMT value |
| CVRD_CNTNGT_AMT | NUMBER |  |  |  | This column holds CVRD_CNTNGT_AMT |
| CVRD_PRMRY_CNTNGNT_CD | VARCHAR2 | 30 |  |  | This column holds CVRD_PRMRY_CNTNGNT_CD |
| CTFN_REQD_FLAG | VARCHAR2 | 30 |  |  | To display meaningful messages and provide more information on selection pages |
| RLNSHP_CD | VARCHAR2 | 30 |  |  | This column holds Relationship code |
| ENRT_BNFT_ID | NUMBER |  | 18 |  | Added  to supplement elig_per_per_elctbl_chc_id where there are more than one benefit row associated with a single electable choice. |
| CNTNGT_BNFS_ALWD_FLAG | VARCHAR2 | 120 |  |  | This column holds CNTNGT_BNFS_ALWD_FLAG |
| SUSPEND_FLAG | VARCHAR2 | 30 |  |  | This column holds SUSPEND_FLAG value |
| BNF_OVRD | VARCHAR2 | 20 |  |  | This column indicates  Overridden Y or N. |
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
| INTERIM_PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | This column will store interim Participant enrollment result id |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_BNFN1_ | Non Unique | Default | PL_BNF_ID |
| BEN_PL_BNF_PK1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PL_BNF_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
