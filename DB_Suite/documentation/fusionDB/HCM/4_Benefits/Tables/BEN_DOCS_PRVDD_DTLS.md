# BEN_DOCS_PRVDD_DTLS

BEN_DOCS_PRVDD_DTLS stores the details of the Document uploaded against certification requirements along with the validity details

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendocsprvdddtls-27224.html#bendocsprvdddtls-27224](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendocsprvdddtls-27224.html#bendocsprvdddtls-27224)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DOCS_PRVDD_DTLS_PK | DOCS_PRVDD_DTLS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOCS_PRVDD_DTLS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id(Foreign Key to per_all_people_f) |
| CONTACT_PERSON_ID | NUMBER |  | 18 |  | Contact Person Id |
| CTFN_TYPE_CD | VARCHAR2 | 30 |  | Yes | Certification Type |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to hr_document_types_b |
| STATUS | VARCHAR2 | 30 |  |  | Approval Status |
| DOR_ID | NUMBER |  | 18 |  | Foreign Key to hr_documents_of_record |
| UPLOADED_BY | VARCHAR2 | 64 |  |  | Indicates the user who uploaded the document. |
| UPLOADED_DT | DATE |  |  |  | Date on which the Document was uploaded |
| VALIDITY_STRT_DT | DATE |  |  |  | Start of the Documents Validity |
| VALIDITY_END_DT | DATE |  |  |  | End of the Documents Validity |
| APPROVAL_STRT_DT | DATE |  |  |  | Start of Approval Validity |
| APPROVAL_END_DT | DATE |  |  |  | End of Approval Validity |
| APPROVED_BY | VARCHAR2 | 64 |  |  | Document Approved By |
| VERIFICATION_MODE | VARCHAR2 | 30 |  |  | This specifies whether a manual approval from admin is needed or not(auto) |
| COMMENTS | VARCHAR2 | 4000 |  |  | Approval Comments |
| APPROVED_DT | DATE |  |  |  | Date on which the Document was approved |
| REJECTED_DT | DATE |  |  |  | Date on which the Document was denied |
| REJECTION_REASON | VARCHAR2 | 30 |  |  | Reason why the Document has been rejected |
| MAPPING_TABLE_NAME | VARCHAR2 | 30 |  | Yes | Name of the table for which the document setup has been done |
| MAPPING_COLUMN_NAME | VARCHAR2 | 30 |  | Yes | Mapping Table Column Name |
| MAPPING_TABLE_PK_ID | NUMBER |  | 18 | Yes | Mapping Table Primary Key Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| VALIDITY_CD | VARCHAR2 | 30 |  |  | Code which determines the validity time of the document |
| VALIDITY_TM_NUM | NUMBER |  | 18 |  | This determines the time period for which the document will be valid. This will be blank when the Validity_cd is 'Lifetime' |
| APPROVAL_PERD_CD | VARCHAR2 | 30 |  |  | Code which determines the time for which the approval is valid |
| APPROVAL_PERD_TM_NUM | NUMBER |  | 18 |  | This determines the time period for which the approval will be valid. |
| DOC_USG_CD | VARCHAR2 | 30 |  |  | This value differentiates whether the row was created as part of Certification Process or as part of Record Life Event |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | Program Application |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | Program |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_DOCS_PRVDD_DTLS_N1 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID, MAPPING_COLUMN_NAME, MAPPING_TABLE_PK_ID, CONTACT_PERSON_ID, CTFN_TYPE_CD |
| BEN_DOCS_PRVDD_DTLS_PK | Unique | Default | DOCS_PRVDD_DTLS_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
