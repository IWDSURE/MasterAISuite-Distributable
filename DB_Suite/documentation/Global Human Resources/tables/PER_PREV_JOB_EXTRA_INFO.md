# PER_PREV_JOB_EXTRA_INFO

Extra information for Jobs held with previous employers

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprevjobextrainfo-21072.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprevjobextrainfo-21072.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PREV_JOB_EXTA_INFO_PK | PREVIOUS_JOB_EXTRA_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREVIOUS_JOB_EXTRA_INFO_ID | NUMBER |  | 18 | Yes | This is the Surrogate ID for Previous Job record |
| PREVIOUS_JOB_ID | NUMBER |  | 18 | Yes | This is the FK of the Previous Job to which previous job extra info  record applies |
| INFORMATION_TYPE | VARCHAR2 | 40 |  | Yes | Information type for this extra job information |
| PJI_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| PJI_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PJI_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield Information Category |
| PJI_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| PJI_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PREV_JOB_EXTRA_INFO_FK1 | Non Unique | Default | PREVIOUS_JOB_ID |
| PER_PREV_JOB_EXTRA_INFO_PK | Unique | Default | PREVIOUS_JOB_EXTRA_INFO_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
