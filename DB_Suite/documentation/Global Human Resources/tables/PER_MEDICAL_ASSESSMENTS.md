# PER_MEDICAL_ASSESSMENTS

This table stores the medical assessments for the person.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permedicalassessments-17892.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permedicalassessments-17892.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_MEDICAL_ASSESSMENTS_PK | MEDICAL_ASSESSMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEDICAL_ASSESSMENT_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate key. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person for whom the medical assessment is recorded |
| EXAMINER_NAME | VARCHAR2 | 240 |  |  | Name of examiner who performed consultation |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Organization in which this assessment came about. Foreign key to HR_ALL_ORGANIZATION_UNITS |
| CONSULTATION_DATE | DATE |  |  | Yes | Date of medical consultation |
| CONSULTATION_TYPE | VARCHAR2 | 30 |  | Yes | Type of medical assessment |
| CONSULTATION_RESULT | VARCHAR2 | 30 |  |  | Result of medical assessment |
| DISABILITY_ID | NUMBER |  | 18 |  | Disability referenced by this assessment. Foreign key to PER_WORK_INCIDENTS |
| INCIDENT_ID | NUMBER |  | 18 |  | Incident referenced by this assessment. Foreign key to PER_WORK_INCIDENTS |
| NEXT_CONSULTATION_DATE | DATE |  |  |  | Date of next medical assessments |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of medical assessment |
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
| MEA_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Oracle-reserved descriptive flexfield structure defining column |
| MEA_INFORMATION1 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION2 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION3 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION4 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION5 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION6 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION7 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION8 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION9 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION10 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION11 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION12 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION13 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION14 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION15 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION16 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION17 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION18 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION19 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION20 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION21 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION22 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION23 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION24 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION25 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION26 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION27 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION28 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION29 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| MEA_INFORMATION30 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_MEDICAL_ASSESSMENTS_PK | Unique | Default | MEDICAL_ASSESSMENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
