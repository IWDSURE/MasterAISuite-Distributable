# PER_JOB_EXTRA_INFO_F_

This table holds details of extra information for a job, an intersection between PER_JOB_INFO_TYPES and PER_JOBS_F.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobextrainfof-25790.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobextrainfof-25790.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOB_EXTRA_INFO_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, JOB_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| JOB_EXTRA_INFO_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| INFORMATION_TYPE | VARCHAR2 | 40 |  |  | Type of information stored in the record. | Active |
| JOB_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOBS_F table. | Active |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| JEI_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| JEI_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Active |
| JEI_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| JEI_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| JEI_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| SEQUENCE_NUMBER | NUMBER |  | 8 |  | Indicates the sequence of the extra information flexfields. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_JOB_EXTRA_INFO_FN1_ | Non Unique | Default | JOB_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_JOB_EXTRA_INFO_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, JOB_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
