# HTS_SCHED_SHIFT_REQUESTS

Table to store the schedule shift requests information.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedshiftrequests-10647.html#htsschedshiftrequests-10647](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedshiftrequests-10647.html#htsschedshiftrequests-10647)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_SHIFT_REQUESTS_PK | SCHED_SHIFT_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_SHIFT_REQUEST_ID | NUMBER |  | 18 | Yes | Schedule shift request transaction identifier. |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Identifier of the schedule to which the shift belongs. |
| SHIFT_DATE | DATE |  |  | Yes | Reference or actual date of the shift. |
| REQUEST_TYPE | VARCHAR2 | 30 |  | Yes | Type of schedule shift request. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person ID who initiated the transaction. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Reference a schedule shift or a shift group in case of Consider Me opportunity requests. |
| OBJECT_TYPE | VARCHAR2 | 20 |  | Yes | Indicates whether object identifier represents shift identifier or group identifier using fixed values SHIFT or GROUP respectively. |
| REASON_CODE | VARCHAR2 | 30 |  |  | Reason code selected by user when submitting the request. |
| REASON_TEXT | VARCHAR2 | 240 |  |  | User entered reason text when reason code is selected as Other. |
| RECIPIENT_SHIFT_ID | NUMBER |  | 18 |  | Indicates the recipient shift identifier in case of swap request |
| RECIPIENT_SHIFT_VERSION | NUMBER |  | 9 |  | Indicates the object version number on the recipient shift at the time of placing this request |
| RECIPIENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | Indicates the assignment identifier on the recipient shift at the time of placing this request. For consider me flow, this is the requestor's assignment identifier. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Indicates the status of the transaction. |
| PARTIAL_REQUEST_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the request is for a partial shift |
| PARTIAL_START_TIME | TIMESTAMP |  |  |  | Stores the requested start time for the partial shift. |
| PARTIAL_END_TIME | TIMESTAMP |  |  |  | Stores the requested end time for the partial shift. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Indicates the enterprise identifier to which this transaction belongs to. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HTS_SCHED_SHIFT_REQUESTS_N1 | Non Unique | Default | SCHEDULE_ID |  |
| HTS_SCHED_SHIFT_REQUESTS_PK | Unique | Default | SCHED_SHIFT_REQUEST_ID |  |
| HTS_SCHED_SHIFT_REQUESTS_U1 | Unique | Default | PERSON_ID, OBJECT_ID, STATUS_CODE | Obsolete |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
