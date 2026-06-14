# BEN_ELIG_DPNT

BEN_ELIG_DPNT identifies the eligibility status of a person's contacts who have the personal relationship flag selected.  This information is updated when an electable choice is created for a person or when the determine dependent eligibility process is run.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligdpnt-19881.html#beneligdpnt-19881](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligdpnt-19881.html#beneligdpnt-19881)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_DPNT_PK | ELIG_DPNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| DPNT_INELIG_FLAG | VARCHAR2 | 30 |  | Yes | Dependent ineligible flag Y or N. |  |
| CVRD_FLAG | VARCHAR2 | 30 |  |  | 'Y' When user covers the dependent |  |
| RLNSHP_CD | VARCHAR2 | 30 |  |  | This column indicates RLNSHP_CD |  |
| ELIG_DPNT_ID | NUMBER |  | 18 | Yes | System generated primary key column |  |
| CREATE_DT | DATE |  |  | Yes | This column indicates Created date. |  |
| ELIG_STRT_DT | DATE |  |  |  | This column indicates Eligibility start date. |  |
| ELIG_THRU_DT | DATE |  |  |  | This column indicates Eligibility through date. |  |
| OVRDN_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates Overridden Y or N. |  |
| OVRDN_THRU_DT | DATE |  |  |  | This column indicates Overridden through date. |  |
| INELG_RSN_CD | VARCHAR2 | 30 |  |  | This column indicates Ineligible reason. |  |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_PER_ELCTBL_CHC. |  |
| PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PER_IN_LER. |  |
| ELIG_PER_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_ELIG_PER_F. |  |
| ELIG_PER_OPT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_PER_OPT_F. |  |
| ELIG_CVRD_DPNT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELG_CVRD_DPNT. |  |
| DPNT_PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| EGD_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| EGD_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Eligible Dependent Attributes (BEN_ELIG_DPNT_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column indicates PROGRAM_APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 20 |  |  | This column indicates PROGRAM_NAME |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ENDED_ELIG_CVRD_DPNT_ID | NUMBER |  | 18 |  | This column indicates ENDED_ELIG_CVRD_DPNT_ID |  |
| CTFN_REQD_FLAG | VARCHAR2 | 30 |  |  | To display meaningful messages and provide more information on selection pages |  |
| PCP_DSGN_CD | VARCHAR2 | 30 |  |  | This column indicates PCP  code |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_DPNT_FK4 | Non Unique | Default | ELIG_PER_ELCTBL_CHC_ID |
| BEN_ELIG_DPNT_FK5 | Non Unique | Default | PER_IN_LER_ID |
| BEN_ELIG_DPNT_FK6 | Non Unique | Default | BUSINESS_GROUP_ID |
| BEN_ELIG_DPNT_N1 | Non Unique | Default | ELIG_PER_OPT_ID |
| BEN_ELIG_DPNT_N2 | Non Unique | Default | ELIG_PER_ID |
| BEN_ELIG_DPNT_N3 | Non Unique | Default | ELIG_CVRD_DPNT_ID |
| BEN_ELIG_DPNT_N4 | Non Unique | Default | DPNT_PERSON_ID |
| BEN_ELIG_DPNT_PK1 | Unique | Default | ELIG_DPNT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
