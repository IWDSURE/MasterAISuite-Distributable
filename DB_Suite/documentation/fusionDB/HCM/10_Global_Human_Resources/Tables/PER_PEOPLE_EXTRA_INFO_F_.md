# PER_PEOPLE_EXTRA_INFO_F_

This table stores effective-dated Extra Information Type data, which consist mainly of legislative person extensions, and vertical extensions.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpeopleextrainfof-12614.html#perpeopleextrainfof-12614](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpeopleextrainfof-12614.html#perpeopleextrainfof-12614)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PEOPLE_EXTRA_INFO_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_EXTRA_INFO_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate key. |
| PERSON_ID | NUMBER |  | 18 |  | Person for whom the Extra Information is recorded |
| INFORMATION_TYPE | VARCHAR2 | 40 |  |  | Type of extra information. |
| PEI_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| PEI_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Extra Information Type flexfield structure defining column |
| PEI_INFORMATION1 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION2 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION3 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION4 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION5 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION6 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION7 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION8 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION9 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION10 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION11 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION12 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION13 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION14 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION15 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION16 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION17 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION18 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION19 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION20 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION21 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION22 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION23 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION24 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION25 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION26 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION27 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION28 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION29 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION30 | VARCHAR2 | 150 |  |  | Extra Information flexfield column |
| PEI_INFORMATION_NUMBER1 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER2 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER3 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER4 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER5 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER6 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER7 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER8 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER9 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER10 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER11 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER12 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER13 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER14 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER15 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER16 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER17 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER18 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER19 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_NUMBER20 | NUMBER |  |  |  | Extra Information flexfield column of Number Type |
| PEI_INFORMATION_DATE1 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE2 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE3 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE4 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE5 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE6 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE7 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE8 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE9 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE10 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE11 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE12 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE13 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE14 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| PEI_INFORMATION_DATE15 | DATE |  |  |  | Extra Information flexfield column of Date Type |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PEI_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEI_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | Extesible Flexfield Category Code |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PEOPLE_EXTRA_INFO_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PPEIFN1_ | Non Unique | Default | PERSON_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
