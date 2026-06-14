# IRC_IS_SCHEDULES_B

IRC_IS_SCHEDULES_B table stores the interview scheduling related information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisschedulesb-26812.html#ircisschedulesb-26812](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisschedulesb-26812.html#ircisschedulesb-26812)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_SCHEDULES_B_PK | SCHEDULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_ID | NUMBER |  | 18 | Yes | The primary key for this table. |
| DEFAULT_TEMPLATE_FLAG | VARCHAR2 | 1 |  |  | Identifies the default template for schedule creation. Possible values Y/N/null |
| SCHEDULE_CODE | VARCHAR2 | 240 |  | Yes | Code associated with the schedule. |
| REQUISITION_ID | NUMBER |  | 18 |  | Foreign key to the associated requisition(IRC_REQUISITIONS_B) for this schedule. |
| SCHEDULE_TYPE | VARCHAR2 | 32 |  | Yes | Lookup defined by ORA_IRC_IS_SCHEDULE_TYPE which can be a template or a normal schedule. |
| INTERVIEW_TYPE | VARCHAR2 | 32 |  |  | Lookup defined by ORA_IRC_IS_INTERVIEW_TYPE which can be a Candidate or Hiring team manage. |
| SCHEDULE_TEMPLATE_ID | NUMBER |  | 18 |  | Foreign key to the schedule template(IRC_IS_SCHEDULES_B) that was used to create this schedule. |
| SCHEDULE_LOCATION_ID | NUMBER |  | 18 |  | Foreign key to the schedule location. (IRC_IS_LOCATIONS) |
| SCHEDULE_LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last modified schedule. |
| STATUS | VARCHAR2 | 32 |  | Yes | The status of the current schedule.

Lookup defined by ORA_IRC_SCHEDULE_STATUS_TYPE which can be a DRAFT, PUBLISHED, UNPUBLISHED. |
| INCLUDE_ICS | VARCHAR2 | 1 |  |  | Include the Interviewer Documents for the ICS. |
| INCLUDE_JOB_POSTING_LINK | VARCHAR2 | 1 |  |  | Include the Interviewer Documents for the Job Posting Link. |
| INCLUDE_RESUME | VARCHAR2 | 1 |  |  | Include the Interviewer Documents for the Candidate Resume. |
| INTR_INVITED_MSG_ID | NUMBER |  | 18 |  | Foreign key to the associated content library (IRC_DESCRIPTIONS_B) Ad Hoc Email message for the candidate to schedule an interview. |
| INTR_SCHEDULED_MSG_ID | NUMBER |  | 18 |  | Foreign key to the associated content library (IRC_DESCRIPTIONS_B) Ad Hoc Email message for the candidate that an interview has been scheduled. |
| INTR_CANCELLED_MSG_ID | NUMBER |  | 18 |  | Foreign key to the associated content library (IRC_DESCRIPTIONS_B) Ad Hoc Email message for the candidate that an interview has been cancelled. |
| INTR_UPDATED_MSG_ID | NUMBER |  | 18 |  | Foreign key to the associated content library (IRC_DESCRIPTIONS_B) Ad Hoc Email message for the candidate that an interview has been updated or rescheduled. |
| INTR_REMINDED_MSG_ID | NUMBER |  | 18 |  | Foreign key to the associated content library (IRC_DESCRIPTIONS_B) Ad Hoc Email message for the candidate for the interview reminder. |
| INTR_RESCHEDULED_MSG_ID | NUMBER |  | 18 |  | Foreign key to the associated content library (IRC_DESCRIPTIONS_B) Ad Hoc Email message for the candidate that reschedule interview has been requested. |
| IS_CANCELLABLE_FLAG | VARCHAR2 | 1 |  |  | Y or N that is set to Y when the candidate can cancel the interview (Default value 'N') |
| IS_RESCHEDULABLE_FLAG | VARCHAR2 | 1 |  |  | Y or N that is set to Y when the candidate can reschedule the interview (Default value 'N') |
| ALLOW_SAME_DAY_SCHDLNG_FLAG | VARCHAR2 | 1 |  |  | Y or N that is set to Y when candidate can schedule/reschedule on the same day. It can be, nowp lus 1 hour or 2 hours later. (Default value 'N') |
| HAS_VISIBILITY_RANGE_FLAG | VARCHAR2 | 1 |  |  | Y or N that is set to Y when a visibility on the interviews range should be applied. (Default value 'N') |
| INTERVWS_VISIBILITY_RANGE_CODE | VARCHAR2 | 30 |  |  | Values from lookup ORA_IRC_IS_INTERVWS_VISIBILITY |
| HAS_RESCHDLE_LIMIT_FLAG | VARCHAR2 | 1 |  |  | Y or N that is set to Y when a reschedule limit should be applied. (Default value 'N') |
| INTERVW_RESCHDLE_LIMIT_CODE | VARCHAR2 | 30 |  |  | Values from lookup ORA_IRC_IS_RESCHDLE_LIMIT |
| HAS_CHANGE_LOCK_FLAG | VARCHAR2 | 1 |  |  | Y or N that is set to Y when reschedule/cancel should be controlled (Default value 'N') |
| INTERVW_CHANGE_LOCK_CODE | VARCHAR2 | 30 |  |  | Values from lookup ORA_IRC_IS_INTRVW_CHANG_LOCK |
| SCHEDULE_ALMOST_FULL_NOTIF | VARCHAR2 | 32 |  |  | Lookup defined by ORA_IRC_IS_SCH_ALMOST_FULL which can be no reminder or when number of openings are less than the given value |
| SCHEDULE_ALMOST_FULL_THRESHOLD | NUMBER |  | 18 |  | Value of the number of openings at which the schedule almost full reminder must be sent |
| SCHEDULE_FULL_NOTIF | VARCHAR2 | 32 |  |  | Lookup defined by ORA_IRC_IS_SCH_FULL which can be no reminder or when schedule is full |
| SCHEDULE_REMINDER_SENT | VARCHAR2 | 30 |  |  | Stores the value of whether the schedule almost full or schedule full notifications has been sent since the last time openings were added to slot |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUTO_O365_CALENDAR_SLOT_FLAG | VARCHAR2 | 1 |  |  | Determine if the O365 automatic slots creation is enabled for this shedule.Y or N or null value |
| AUTO_SLOT_INTERVIEW_DURATION | VARCHAR2 | 32 |  |  | Determine the interview meeting slot duration.Lookup to use ORA_IRC_IS_MEETING_DURATION |
| AUTO_COLLAB_RESP_TYPE_LIST | VARCHAR2 | 1000 |  |  | The collaborator's type associated with this schedule will be used to determine the O365 available slots for the associated interviewers. |
| AUTO_MEETING_PROVIDER | VARCHAR2 | 64 |  |  | Stores the value of the meeting provider for the interview.Value from Lookup type ORA_IRC_IS_ONLINE_MEETG_PROVIDER,ORA_IS_TEAMS |
| AUTO_MEETING_HOST | VARCHAR2 | 240 |  |  | Stores the value of meeting host for the interview. Selected named person or team member type as meeting host. Lookup to use ORA_HIRINGMANAGER or ORA_HIRING_TEAM_COLLABORATOR or ORA_RECRUITER or ORA_HOST |
| SCHEDULE_OWNER | NUMBER |  | 18 |  | Person Id of the user who created the interview schedule |
| SEND_AVAILABILITY_REQUEST_FLAG | VARCHAR2 | 1 |  |  | Setting to request availability for defined users when the interview schedule is saved.Y or N or null value |
| IS_FEEDBK_INFO_FLAG | VARCHAR2 | 1 |  |  | Include the feedback information in interview schedule.Y or N |
| INCLUDE_INTERVIEWER_ICS_FLAG | VARCHAR2 | 1 |  |  | Include .isc file for interviewer |
| NB_DAYS_BEFORE_SCHDLNG | NUMBER |  | 9 |  | Number of days before candidate can schedule |
| INCLUDE_COVER_LETTER_FLAG | VARCHAR2 | 1 |  |  | Include the Interviewer Documents for the Candidate Cover Letter |
| INCLUDE_MISC_ATTACHMENTS_FLAG | VARCHAR2 | 1 |  |  | Include the Interviewer Documents for the Candidate Miscellaneous Attachments |
| INCLUDE_INTERNAL_DOCS_FLAG | VARCHAR2 | 1 |  |  | Include the Interviewer Documents for the Candidate Internal Documents |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_SCHEDULES_B_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_IS_SCHEDULES_B_FK10 | Non Unique | Default | SCHEDULE_OWNER |
| IRC_IS_SCHEDULES_B_FK2 | Non Unique | Default | SCHEDULE_TEMPLATE_ID |
| IRC_IS_SCHEDULES_B_FK3 | Non Unique | Default | SCHEDULE_LOCATION_ID |
| IRC_IS_SCHEDULES_B_FK4 | Non Unique | Default | INTR_INVITED_MSG_ID |
| IRC_IS_SCHEDULES_B_FK5 | Non Unique | Default | INTR_SCHEDULED_MSG_ID |
| IRC_IS_SCHEDULES_B_FK6 | Non Unique | Default | INTR_CANCELLED_MSG_ID |
| IRC_IS_SCHEDULES_B_FK7 | Non Unique | Default | INTR_UPDATED_MSG_ID |
| IRC_IS_SCHEDULES_B_FK8 | Non Unique | Default | INTR_REMINDED_MSG_ID |
| IRC_IS_SCHEDULES_B_FK9 | Non Unique | Default | INTR_RESCHEDULED_MSG_ID |
| IRC_IS_SCHEDULES_B_N1 | Non Unique | Default | SCHEDULE_TYPE, STATUS |
| IRC_IS_SCHEDULES_B_N2 | Non Unique | Default | DEFAULT_TEMPLATE_FLAG, INTERVIEW_TYPE |
| IRC_IS_SCHEDULES_B_PK | Unique | Default | SCHEDULE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
