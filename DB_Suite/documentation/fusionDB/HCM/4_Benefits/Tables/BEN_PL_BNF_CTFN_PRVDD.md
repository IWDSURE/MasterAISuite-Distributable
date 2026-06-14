# BEN_PL_BNF_CTFN_PRVDD

BEN_PL_BNF_CTFN_PRVDD  identifies the certfications  that have been provided by a participant designating beneficiaries for a plan.   . For example,  a person may have provided a notarized statement of non-spousal designation as a result of designating a beneficiary other than his or her spouse.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplbnfctfnprvdd-26830.html#benplbnfctfnprvdd-26830](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplbnfctfnprvdd-26830.html#benplbnfctfnprvdd-26830)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_BNF_CTFN_PRVDD_PK | PL_BNF_CTFN_PRVDD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PL_BNF_CTFN_PRVDD_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| BNF_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Beneficiary certification type. |  |
| BNF_CTFN_RECD_DT | DATE |  |  |  | Beneficiary certification received date. |  |
| CVRD_BNF_CTFN_RECD_DT | DATE |  |  |  | Certification Received Date |  |
| BNF_CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary certification required Y or N. |  |
| PL_BNF_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PL_BNF_F. |  |
| PRTT_ENRT_ACTN_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PRTT_ENRT_ACTN_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| PBC_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| PBC_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Beneficiary Certification Attributes (BEN_PL_BNF_CTFN_PRVDD_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | Program Application |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | Program Name |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ENDED_PER_IN_LER_ID | NUMBER |  | 18 |  | Life Event That caused the End Date |  |
| DOCS_PRVDD_DTLS_ID | NUMBER |  | 18 |  | Foreign Key to BEN_DOCS_PRVDD_DTLS |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |  |
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
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_BNF_CTFN_PRVDD_N1 | Non Unique | Default | PL_BNF_ID |
| BEN_PL_BNF_CTFN_PRVDD_N2 | Non Unique | Default | PRTT_ENRT_ACTN_ID |
| BEN_PL_BNF_CTFN_PRVDD_N3 | Non Unique | FUSION_TS_TX_IDX | DOCS_PRVDD_DTLS_ID |
| BEN_PL_BNF_CTFN_PRVDD_PK1 | Unique | Default | PL_BNF_CTFN_PRVDD_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
