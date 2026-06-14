# IRC_IS_INTERVIEWS

IRC_IS_INTERVIEWS will contain all the interview slots information

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisinterviews-25653.html#ircisinterviews-25653](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisinterviews-25653.html#ircisinterviews-25653)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_INTERVIEWS_PK | SCHEDULE_INTERVIEW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SCHEDULE_INTERVIEW_ID | NUMBER |  | 18 | Yes | The primary key for this table. |  |
| MEETING_HOST_TYPE | VARCHAR2 | 240 |  |  | Stores the value of meeting host for the interview. Selected named person or team member type as meeting host. Lookup to use ORA_HIRINGMANAGER or ORA_HIRING_TEAM_COLLABORATOR or ORA_RECRUITER or ORA_IS_HOST |  |
| INTERVIEW_MEETING_PROVIDER | VARCHAR2 | 64 |  |  | Stores the value of the meeting provider for the interview |  |
| SUBMISSION_ID | NUMBER |  | 18 |  | Foreign key to the associated submission(IRC_SUBMISSIONS) for this schedule. | Obsolete |
| SCHEDULE_ID | NUMBER |  | 18 |  | Foreign key to the associated schedule(IRC_IS_SCHEDULES_B) for this schedule. |  |
| INTERVIEW_NOTES | CLOB |  |  |  | Interview notes for the candidate |  |
| INTERVIEW_GUIDELINES | CLOB |  |  |  | Provides the interview guidelines |  |
| IS_SCHEDULED | VARCHAR2 | 1 |  |  | Y or N that is set to Y when the time proposal is used by a candidate. |  |
| START_DATE | TIMESTAMP |  |  |  | The start date for the planned interview. |  |
| END_DATE | TIMESTAMP |  |  |  | The end date for the planned interview. |  |
| SCHEDULE_LOCATION_ID | NUMBER |  | 18 |  | Foreign key to the schedule location. (IRC_IS_LOCATIONS) |  |
| LAST_REMINDER_DATE | TIMESTAMP |  |  |  | Last time that the interview reminder message was sent through ESS job. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OFFICE365_USER_ID | VARCHAR2 | 256 |  |  | The Microsoft Active Directory user id that was used to create the calendar event. This user is also the organizer for this event. |  |
| OFFICE365_CALENDAR_ID | VARCHAR2 | 256 |  |  | The calendar id that was used to create the calendar event for the scheduled interview. |  |
| OFFICE365_CALENDAR_EVENT_ID | VARCHAR2 | 256 |  |  | The calendar event of the calendar event that was created for the interview. |  |
| OFFICE365_CAL_EV_IMMUTABLE_ID | VARCHAR2 | 256 |  |  | The calendar event immutable id of the calendar event that was created for the interview |  |
| OFFICE365_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last update in Office 365 |  |
| OFFICE365_LAST_SYNC_TIME | TIMESTAMP |  |  |  | Indicates the date and time of the last synchronization with Office 365 |  |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | ESS job request Id that retrieved the latest information from Office 365 |  |
| TOTAL_SEATS_COUNT | NUMBER |  | 9 |  | The number of seats available for the candidates to schedule an interview for this interview slot. |  |
| IS_COMPLETED | VARCHAR2 | 1 |  |  | Y or N that is set to Y once the interview is completed. |  |
| MEETING_LINK_URL | VARCHAR2 | 500 |  |  | Stores the meeting join link URL. |  |
| MEETING_HTTP_CONTENT | CLOB |  |  |  | Stores HTTP content for the online meeting event |  |
| ZOOM_MEETING_ID | NUMBER |  | 18 |  | The meeting ID of the Zoom meeting |  |
| GOOGLE_USER_ID | VARCHAR2 | 256 |  |  | Google user that was used to create the calendar event. This user is also the organizer for this event. |  |
| GOOGLE_CALENDAR_ID | VARCHAR2 | 256 |  |  | The Google calendar id that was used to create the calendar event for the scheduled interview. |  |
| GOOGLE_CALENDAR_EVENT_ID | VARCHAR2 | 256 |  |  | The Google calendar event of the calendar event that was created for the interview. |  |
| GOOGLE_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last update in Google. |  |
| GOOGLE_LAST_SYNC_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last synchronization with Google. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_IS_INTERVIEWS_FK1 | Non Unique | Default | SCHEDULE_LOCATION_ID |  |
| IRC_IS_INTERVIEWS_FK2 | Non Unique | Default | SCHEDULE_ID |  |
| IRC_IS_INTERVIEWS_FK3 | Non Unique | Default | SUBMISSION_ID | Obsolete |
| IRC_IS_INTERVIEWS_N1 | Non Unique | Default | START_DATE, OFFICE365_CAL_EV_IMMUTABLE_ID |  |
| IRC_IS_INTERVIEWS_N2 | Non Unique | Default | IS_COMPLETED, END_DATE |  |
| IRC_IS_INTERVIEWS_PK | Unique | Default | SCHEDULE_INTERVIEW_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
