# HRA_CHECK_IN_MEETINGS

It will store UI field values for creating check-in meeting like check-in meeting name, date etc.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckinmeetings-12521.html#hracheckinmeetings-12521](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckinmeetings-12521.html#hracheckinmeetings-12521)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_CHECK_IN_MEETINGS_PK | CHECK_IN_MEETING_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECK_IN_MEETING_ID | NUMBER |  | 18 | Yes | Primary key of Check-In Meeting. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| MANAGER_PERSON_ID | NUMBER |  | 18 |  | This is the manager associated with this check-in meeting |
| WORKER_PERSON_ID | NUMBER |  | 18 |  | This is the worker associated with this check-in meeting |
| WORKER_ASSIGNMENT_ID | NUMBER |  | 18 |  | This is the worker assignment id associated with this check-in meeting |
| CREATED_BY_PERSON_ID | NUMBER |  | 18 |  | This is the id of person who created this check-in meeting. |
| CHECK_IN_TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign Key to Templates table (HRA_CHECK_IN_TMPLS_B) |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | Foreign key to HRT_REVIEW_PERIODS_B |
| DOCUMENT_NAME | VARCHAR2 | 240 |  | Yes | Name of Check In Template |
| CHECK_IN_DATE | DATE |  |  | Yes | This is the date when the check-in meeting is valid from |
| STATUS_CODE | VARCHAR2 | 30 |  |  | This is the status of check-in document. |
| TEMPLATE_TYPE_CODE | VARCHAR2 | 30 |  |  | Identifies template type of the CheckIn document. |
| WORKER_QSTNR_DISCUSSED_FLAG | VARCHAR2 | 30 |  |  | Identify if the worker questionnaire has been discussed or not |
| MANAGER_QSTNR_DISCUSSED_FLAG | VARCHAR2 | 30 |  |  | Identify if the manager questionnaire has been discussed or not. |
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
| SCHEDULE_OWNER_ID | NUMBER |  | 18 |  | This is the parent key for PER_CHECKLIST_SCHEDULES.SCHEDULE_OWNER_ID to create recurring check-ins. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CALENDAR_INVITE_FLAG | VARCHAR2 | 30 |  |  | Identify if the create meeting invite is enabled or not. |
| CALENDAR_INVITE_START_TIME | TIMESTAMP |  |  |  | This is the start time of the check-in meeting in the invite. |
| CALENDAR_INVITE_END_TIME | TIMESTAMP |  |  |  | This is the end time of the check-in meeting in the invite. |
| CALENDAR_INVITE_DESCRIPTION | VARCHAR2 | 4000 |  |  | This is the description of the check-in meeting in the invite. |
| CALENDAR_INVITE_LOCATION | VARCHAR2 | 4000 |  |  | This is the location of the check-in meeting in the invite. |
| CLOSED_FLAG | VARCHAR2 | 30 |  |  | Identify if the check-in is closed or not. |
| ACTION_CODE | VARCHAR2 | 30 |  |  | Action Code for performing the action on the check-in meeting. |
| ACTION_REASON | VARCHAR2 | 30 |  |  | Reason for performing the action on the check-in meeting. |
| ACTION_PERFORMED_BY | NUMBER |  | 18 |  | Stores the Person Id of the person performing the action. |
| ACTION_PERFORMED_DATE | TIMESTAMP |  |  |  | Timestamp when the action was performed. |
| TRANSCRIPT_SUMMARY | CLOB |  |  |  | Stores the summary of the transcript |
| TRANSCRIPT_FILE_NAME | VARCHAR2 | 240 |  |  | Stores the name of the transcript file. |
| TRANSCRIPT_FILE_UPLOADED_BY | NUMBER |  |  |  | Stores the person id who uploaded the transcript file. |
| TRANSCRIPT_FILE_UPLOAD_DATE | TIMESTAMP |  |  |  | Stores the date on which transcript file got uploaded |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_CHECK_IN_MEETINGS_N1 | Non Unique | Default | CHECK_IN_TEMPLATE_ID, DOCUMENT_NAME |
| HRA_CHECK_IN_MEETINGS_N2 | Non Unique | Default | WORKER_PERSON_ID, CHECK_IN_TEMPLATE_ID, REVIEW_PERIOD_ID |
| HRA_CHECK_IN_MEETINGS_N3 | Non Unique | Default | WORKER_ASSIGNMENT_ID, BUSINESS_GROUP_ID, REVIEW_PERIOD_ID |
| HRA_CHECK_IN_MEETINGS_N4 | Non Unique | Default | SCHEDULE_OWNER_ID |
| HRA_CHECK_IN_MEETINGS_PK | Unique | Default | CHECK_IN_MEETING_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
