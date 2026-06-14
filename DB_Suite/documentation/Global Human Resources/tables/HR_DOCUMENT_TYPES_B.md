# HR_DOCUMENT_TYPES_B

This table will contain definitions for type of personal document that can be  maintained by Documents of Record functionality.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumenttypesb-12430.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumenttypesb-12430.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_DOCUMENT_TYPES_B_PK | DOCUMENT_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DOCUMENT_TYPE_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a Document Type |  |
| CATEGORY_CODE | VARCHAR2 | 30 |  | Yes | Define document category for a document type. |  |
| SUB_CATEGORY_CODE | VARCHAR2 | 30 |  |  | Define document sub category for a document type. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from the Legal Entity. |  |
| DOCUMENT_TYPE_LEVEL | VARCHAR2 | 30 |  |  | Document type to be applicable to person or assignment. |  |
| WARNING_PERIOD | NUMBER |  | 18 |  | Warning Period (number of days in advance) to send a notification? in case a particular document is going to expire. |  |
| ACTIVE_INACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | Activate or deactivate a document type In case it is not suitable for deletion. |  |
| MULTIPLE_OCCURENCES_FLAG | VARCHAR2 | 30 |  | Yes | Determine if a particular document type can have multiple instances for the same person, for example Visa. |  |
| AUTHORIZATION_REQUIRED | VARCHAR2 | 1 |  | Yes | Determine if an operation like create, update, delete for particular type of document needs approval or not . |  |
| DOCUMENT_NAME_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type will support attribute document name or not. This can take YES/NO value. |  |
| DOCUMENT_NUMBER_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type will support the attribute document number or not. This can take YES/NO value. |  |
| DATE_FROM_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type will support attribute DateFrom or not. |  |
| DATE_TO_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type will support attribute DateTo or not. |  |
| ISSUING_AUTHORITY_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type will support attribute Issuing Authority or not. |  |
| ISSUED_DATE_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type will have issue date as mandatory attribute or not. |  |
| ISSUING_COUNTRY_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type have issuing country as mandatory attribute or not. |  |
| ISSUING_LOCATION_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type require attribute issuing location or not. |  |
| COMMENTS_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if the documents of this type will support attribute Comments or not. |  |
| PUBLISH_REQUIRED | VARCHAR2 | 30 |  | Yes | This will decide if documents of this type will require publishing or not. |  |
| SYSTEM_DOCUMENT_TYPE | VARCHAR2 | 120 |  | Yes | Name of the document type. |  |
| HIERARCHY_CODE | VARCHAR2 | 30 |  |  | Can be GENERIC - For choosing Legal Employer based Hierarchy or PAYROLL - For choosing Payroll based Hiearchy |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. | Obsolete |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| BI_REPORT_PATH | VARCHAR2 | 2000 |  |  | BI Report Path |  |
| LOCK_CREATE | VARCHAR2 | 30 |  |  | Creation allowed or not |  |
| LOCK_UPDATE | VARCHAR2 | 30 |  |  | Updated allowed or not |  |
| LOCK_DELETE | VARCHAR2 | 30 |  |  | Deletion allowed or not |  |
| MIN_ATTACHMENTS_COUNT | NUMBER |  | 5 | Yes | Minimum Attachments Required . |  |
| RESTRICT_CREATE_ATTACH | VARCHAR2 | 30 |  |  | obsoleted - not in use. |  |
| RESTRICT_UPDATE_ATTACH | VARCHAR2 | 30 |  |  | obsoleted - not in use. |  |
| RESTRICT_DELETE_ATTACH | VARCHAR2 | 30 |  |  | obsoleted - not in use. |  |
| DT_ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |
| DT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE9 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE10 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |
| DT_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION9 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION10 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| DT_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| DT_INFORMATION_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| ARCHIVE_CRITERIA_DAYS | NUMBER |  | 5 |  | Archive documents of records of current document type after criteria days. |  |
| ARCHIVE_CRITERIA_BASIS | VARCHAR2 | 30 |  |  | Archive criteria bases i.e Creation Date , To Date , Issued Date etc . |  |
| PURGE_ARCHIVE_CRITERIA_DAYS | NUMBER |  | 5 |  | Purge archived documents of records of current document type after criteria days. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |
| LOCK_CREATE_ROLE_LIST | VARCHAR2 | 4000 |  |  | Creation allowed for these roles. |  |
| LOCK_UPDATE_ROLE_LIST | VARCHAR2 | 4000 |  |  | Updation allowed for these roles. |  |
| LOCK_DELETE_ROLE_LIST | VARCHAR2 | 4000 |  |  | Deletion allowed for these roles. |  |
| DFF_GLB_SEG_DISPLAY_PREF | VARCHAR2 | 30 |  |  | Global segment display preferences. |  |
| DFF_CTX_SEG_DISPLAY_PREF | VARCHAR2 | 30 |  |  | Context segment display preferences. |  |
| DFF_CTX_SEG_DEFAULT_VALUE | VARCHAR2 | 120 |  |  | Context segment default value. |  |
| TAG_LIST | VARCHAR2 | 2000 |  |  | Tags used to identify document type for classification and grouping |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_DOCUMENT_TYPES_B_N20 | Non Unique | FUSION_TS_TX_IDX | SGUID |
| HR_DOCUMENT_TYPES_B_PK | Unique | FUSION_TS_TX_IDX | DOCUMENT_TYPE_ID, ORA_SEED_SET1 |
| HR_DOCUMENT_TYPES_B_PK1 | Unique | FUSION_TS_TX_IDX | DOCUMENT_TYPE_ID, ORA_SEED_SET2 |
| HR_DOCUMENT_TYPES_B_U1 | Unique | FUSION_TS_TX_IDX | SYSTEM_DOCUMENT_TYPE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
