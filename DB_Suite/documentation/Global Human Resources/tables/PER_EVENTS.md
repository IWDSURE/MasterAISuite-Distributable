# PER_EVENTS

Table Definition for PER_EVENTS

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perevents-21553.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perevents-21553.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EVENTS_PK | EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign key to HR_LOCATIONS. |
| INTERNAL_CONTACT_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_PEOPLE. |
| ORGANIZATION_RUN_BY_ID | NUMBER |  | 18 |  | Foreign key to HR_ORGANIZATION_UNITS. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ASSIGNMENTS. |
| DATE_START | DATE |  |  | Yes | Start date of event or interview. |
| TYPE | VARCHAR2 | 30 |  | Yes | Event type or interview name. |
| CONTACT_TELEPHONE_NUMBER | VARCHAR2 | 60 |  |  | External contact telephone number. |
| DATE_END | DATE |  |  |  | End date of event or interview. |
| EMP_OR_APL | VARCHAR2 | 1 |  |  | Indicates an employee or applicant (E=employee and A=applicant). |
| EVENT_OR_INTERVIEW | VARCHAR2 | 30 |  |  | Indicates an event or interview (E = event and I = interview. |
| EXTERNAL_CONTACT | VARCHAR2 | 80 |  |  | Name of the external contact.  Only used for events. |
| TIME_END | VARCHAR2 | 5 |  |  | Time the event or interview is expected to end. |
| TIME_START | VARCHAR2 | 5 |  |  | Time the event or interview is expected to start. |
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
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EVENTS_N1 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_EVENTS_N2 | Non Unique | Default | LOCATION_ID |
| PER_EVENTS_N3 | Non Unique | Default | INTERNAL_CONTACT_PERSON_ID |
| PER_EVENTS_N4 | Non Unique | Default | ORGANIZATION_RUN_BY_ID |
| PER_EVENTS_N5 | Non Unique | Default | ASSIGNMENT_ID |
| PER_EVENTS_PK | Unique | Default | EVENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
