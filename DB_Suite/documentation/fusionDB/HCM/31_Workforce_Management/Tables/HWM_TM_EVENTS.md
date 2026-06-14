# HWM_TM_EVENTS

This table stores In or Out time transaction reported using a time collection device

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_INTERFACE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmevents-9513.html#hwmtmevents-9513](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmevents-9513.html#hwmtmevents-9513)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_EVENTS_PK | TM_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_EVENT_ID | NUMBER |  | 18 | Yes | TM_EVENT_ID |
| MANUAL_FLAG | VARCHAR2 | 1 |  |  | Y/N. Indicates if the time was entered manually by the worker or not. Considered as 'N' if empty. |
| EVENT_TYPE | VARCHAR2 | 40 |  |  | EVENT_TYPE |
| EVENT_TIME_REAL | TIMESTAMP |  |  | Yes | EVENT_TIME_REAL |
| TIMEZONE_OFFSET | NUMBER |  | 22 |  | TIMEZONE_OFFSET |
| EVENT_TIME_STRING | VARCHAR2 | 150 |  | Yes | EVENT_TIME_STRING,support iso8601 with duration |
| REPORTER_ID | VARCHAR2 | 80 |  | Yes | REPORTER_ID |
| REPORTER_ID_TYPE | VARCHAR2 | 30 |  | Yes | REPORTER_ID_TYPE |
| PERSON_ID | NUMBER |  | 18 |  | person id of the reporter for internal use |
| DEVICE_ID | VARCHAR2 | 40 |  |  | DEVICE_ID |
| TM_EVENT_REQ_ID | NUMBER |  | 18 |  | TM_EVENT_REQ_ID |
| STATUS | VARCHAR2 | 30 |  |  | obsolete (EVENT_STATUS Instead) |
| EVENT_STATUS | NUMBER |  | 2 | Yes | EVENT_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| REF_TIMEZONE_ID | VARCHAR2 | 50 |  |  | The time zone associated to the event time. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_EVENTS_N1 | Non Unique | Default | REPORTER_ID |
| HWM_TM_EVENTS_N2 | Non Unique | Default | TM_EVENT_REQ_ID |
| HWM_TM_EVENTS_N3 | Non Unique | Default | PERSON_ID |
| HWM_TM_EVENTS_N5 | Non Unique | Default | EVENT_STATUS, TRUNC("EVENT_TIME_REAL") |
| HWM_TM_EVENTS_UK1 | Unique | Default | TM_EVENT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
