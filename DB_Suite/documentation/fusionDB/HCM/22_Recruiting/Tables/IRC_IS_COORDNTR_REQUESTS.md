# IRC_IS_COORDNTR_REQUESTS

This table stores the interview schedule coordinator requests information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** DEFAULT

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irciscoordntrrequests-12945.html#irciscoordntrrequests-12945](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irciscoordntrrequests-12945.html#irciscoordntrrequests-12945)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_COORDNTR_REQUESTS_PK | COORDNTR_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COORDNTR_REQUEST_ID | NUMBER |  | 18 | Yes | Primary key for this table.System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_SUBMISSIONS table. |
| REQUEST_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status as a lookup code. Lookup value associated with ORA_IRC_IS_COORDNTR_REQUEST_STATUS lookup type. |
| COORDNTR_PERSON_ID | NUMBER |  | 18 | Yes | Person-Id of the user who coordinates the interview schedule.Foreign Key to PER_PERSONS table. |
| REQUESTED_BY_PERSON_ID | NUMBER |  | 18 | Yes | Person-Id of the user who created request to interview schedule to the coordinator.Foreign Key to PER_PERSONS table |
| LOCATION_TYPE_CODE | VARCHAR2 | 32 |  |  | Lookup defined by ORA_IRC_IS_LOCATION_TYPE which can be an interview in person, through phone or through a web conference. |
| MEETING_DURATION_CODE | VARCHAR2 | 32 |  |  | Interview meeting duration.We should use existing lookup ORA_IRC_IS_MEETING_DURATION |
| SCHEDULE_NOTES | CLOB |  |  |  | Stores the notes entered by the request creator. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_COORDNTR_REQUESTS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_IS_COORDNTR_REQUESTS_FK2 | Non Unique | Default | SUBMISSION_ID |
| IRC_IS_COORDNTR_REQUESTS_FK3 | Non Unique | Default | COORDNTR_PERSON_ID |
| IRC_IS_COORDNTR_REQUESTS_FK4 | Non Unique | Default | REQUESTED_BY_PERSON_ID |
| IRC_IS_COORDNTR_REQUESTS_PK | Unique | Default | COORDNTR_REQUEST_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
