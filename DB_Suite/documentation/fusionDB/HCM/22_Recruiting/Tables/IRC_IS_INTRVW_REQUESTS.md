# IRC_IS_INTRVW_REQUESTS

This table stores all the interview requests done to the candidate as well store other information like counts

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisintrvwrequests-18264.html#ircisintrvwrequests-18264](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisintrvwrequests-18264.html#ircisintrvwrequests-18264)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_INTRVW_REQUESTS_PK | INTRVW_REQUESTS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTRVW_REQUESTS_ID | NUMBER |  | 18 | Yes | The primary key for this table. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign key to the submissions (IRC_SUBMISSIONS) to which we are linking the interview request |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Foreign key to the schedules (IRC_IS_SCHEDULES_B) to which we are linking the interview request |
| INTERVIEW_ID | NUMBER |  | 18 |  | Foreign key to the interviews (IRC_IS_INTERVIEWS) to which we are linking the interview request |
| IS_RSCHLD_RQSTED_FLAG | VARCHAR2 | 1 |  | Yes | Flag used when reschedule is requested to the candidate, count will not be incremented. (Default value 'N') |
| INTRVW_RSCHLD_COUNT | NUMBER |  | 9 | Yes | Holds the count for the reschedules because it can exceed setting value, default is 0 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUTO_O365_IS_OVERRIDDEN_FLAG | VARCHAR2 | 1 |  |  | Flag used when the interviewers are overridden. |
| AUTO_O365_OVERRIDDEN_DURATION | VARCHAR2 | 32 |  |  | Determine the overridden interview meeting slot duration. Lookup to use ORA_IRC_IS_MEETING_DURATION. |
| IS_RESCHEDULED_FLAG | VARCHAR2 | 1 |  | Yes | Determine if the Interview Request has been rescheduled. |
| EARLIEST_AVAILABLE_DATE | TIMESTAMP |  |  |  | Manual and proposed slots will be shown starting from this timestamp. |
| FEEDBACK_REQUEST_CONFIG | CLOB |  |  |  | Contains feedback request configuration to be created. |
| OVERRIDDEN_LOCATION_TYPE | VARCHAR2 | 32 |  |  | Overrides IRC_IS_LOCATIONS.LOCATION_TYPE. |
| OVERRIDDEN_MEETING_PROVIDER | VARCHAR2 | 64 |  |  | Overrides IRC_IS_INTERVIEWS.INTERVIEW_MEETING_PROVIDER. |
| OVERRIDDEN_VISBLTY_RANGE_CODE | VARCHAR2 | 30 |  |  | Overrides IRC_IS_SCHEDULES_B.INTERVWS_VISIBILITY_RANGE_CODE. |
| OVERRIDDEN_CONFERENCE_LINK | VARCHAR2 | 4000 |  |  | Overrides IRC_IS_LOCATIONS.WEB_CONFERENCE_LINK. |
| OVERRIDDEN_PHONE_PASSCODE | VARCHAR2 | 30 |  |  | Overrides IRC_IS_LOCATIONS.PHONE_NUMBER_PASSCODE. |
| OVERRIDDEN_PH_COUNTRY_CODE_ID | NUMBER |  | 18 |  | Foreign key to a phone country code. (HZ_PHONE_COUNTRY_CODES) |
| OVERRIDDEN_PHONE_COUNTRY | VARCHAR2 | 30 |  |  | Overrides IRC_IS_LOCATIONS.PHONE_COUNTRY_CODE_NUMBER. |
| OVERRIDDEN_PHONE_AREA | VARCHAR2 | 30 |  |  | Overrides IRC_IS_LOCATIONS.PHONE_AREA_CODE. |
| OVERRIDDEN_PHONE_NUMBER | VARCHAR2 | 60 |  |  | Overrides IRC_IS_LOCATIONS.PHONE_NUMBER. |
| OVERRIDDEN_PHONE_EXTENSION | VARCHAR2 | 60 |  |  | Overrides IRC_IS_LOCATIONS.PHONE_EXT. |
| OVERRIDDEN_LOCATION_ID | NUMBER |  | 18 |  | Overrides IRC_IS_LOCATIONS.LOCATION_ID. |
| OVERRIDDEN_LOCATION_DETAILS | CLOB |  |  |  | Overrides IRC_IS_LOCATIONS.LOCATION_DETAILS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_INTRVW_REQUESTS_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_IS_INTRVW_REQUESTS_FK2 | Non Unique | Default | SCHEDULE_ID |
| IRC_IS_INTRVW_REQUESTS_FK4 | Non Unique | Default | OVERRIDDEN_PH_COUNTRY_CODE_ID |
| IRC_IS_INTRVW_REQUESTS_N1 | Non Unique | Default | INTERVIEW_ID, CREATION_DATE |
| IRC_IS_INTRVW_REQUESTS_PK | Unique | Default | INTRVW_REQUESTS_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
