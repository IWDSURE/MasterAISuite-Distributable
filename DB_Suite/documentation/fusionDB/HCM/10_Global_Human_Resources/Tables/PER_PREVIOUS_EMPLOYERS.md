# PER_PREVIOUS_EMPLOYERS

Details about the previous employers that the employee worked for before the current enterprise.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpreviousemployers-10801.html#perpreviousemployers-10801](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpreviousemployers-10801.html#perpreviousemployers-10801)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PREVIOUS_EMPLOYERS_PK | PREVIOUS_EMPLOYER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREVIOUS_EMPLOYER_ID | NUMBER |  | 18 | Yes | Surrogate ID for Previous Employer record |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 | Yes | This is the FK of the person to which previous employer record applies |
| START_DATE | DATE |  |  |  | Start Date of the Previous Employer Record |
| END_DATE | DATE |  |  |  | End Date of the Previous Employer Record |
| PERIOD_YEARS | NUMBER |  | 2 |  | The whole number of years at the previous employer |
| PERIOD_DAYS | NUMBER |  | 3 |  | The Number of days on top of the whole year at the previous employer |
| EMPLOYER_NAME | VARCHAR2 | 240 |  |  | Identifier for the employer |
| EMPLOYER_COUNTRY | VARCHAR2 | 30 |  |  | Country of the Employer |
| EMPLOYER_ADDRESS | VARCHAR2 | 4000 |  |  | Address for the employer |
| EMPLOYER_TYPE | VARCHAR2 | 30 |  |  | Category of the employer |
| EMPLOYER_SUBTYPE | VARCHAR2 | 30 |  |  | Category of the employer |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description for the service history period |
| PEM_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| PEM_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PEM_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| PEM_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| PEM_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| ALL_ASSIGNMENTS | VARCHAR2 | 1 |  | Yes | Obsolete. Not used anymore. |
| PERIOD_MONTHS | NUMBER |  | 2 |  | Obsolete. Not used anymore. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PREVIOUS_EMPLOYERS_FK1 | Non Unique | Default | PERSON_ID |
| PER_PREVIOUS_EMPLOYERS_PK | Unique | Default | PREVIOUS_EMPLOYER_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
