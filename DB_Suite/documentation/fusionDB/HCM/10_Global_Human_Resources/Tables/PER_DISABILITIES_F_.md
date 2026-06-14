# PER_DISABILITIES_F_

Store disability information for a person.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdisabilitiesf-20906.html#perdisabilitiesf-20906](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdisabilitiesf-20906.html#perdisabilitiesf-20906)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DISABILITIES_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DISABILITY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DISABILITY_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| SELF_DISCLOSED_TYPE | VARCHAR2 | 30 |  |  | Self Disclosed Disability |
| DISCLOSURE_DATE | DATE |  |  |  | Disability Disclosure Date |
| ACCOMMODATION_REQUEST | VARCHAR2 | 2000 |  |  | Accommodation Request |
| PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_PEOPLE_F. |
| INCIDENT_ID | NUMBER |  | 18 |  | Foreign key to PER_WORK_INCIDENTS. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_F |
| REGISTRATION_ID | VARCHAR2 | 30 |  |  | ID given to person following registration with disability organization. |
| REGISTRATION_DATE | DATE |  |  |  | Date of registration with organization for the disabled. |
| REGISTRATION_EXP_DATE | DATE |  |  |  | Expiry date of registration with organization for the disabled. |
| ASSESSMENT_DUE_DATE | DATE |  |  |  | Obsolete |
| CATEGORY | VARCHAR2 | 30 |  |  | Person Disability Category Name, derived from DISABILITY_CATEGORY lookup. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Person Disability description text |
| DEGREE | NUMBER |  | 5 |  | Person Disability degree |
| QUOTA_FTE | NUMBER |  | 5 |  | Person Disability Quota FTE value |
| REASON | VARCHAR2 | 30 |  |  | Person Disability Reason name, derived from DISABILITY_REASON lookup. |
| PRE_REGISTRATION_JOB | VARCHAR2 | 30 |  |  | Obsolete |
| WORK_RESTRICTION | VARCHAR2 | 2000 |  |  | Person Disability work restriction details |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| DIS_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| DIS_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STATUS | VARCHAR2 | 30 |  |  | Denotes the status for the person's disability like Temporary. |
| DIS_INFORMATION_DATE1 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE2 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE3 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE4 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE5 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE6 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE7 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE8 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE9 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE10 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER1 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER2 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER3 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER4 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER5 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER6 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER7 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER8 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER9 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER10 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| DIS_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIS_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DISABILITY_CODE | VARCHAR2 | 35 |  |  | Part of the alternate key or user key that contains a user defined value that can be used to identify a disabilities record in conjunction with the effective start date |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PDFN1_ | Non Unique | Default | DISABILITY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_DISABILITIES_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DISABILITY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
