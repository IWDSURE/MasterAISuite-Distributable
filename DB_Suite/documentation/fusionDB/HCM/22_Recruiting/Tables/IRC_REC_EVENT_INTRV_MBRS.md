# IRC_REC_EVENT_INTRV_MBRS

This table is used to store the interview members associated with the interview for an event

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventintrvmbrs-13957.html#ircreceventintrvmbrs-13957](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventintrvmbrs-13957.html#ircreceventintrvmbrs-13957)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENT_INTRV_MBRS_PK | INTERVIEW_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERVIEW_MEMBER_ID | NUMBER |  | 18 | Yes | The Primary Key of the table. Auto generated. |
| INTERVIEW_DETAILS_ID | NUMBER |  | 18 | Yes | To store the interview details id. Foreign Key to IRC_REC_EVENT_INTRV_DTLS. |
| INTERVIEWER_PERSON_ID | NUMBER |  | 18 | Yes | To store the interviewer person id. Foreign Key to PER_PERSONS table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENT_INTRV_MBRS_FK2 | Non Unique | Default | INTERVIEWER_PERSON_ID |
| IRC_REC_EVENT_INTRV_MBRS_N1 | Non Unique | Default | INTERVIEW_DETAILS_ID, INTERVIEWER_PERSON_ID |
| IRC_REC_EVENT_INTRV_MBRS_PK | Unique | Default | INTERVIEW_MEMBER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
