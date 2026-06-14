# HRR_MEETINGS

The meeting table covers the basic information about the meeting.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetings-17772.html#hrrmeetings-17772](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetings-17772.html#hrrmeetings-17772)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_MEETINGS_PK | MEETING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| MEETING_ID | NUMBER |  | 18 | Yes | Unique primary key that identifies each distinct meeting record in this table. |  |  |
| USE_POT_ASSESS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether Potential Assessment will be used or not. |  |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Identifier of the questionnaire that should be used in the potential assessment in the meeting. |  |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |  |  |
| DASHBOARD_TMPL_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_DASHBOARD_TMPLS_B. |  |  |
| MEETING_PURPOSE | VARCHAR2 | 4000 |  |  | A larger text area to capture the facilitators instructions and comments for the meeting participants. |  |  |
| MEETING_TITLE | VARCHAR2 | 400 |  | Yes | A brief description of the talent review meeting to help distinguish it from other meeting instances. |  |  |
| MEETING_INSTRUCTIONS | VARCHAR2 | 2000 |  |  | An instructions text for the talent review meeting. |  |  |
| MEETING_DATE | TIMESTAMP |  |  | Yes | Date to indicate when the actual meeting will take place. |  |  |
| MEETING_LEADER_ID | NUMBER |  | 18 | Yes | The individual at the top of the organization under review. |  |  |
| MEETING_FACILITATOR_ID | NUMBER |  | 18 | Yes | The person responsible for scheduling, managing and conducting the talent review meeting.  This could be the Business Unit Leader or an individual from the HR department assigned to assist the Business Unit Leader.  The facilitator will be the only person who can create, update, view, and launch the talent review dashboard. |  | Obsolete |
| MEETING_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Indicates the status of the meeting |  |  |
| MEETING_SUBMIT_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the meeting configuration status of a talent review meeting. |  |  |
| MEETING_FACILITATOR_NOTES | VARCHAR2 | 2000 |  |  | Indicates if notes can be captured for this talent review meeting. |  |  |
| MEETING_ORGANIZATION_ID | NUMBER |  | 18 |  | Organization for the review meeting |  |  |
| DATA_SUBMIT_DATE | DATE |  |  |  | The deadline for data used during the talent review meeting to be entered in the various source systems by the meeting participants. |  | Obsolete |
| DATA_SUBMIT_DATE#01 | TIMESTAMP |  |  |  | The deadline for data used during the talent review meeting to be entered in the various source systems by the meeting participants. |  |  |
| MEETING_SUBMISSION_DATE | TIMESTAMP |  |  |  | The timestamp when the meeting was actually submitted. |  |  |
| PREF_REVIEW_QUALIFIER_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_QUALIFIERS_B. |  |  |
| DATA_VALIDITY_CODE | VARCHAR2 | 30 |  |  | The data validity guideline is intended to help the participants determine if the data already captured in the system is still valid for the talent review meeting. |  |  |
| INCLUDE_MATRIX_MGMT | VARCHAR2 | 20 |  |  | Indicates whether matrix managers should be included as reviewers for the meeting. |  |  |
| ENABLE_CALENDAR_INVITE | VARCHAR2 | 30 |  |  | Flag to indicate meeting invite need to be created. |  |  |
| MEETING_END_DATE | TIMESTAMP |  |  |  | The timestamp when the meeting ends. |  |  |
| MEETING_LOCATION | VARCHAR2 | 800 |  |  | URL or physical location of the meeting. |  |  |
| CALENDAR_INVITATION_DETAILS | VARCHAR2 | 4000 |  |  | Additional info for meeting invite. |  |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE1 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE2 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE3 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE4 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE5 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE6 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE7 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE8 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE9 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE10 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE11 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE12 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE13 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE14 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE15 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE16 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE17 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE18 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE19 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE20 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE21 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE22 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE23 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE24 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE25 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE26 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE27 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE28 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE29 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE30 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Meetings (HRR_MEETINGS) |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_MEETINGS_N1 | Non Unique | FUSION_TS_TX_DATA | DASHBOARD_TMPL_ID, BUSINESS_GROUP_ID |
| HRR_MEETINGS_U1 | Unique | FUSION_TS_TX_DATA | MEETING_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
