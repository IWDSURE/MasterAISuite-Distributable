# HRR_MEETING_PARTICIPANTS

This meeting table incluedes the list of participants for the meeting.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingparticipants-24344.html#hrrmeetingparticipants-24344](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingparticipants-24344.html#hrrmeetingparticipants-24344)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_MEETING_PARTICIPANTS_PK | MEETING_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEETING_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Primary key to this table. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| MEETING_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_MEETINGS. |
| PARTICIPANT_PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID of the participant. |
| PARTICIPANT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Participant type code with values REVIEWER, DELEGATED_REVIEWER, PARTICIPANT |
| DATA_SUBMISSION_STATUS_CODE | VARCHAR2 | 30 |  |  | Indicates the status of the participants data submission for the meeting. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_MEETING_PARTICIPANTS_FK1 | Non Unique | FUSION_TS_TX_DATA | MEETING_ID |
| HRR_MEETING_PARTICIPANTS_PK | Unique | FUSION_TS_TX_DATA | MEETING_PARTICIPANT_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
