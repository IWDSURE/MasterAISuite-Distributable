# IRC_IS_INTERVIEW_PART

IRC_IS_INTERVIEW_PART will contain all the interview participants.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisinterviewpart-25045.html#ircisinterviewpart-25045](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisinterviewpart-25045.html#ircisinterviewpart-25045)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_INTERVIEW_PART_PK | PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARTICIPANT_ID | NUMBER |  | 18 | Yes | The primary key representing the participant for this table. |
| SCHEDULE_INTERVIEW_ID | NUMBER |  | 18 |  | Foreign key to the schedule interview entry. (IRC_IS_INTERVIEWS) |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key for the person_id representing this participants. (PER_PERSONS) |
| PARTICIPANT_TYPE | VARCHAR2 | 32 |  | Yes | The type of participant that will take part of the interview. Lookup defined by ORA_IRC_IS_INTERVIEWS_PART_TYPE which can be INTERVIEWER or ORGANIZER. |
| RESPONSE_CODE | VARCHAR2 | 32 |  |  | Lookup value associated with ORA_IRC_IS_PARTICIPANT_RESPONSE lookup type. |
| RESPONSE_PROPOSED_START_DATE | TIMESTAMP |  |  |  | The participant proposed a new start date. |
| RESPONSE_PROPOSED_END_DATE | TIMESTAMP |  |  |  | The participant proposed a new end date. |
| RESPONSE_MESSAGE | VARCHAR2 | 4000 |  |  | The participant responded message that he entered manually. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SUBMISSION_ID | NUMBER |  | 18 |  | The submission id of the candidate that participates in an interview. Foreign key to the associated submission(IRC_SUBMISSIONS). |
| COORDNTR_REQUEST_ID | NUMBER |  | 18 |  | Foreign key to IRC_IS_COORDNTR_REQUESTS table. |
| INTRVW_REQUESTS_ID | NUMBER |  | 18 |  | Foreign key to the interview request entry. (IRC_IS_INTRVW_REQUESTS) |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_INTERVIEW_PART_FK1 | Non Unique | Default | SCHEDULE_INTERVIEW_ID |
| IRC_IS_INTERVIEW_PART_FK2 | Non Unique | Default | PERSON_ID |
| IRC_IS_INTERVIEW_PART_FK3 | Non Unique | Default | SUBMISSION_ID |
| IRC_IS_INTERVIEW_PART_FK4 | Non Unique | Default | COORDNTR_REQUEST_ID |
| IRC_IS_INTERVIEW_PART_FK5 | Non Unique | Default | INTRVW_REQUESTS_ID |
| IRC_IS_INTERVIEW_PART_PK | Unique | Default | PARTICIPANT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
