# IRC_REC_EVENT_INTRV_PARTS

This table stores the event interview participants.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventintrvparts-5811.html#ircreceventintrvparts-5811](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventintrvparts-5811.html#ircreceventintrvparts-5811)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENT_INTRV_PARTS_PK | INTERVIEW_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERVIEW_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Primary Key of the table. Auto generated. |
| INTERVIEW_DETAILS_ID | NUMBER |  | 18 | Yes | To store the interview details id. Foreign Key to IRC_REC_EVENT_INTRV_DTLS. |
| EVENT_POOL_MEMBER_ID | NUMBER |  | 18 | Yes | To store the event pool member id. Foreign Key to IRC_REC_EVENT_POOL_MEMBERS. |
| INTERVIEWER_PERSON_ID | NUMBER |  | 18 |  | To store the interviewer person id. Foreign Key to PER_PERSONS table. |
| PARTICIPANT_PERSON_ID | NUMBER |  | 18 |  | To store the participant person id. Foreign Key to PER_PERSONS table. |
| FEEDBACK_CODE | VARCHAR2 | 30 |  |  | Column to store feedback code for the participant which is configured in HCM_LOOKUP table. The corresponding lookup type is ORA_IRC_REC_EVT_INTR_FDBCK_CD. |
| FEEDBACK_DATE | TIMESTAMP |  |  |  | Stores the date in which the feedback of the participant is submitted. |
| FEEDBACK_COMMENTS | VARCHAR2 | 1000 |  |  | To store the feedback comments entered by the interviewer |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENT_INTRV_PARTS_FK2 | Non Unique | Default | EVENT_POOL_MEMBER_ID |
| IRC_REC_EVENT_INTRV_PARTS_FK3 | Non Unique | Default | INTERVIEWER_PERSON_ID |
| IRC_REC_EVENT_INTRV_PARTS_FK4 | Non Unique | Default | PARTICIPANT_PERSON_ID |
| IRC_REC_EVENT_INTRV_PARTS_N1 | Non Unique | Default | FEEDBACK_CODE |
| IRC_REC_EVENT_INTRV_PARTS_N2 | Non Unique | Default | INTERVIEW_DETAILS_ID, INTERVIEWER_PERSON_ID |
| IRC_REC_EVENT_INTRV_PARTS_PK | Unique | Default | INTERVIEW_PARTICIPANT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
