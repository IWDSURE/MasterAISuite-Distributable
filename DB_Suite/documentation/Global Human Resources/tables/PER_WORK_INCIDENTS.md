# PER_WORK_INCIDENTS

This table stores details of incidents at work, dates, place, types

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perworkincidents-17437.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perworkincidents-17437.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_WORK_INCIDENTS_PK | INCIDENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INCIDENT_ID | NUMBER |  | 18 | Yes | System generated part of primary key. Surrogate key. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person for whom the row is recorded |
| INCIDENT_REFERENCE | VARCHAR2 | 30 |  | Yes | Unique reference code for the work incident |
| INCIDENT_TYPE | VARCHAR2 | 30 |  | Yes | Type of incident. |
| INCIDENT_DATE | DATE |  |  | Yes | Date of incident. |
| INCIDENT_TIME | VARCHAR2 | 5 |  |  | Time of incident. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment under which incident happened, foreign key to PER_ALL_ASSIGNMENTS_M |
| LOCATION | VARCHAR2 | 30 |  |  | Location of the incident (not related to HR locations) |
| AT_WORK_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether incident occurred at work or en route to work. |
| LAST_WORK_DATE | DATE |  |  |  | Obsolete. Not Used anymore. |
| LAST_WORK_TIME | DATE |  |  |  | Obsolete. Not Used anymore. |
| REPORT_DATE | DATE |  |  |  | Date incident was reported. |
| REPORT_TIME | VARCHAR2 | 5 |  |  | Time incident was reported. |
| REPORT_METHOD | VARCHAR2 | 30 |  |  | Method by which the incident was reported. |
| PERSON_REPORTED_BY | NUMBER |  | 10 |  | Person who reported the incident. Foreign key to PER_PEOPLE_F. |
| PERSON_REPORTED_TO | VARCHAR2 | 2000 |  |  | Details of person or authority that the incident was reported to. |
| WITNESS_DETAILS | VARCHAR2 | 2000 |  |  | Name and contact information of witness(es) to the incident. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Long text description of the incident |
| INJURY_TYPE | VARCHAR2 | 30 |  |  | The category of injury that was incurred. |
| DISEASE_TYPE | VARCHAR2 | 30 |  |  | The category of disease diagnosed |
| HAZARD_TYPE | VARCHAR2 | 30 |  |  | The category of hazard (object or substance) involved |
| BODY_PART | VARCHAR2 | 2000 |  |  | Description of body part involved and how affected. |
| TREATMENT_RECEIVED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether medical treatment administered. |
| HOSPITAL_DETAILS | VARCHAR2 | 2000 |  |  | Details of hospitalisation. |
| DOCTOR_ID | NUMBER |  | 18 |  | Id of doctor treating the injury or disease |
| NEXT_OF_KIN_ID | NUMBER |  | 18 |  | Obsolete. Not Used anymore. |
| ABSENCE_ID | NUMBER |  | 18 |  | Identifies the absence that was recorded, foreign key to PER_ABSENCE_ATTENDANCES |
| COMPENSATION_DATE | DATE |  |  |  | Date of compensation award. |
| COMPENSATION_CURRENCY | VARCHAR2 | 30 |  |  | Currency in which compensation was awarded. |
| COMPENSATION_AMOUNT | NUMBER |  |  |  | Amount of compensation. |
| REMEDIAL_HS_ACTION | VARCHAR2 | 2000 |  |  | Details of health and safely action required following the incident. |
| NOTIFIED_HSREP_ID | NUMBER |  | 18 |  | Health and Safety representative notified of incident. Foreign key to PER_ALL_PEOPLE_F |
| NOTIFIED_HSREP_DATE | DATE |  |  |  | Date Health and Safety representative was notified. |
| NOTIFIED_UREP_ID | NUMBER |  | 18 |  | Person belonging to representative body notified of incident.  Foreign Key to PER_ALL_PEOPLE_F. |
| NOTIFIED_UREP_DATE | DATE |  |  |  | Date representative body was notified of incident. |
| PREVIOUS_INCIDENT_ID | NUMBER |  | 18 |  | Obsolete. Not Used anymore. |
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
| INC_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Oracle-reserved descriptive flexfield structure defining column |
| INC_INFORMATION1 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION2 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION3 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION4 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION5 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION6 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION7 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION8 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION9 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION10 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION11 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION12 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION13 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION14 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION15 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION16 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION17 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION18 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION19 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION20 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION21 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION22 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION23 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION24 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION25 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION26 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION27 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION28 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION29 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| INC_INFORMATION30 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORG_NOTIFIED_DATE | DATE |  |  |  | Date the organization was notified of the work incident. |
| DOCTOR_NAME | VARCHAR2 | 60 |  |  | Name of doctor treating the injury or disease |
| NOTIFIED_REP_ID | NUMBER |  | 18 |  | Person belonging to representative body notified of incident.  Foreign Key to PER_ALL_PEOPLE_F. |
| NOTIFIED_REP_DATE | DATE |  |  |  | Date representative body was notified of incident. |
| NOTIFIED_REP_ORG_ID | NUMBER |  | 18 |  | Representative Body that has been notified. Foreign key to HR_ALL_ORGANIZATION_UNITS |
| RELATED_INCIDENT_ID | NUMBER |  | 18 |  | Work incident to which this record relates. Foreign key to PER_WORK_INCIDENTS |
| OVER_TIME_FLAG | VARCHAR2 | 1 |  |  | Indicates whether disease or condition occurred gradually |
| ABSENCE_EXISTS_FLAG | VARCHAR2 | 1 |  | Yes | Indicates if an absence was recorded for the work incident |
| EMERGENCY_CODE | VARCHAR2 | 30 |  |  | Indicates if the case was an emergency |
| PRIVACY_ISSUE | VARCHAR2 | 30 |  | Yes | Whether this incident is a privacy matter |
| OBJECTS_INVOLVED | VARCHAR2 | 240 |  |  | Objects or substances involved |
| ACTIVITY_AT_TIME_OF_WORK | VARCHAR2 | 240 |  |  | Activity at time of work |
| HOSPITAL_ADDRESS | VARCHAR2 | 240 |  |  | Address of the Hospital |
| DAYS_RESTRICTED_WORK | NUMBER |  | 10 |  | Number of days where work was restricted |
| HOSPITALIZED_FLAG | VARCHAR2 | 30 |  | Yes | Indicates if the person was hospitalized |
| DATE_OF_DEATH | DATE |  |  |  | Denotes the date of death. |
| DAYS_AWAY_FROM_WORK | NUMBER |  | 10 |  | Number of days away from work |
| WORK_START_TIME | VARCHAR2 | 5 |  |  | Time employee began work |
| REPORTING_PERSON_PHONE | VARCHAR2 | 30 |  |  | Phone number of reporting person |
| REPORTING_PERSON_TITLE | VARCHAR2 | 30 |  |  | Job title of person reporting the incident |
| REPORT_COMPLETED_BY | VARCHAR2 | 60 |  |  | Name of the person reporting |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_WORK_INCIDENTS_PK | Unique | Default | INCIDENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
