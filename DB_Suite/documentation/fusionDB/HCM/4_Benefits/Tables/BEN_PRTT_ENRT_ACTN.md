# BEN_PRTT_ENRT_ACTN

BEN_PRTT_ENRT_ACTN identifies any outstanding enrollment action required of a person in order for elections or life events to be unsuspended or, at a minimum, considered complete.  For example, participants must provided evidence of good health if they are to enrolled in a group term life insurance policy at a high coverage volume.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttenrtactn-11396.html#benprttenrtactn-11396](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttenrtactn-11396.html#benprttenrtactn-11396)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTT_ENRT_ACTN_PK | PRTT_ENRT_ACTN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PRTT_ENRT_ACTN_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PRTT_ENRT_ACTN_F. |  |
| CMPLTD_DT | DATE |  |  |  | Completed date. |  |
| DUE_DT | DATE |  |  |  | Due date. |  |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |  |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PRTT_ENRT_RSLT_F. |  |
| ACTN_TYP_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTN_TYP_F. |  |
| ELIG_CVRD_DPNT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_CVRD_DPNT_F. |  |
| ENDED_PER_IN_LER_ID | NUMBER |  | 18 |  | Life Event Identifier |  |
| PL_BNF_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_BNF_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| PEA_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| PEA_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Enrollment Action Attributes (BEN_PRTT_ENRT_ACTN_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | Program Application |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | Program |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PER_IN_LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PER_IN_LER. |  |
| ACTN_TYP_LVL_CD | VARCHAR2 | 30 |  |  | This lookup will have values
DPNT - 'Dependent Action Items'
BNF - 'Beneficiary Action Items'
ENRTCTFN - 'Enrollment Certification'
RSTRNCTFN - 'Enrollment Restriction Certification'
DPNTCTFN - 'Dependent Certification'
BNFCTFN - 'Beneficiary Certification' |  |
| SSPND_FLAG | VARCHAR2 | 30 |  |  | This column is populated as per the plan design setup in ben_popl_actn_typ_f or ben_ler_popl_actn_typ_f record. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRTT_ENRT_ACTN_FK4 | Non Unique | Default | PER_IN_LER_ID |
| BEN_PRTT_ENRT_ACTN_FK5 | Non Unique | Default | ACTN_TYP_ID |
| BEN_PRTT_ENRT_ACTN_N1 | Non Unique | Default | PL_BNF_ID |
| BEN_PRTT_ENRT_ACTN_N2 | Non Unique | Default | PRTT_ENRT_RSLT_ID |
| BEN_PRTT_ENRT_ACTN_N3 | Non Unique | Default | ELIG_CVRD_DPNT_ID |
| BEN_PRTT_ENRT_ACTN_PK | Unique | Default | PRTT_ENRT_ACTN_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
