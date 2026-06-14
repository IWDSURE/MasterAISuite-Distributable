# BEN_ELCTBL_CHC_CTFN

BEN_ELCTBL_CHC_CTFN  identifies certifications that may be  required if a person elects to enroll in a plan, option or benefit.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelctblchcctfn-9265.html#benelctblchcctfn-9265](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelctblchcctfn-9265.html#benelctblchcctfn-9265)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELCTBL_CHC_CTFN_PK | ELCTBL_CHC_CTFN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ELCTBL_CHC_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| ENRT_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Enrollment certification type. |  |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |  |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | Foreign key top BEN_ELIG_PER_ELCTBL_CHC_F. |  |
| ENRT_BNFT_ID | NUMBER |  | 18 |  | Foreign key top BEN_ENRT_BNFT_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| ECC_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| ECC_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Choice Certification Attributes (BEN_ELCTBL_CHC_CTFN_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | PROGRAM_APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | PROGRAM_NAME |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SUSP_IF_CTFN_NOT_PRVD_FLAG | VARCHAR2 | 30 |  | Yes | Suspend Enrollment if Certification not provided |  |
| CTFN_DETERMINE_LVL_CD | VARCHAR2 | 30 |  |  | Certificaiton Determination Code.
This can be either PL or OIPL used in determine certification process in enrollment process in benactcm. |  |
| RSTRCTN_TYP_CD | VARCHAR2 | 30 |  |  | BNFT - Coverage Restriction
OPT - Option Sequence based Restriction |  |
| ACTN_TYP_LVL_CD | VARCHAR2 | 30 |  |  | This will be like
ENRTCTFN - Enrollment based
RSTRNCTFN - Restriction based |  |
| CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | Certificaiton Determination Code |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELCTBL_CHC_CTFN_FK2 | Non Unique | Default | ENRT_BNFT_ID |
| BEN_ELCTBL_CHC_CTFN_FK4 | Non Unique | Default | ELIG_PER_ELCTBL_CHC_ID |
| BEN_ELCTBL_CHC_CTFN_PK1 | Unique | Default | ELCTBL_CHC_CTFN_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
