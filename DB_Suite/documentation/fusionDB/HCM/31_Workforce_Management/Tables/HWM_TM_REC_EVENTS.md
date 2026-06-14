# HWM_TM_REC_EVENTS

Time event table for rest service devices.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecevents-27956.html#hwmtmrecevents-27956](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecevents-27956.html#hwmtmrecevents-27956)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_EVENTS_PK | TM_REC_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_EVENT_ID | NUMBER |  | 18 | Yes | TM_REC_EVENT_ID |
| CHANGE_REASON | VARCHAR2 | 64 |  |  | Change reason for attribute change. |
| TM_REC_EVENT_REQ_ID | NUMBER |  |  | Yes | TM_REC_EVENT_REQ_ID |
| TM_REC_ID | NUMBER |  | 18 |  | TM_REC_ID |
| TM_REC_VERSION | NUMBER |  | 9 |  | TM_REC_VERSION |
| START_TIME_STRING | VARCHAR2 | 150 |  |  | START_TIME_STRING |
| STOP_TIME_STRING | VARCHAR2 | 150 |  |  | STOP_TIME_STRING |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| STOP_TIME | TIMESTAMP |  |  |  | STOP_TIME |
| MEASURE | NUMBER |  |  |  | MEASURE |
| UNIT_OF_MEASURE | VARCHAR2 | 30 |  |  | UNIT_OF_MEASURE |
| REPORTER_ID_TYPE | VARCHAR2 | 30 |  | Yes | REPORTER_ID_TYPE |
| REPORTER_ID | VARCHAR2 | 80 |  | Yes | REPORTER_ID |
| PERSON_ID | NUMBER |  |  | Yes | PERSON_ID |
| START_TIMEZONE_CODE | VARCHAR2 | 20 |  |  | START_TIMEZONE_CODE |
| STOP_TIMEZONE_CODE | VARCHAR2 | 20 |  |  | STOP_TIMEZONE_CODE |
| START_GMT_OFFSET | NUMBER |  |  |  | START_GMT_OFFSET |
| STOP_GMT_OFFSET | NUMBER |  |  |  | STOP_GMT_OFFSET |
| SUBRESOURCE_ID | NUMBER |  |  |  | SUBRESOURCE_ID |
| ZONE_TYPE | VARCHAR2 | 20 |  |  | ZONE_TYPE |
| COMMENT_TEXT | VARCHAR2 | 1000 |  |  | COMMENT_TEXT |
| REF_DATE | DATE |  |  |  | REF_DATE |
| EVENT_STATUS | NUMBER |  | 2 | Yes | EVENT_STATUS |
| CRUD_STATUS | NUMBER |  | 2 | Yes | CRUD_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REC_EVENTS_N1 | Non Unique | Default | TM_REC_ID |
| HWM_TM_REC_EVENTS_N2 | Non Unique | Default | PERSON_ID |
| HWM_TM_REC_EVENTS_N4 | Non Unique | Default | TM_REC_EVENT_REQ_ID |
| HWM_TM_REC_EVENTS_N5 | Non Unique | Default | EVENT_STATUS, PERSON_ID |
| HWM_TM_REC_EVENTS_U1 | Unique | Default | TM_REC_EVENT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
