# HR_DOCUMENTS_OF_RECORD_ARCHIVE

This table contains information about the archived data for document records.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** ARCHIVE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumentsofrecordarchive-27032.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumentsofrecordarchive-27032.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_DOCS_OF_RECORD_ARCHIVE_PK | DOCUMENTS_OF_RECORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOCUMENTS_OF_RECORD_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a document of record. |
| DOCUMENT_CODE | VARCHAR2 | 150 |  |  | Document Code uniquely identifies record . |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person against whom document has to be stored. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment against whom document has to be stored. |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 | Yes | Identifies the type of document which is stored. It also determines the document category and subcategory it will be related to. |
| DOCUMENT_NAME | VARCHAR2 | 80 |  |  | Name of the document of record. Used in order to differentiate incase multiple documents are added to the same document type. |
| DOCUMENT_NUMBER | VARCHAR2 | 150 |  |  | Number which legally identifies the particular document. |
| DATE_FROM | DATE |  |  |  | Date from which the document is valid. |
| DATE_TO | DATE |  |  |  | Date until which the document is valid. |
| ISSUING_COUNTRY | VARCHAR2 | 60 |  |  | Country which has issued the document. |
| ISSUING_LOCATION | VARCHAR2 | 100 |  |  | Location at which document has been issued. |
| ISSUED_DATE | DATE |  |  |  | Date on which document has been issued. |
| ISSUING_AUTHORITY | VARCHAR2 | 100 |  |  | Designation of person or authority name who has issued the document. |
| RELATED_OBJECT_NAME | VARCHAR2 | 60 |  |  | Name of the entity whose document is being stored for example Absences. |
| RELATED_OBJECT_ID_COL | VARCHAR2 | 60 |  |  | Attribute name of the entity whose document is being stored e.g. Absence_Id. |
| RELATED_OBJECT_ID | NUMBER |  | 18 |  | Actual value of the attribute. E.g. 100001, actual value of Absence_Id. |
| DEI_ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| DEI_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DEI_ATTRIBUTE31 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE32 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE33 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE34 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE35 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE36 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE37 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE38 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE39 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE40 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DEI_INFORMATION_CATEGORY | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| DEI_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION31 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION32 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION33 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION34 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION35 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION36 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION37 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION38 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION39 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION40 | VARCHAR2 | 4000 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER1 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER2 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER3 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER4 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER5 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER6 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER7 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER8 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER9 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER10 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER11 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER12 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER13 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER14 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER15 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER16 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER17 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER18 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER19 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_NUMBER20 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE1 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE2 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE3 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE4 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE5 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE6 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE7 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE8 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE9 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE10 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE11 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE12 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE13 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE14 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_DATE15 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_TIMESTAMP1 | TIMESTAMP |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_TIMESTAMP2 | TIMESTAMP |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_TIMESTAMP3 | TIMESTAMP |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_TIMESTAMP4 | TIMESTAMP |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DEI_INFORMATION_TIMESTAMP5 | TIMESTAMP |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| COMMENTS | VARCHAR2 | 4000 |  |  | Comments pertaining to the Document Record. |
| PUBLISH | VARCHAR2 | 30 |  |  | Indicates whether the document should be published before the start date |
| PUBLISH_DATE | DATE |  |  |  | Publish date will decide when document should be visible. |
| CREATION_SOURCE | VARCHAR2 | 30 |  |  | Indicates the source of the record creation ie HDL/HSDL/UI/REST etc. |
| TAG_LIST | VARCHAR2 | 2000 |  |  | Tags used to identify document record for class
      ification and grouping. |
| ARCHIVED_BY | VARCHAR2 | 64 |  | Yes | Indicates the user who created the row. |
| ARCHIVE_DATE | TIMESTAMP |  |  | Yes | Indicates the date and time of the creation of the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_DOCS_OF_RECORD_ARCHIVE_N1 | Non Unique | HR_DOCS_OF_RECORD_ARCHIVE_N1 | PERSON_ID |
| HR_DOCS_OF_RECORD_ARCHIVE_N2 | Non Unique | HR_DOCS_OF_RECORD_ARCHIVE_N2 | DOCUMENT_TYPE_ID |
| HR_DOCS_OF_RECORD_ARCHIVE_PK | Unique | HR_DOCS_OF_RECORD_ARCHIVE_PK | DOCUMENTS_OF_RECORD_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
