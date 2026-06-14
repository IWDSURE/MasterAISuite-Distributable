# IRC_REC_EVENT_INTRV_DTLS

This is the table to store the interview details for an event

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventintrvdtls-10350.html#ircreceventintrvdtls-10350](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventintrvdtls-10350.html#ircreceventintrvdtls-10350)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENT_INTRV_DTLS_PK | INTERVIEW_DETAILS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERVIEW_DETAILS_ID | NUMBER |  | 18 | Yes | Primary key of the table. Auto generated. |
| INTERVIEW_TYPE | VARCHAR2 | 30 |  |  | To store the interview type enum which is internal to the application. |
| EVENT_ID | NUMBER |  | 18 | Yes | To store the event id. Foreign Key to IRC_REC_EVENTS_B. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENT_INTRV_DTLS_FK1 | Non Unique | Default | EVENT_ID |
| IRC_REC_EVENT_INTRV_DTLS_PK | Unique | Default | INTERVIEW_DETAILS_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
