# PER_PREVIOUS_JOBS

Details of Jobs held with previous employers

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpreviousjobs-17339.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpreviousjobs-17339.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PREVIOUS_JOB_PK | PREVIOUS_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREVIOUS_JOB_ID | NUMBER |  | 18 | Yes | Primary Key of the Table |
| PREVIOUS_EMPLOYER_ID | NUMBER |  | 18 | Yes | Must exist in PER_PREVIOUS_EMPLOYERS |
| START_DATE | DATE |  |  |  | Start date of the job |
| END_DATE | DATE |  |  |  | End date of the job |
| PERIOD_YEARS | NUMBER |  | 2 |  | The whole number of Years at the previous job |
| PERIOD_DAYS | NUMBER |  | 3 |  | the number of days on top of the whole years at the previous employer |
| JOB_NAME | VARCHAR2 | 240 |  |  | Identifier for the Job |
| EMPLOYMENT_CATEGORY | VARCHAR2 | 30 |  |  | Description for the job |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description for the job |
| PJO_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive flexfield Attribute Category |
| PJO_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PJO_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield Information Category |
| PJO_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJO_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| ALL_ASSIGNMENTS | VARCHAR2 | 1 |  |  | All Assignments Flag |
| PERIOD_MONTHS | NUMBER |  | 2 |  | The whole number of Months at the previous job |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PREVIOUS_JOBS_FK1 | Non Unique | Default | PREVIOUS_EMPLOYER_ID |
| PER_PREVIOUS_JOBS_PK | Unique | Default | PREVIOUS_JOB_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
