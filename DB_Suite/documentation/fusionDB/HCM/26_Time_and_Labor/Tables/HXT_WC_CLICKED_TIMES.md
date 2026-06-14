# HXT_WC_CLICKED_TIMES

This table stores web clock events and time information clicked by users

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtwcclickedtimes-15941.html#hxtwcclickedtimes-15941](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtwcclickedtimes-15941.html#hxtwcclickedtimes-15941)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_WC_CLICKED_TIMES_PK | WC_CLICKED_TIME_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WC_CLICKED_TIME_ID | NUMBER |  | 18 | Yes | Primary key |
| WORK_FROM_HOME_FLAG | VARCHAR2 | 3 |  |  | Flag for Work From Home |
| DEVICE_TYPE | VARCHAR2 | 30 |  |  | Device Type of the Time Event |
| GEO_LOCATION | VARCHAR2 | 150 |  |  | Geo Coordinates of the time event |
| GEO_LOC_EXCEPTION | VARCHAR2 | 30 |  |  | Indicates the reason why geo coordinates were not captured |
| GEOFENCE_ERROR | VARCHAR2 | 30 |  |  | Identifies why geofence validation failed for web clock event. |
| GEOFENCE_VAL_STATUS | VARCHAR2 | 30 |  |  | Indicates geofence validation succeeded or not for web clock event. |
| TIME_EVENT_ID | NUMBER |  | 18 |  | Stores the Id returned by time event api |
| CLICKED_TIME_STRING | VARCHAR2 | 80 |  | Yes | Stores device time if there is no adjustement else it contains the adjusted time |
| DEVICE_CLICKED_TIME_STRING | VARCHAR2 | 80 |  |  | Stores the initial device time before adjustement. If there is no adjustement, this field is empty |
| CLICKED_SERVER_TIME | TIMESTAMP |  |  | Yes | Stores the server clicked time |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Stores the enterprise id of the user |
| MANUAL_FLAG | VARCHAR2 | 1 |  |  | Y/N. Indicates if the time was entered manually by the worker or not. Considered as 'N' if empty. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_ID | NUMBER |  | 18 | Yes | Stores the person id of the user clicked the event |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Stores the assignment id of the user clicked the event |
| TCLAYFLD_DEFNS_ID | NUMBER |  | 18 | Yes | Id of the Time Card Field |
| TCLAYFLD_DEFNS_INSTANCE_ID | NUMBER |  | 18 | Yes | Id of the TCF used in a layout set |
| CLICKED_TIME | TIMESTAMP |  |  | Yes | Stores the system clicked time |
| SEQUENCE_NUM | NUMBER |  |  |  | The value stored in this column is used for business logic rule |
| REF_TIMEZONE_ID | VARCHAR2 | 50 |  |  | The time zone associated to the Click time |
| TIMEZONE_OFFSET | NUMBER |  | 22 |  | TIMEZONE_OFFSET |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_WC_CLICKED_TIMES_N1 | Non Unique | Default | PERSON_ID |
| HXT_WC_CLICKED_TIMES_N2 | Non Unique | Default | ASSIGNMENT_ID, TRUNC("CLICKED_TIME") |
| HXT_WC_CLICKED_TIMES_N3 | Non Unique | Default | CLICKED_SERVER_TIME |
| HXT_WC_CLICKED_TIMES_U1 | Unique | Default | WC_CLICKED_TIME_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
