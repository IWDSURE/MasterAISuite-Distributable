# BEN_PRTT_RT_VAL_CTFN_PRVDD

BEN_PRTT_RT_VAL_CTFN_PRVDD identifies the certifications that have been provided for a rate.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttrtvalctfnprvdd-29148.html#benprttrtvalctfnprvdd-29148](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttrtvalctfnprvdd-29148.html#benprttrtvalctfnprvdd-29148)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRV_CTFN_PRVDD_PK | PRTT_RT_VAL_CTFN_PRVDD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTT_RT_VAL_CTFN_PRVDD_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| ENRT_CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Enrollment certification required Y or N. |
| PRTT_RT_VAL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PRTT_RT_VAL. |
| ENRT_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Enrollment certification type. |
| ENRT_CTFN_RECD_DT | DATE |  |  |  | Certification received date. |
| ENRT_CTFN_DND_DT | DATE |  |  |  | Certification denied date. |
| RVC_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| RVC_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| RVC_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRV_CTFN_PRVDD_FK1 | Non Unique | Default | PRTT_RT_VAL_ID |
| BEN_PRV_CTFN_PRVDD_PK1 | Unique | Default | PRTT_RT_VAL_CTFN_PRVDD_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
