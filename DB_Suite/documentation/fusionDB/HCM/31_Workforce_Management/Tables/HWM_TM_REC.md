# HWM_TM_REC

An amount or range of time used within workforce management, which is associated with various attributes describing what occurred during that time.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrec-7451.html#hwmtmrec-7451](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrec-7451.html#hwmtmrec-7451)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_PK | TM_REC_ID, TM_REC_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_ID | NUMBER |  |  | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| TM_REC_ROW_ID | NUMBER |  |  |  | Unique row  to track payroll processing status |
| GRP_TYPE_ID | NUMBER |  | 18 |  | Foreign Key |
| ACTIVITY_IN_ID | NUMBER |  | 18 |  | Foreign Key to Activity Type record |
| ACTIVITY_OUT_ID | NUMBER |  | 18 |  | Foreign key to out type activity time record |
| ORIG_TM_REC_ID | NUMBER |  |  |  | ORIG_TM_REC_ID : foreign key to retrieve original time record row |
| ORIG_TM_REC_VERSION | NUMBER |  |  |  | ORIG_TM_REC_VERSION : Foreign Key column containing the version of the original time building block. |
| TM_REC_VERSION | NUMBER |  | 9 | Yes | Primary Key column containing the current version of the time building block.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_REC_TYPE | VARCHAR2 | 30 |  | Yes | Indicates if the block is 'RANGE' or 'MEASURE' |
| ACTIVITY_TYPE | VARCHAR2 | 30 |  |  | ACTIVITY_TYPE |
| ACTIVITY_EVENT_TIME | TIMESTAMP |  |  |  | ACTIVITY_EVENT_TIME |
| MEASURE | NUMBER |  |  |  | The measure value of the time building block. |
| UNIT_OF_MEASURE | VARCHAR2 | 30 |  |  | The units corresponding to the Measure.  HOURS |
| START_TIME | TIMESTAMP |  |  |  | For Range type of building blocks, the start time of the block. |
| STOP_TIME | TIMESTAMP |  |  |  | For Range type of building blocks, the stop time of the block. |
| REF_DATE | DATE |  |  |  | The day to which the record logically belongs when the start and stop times span multiple days. |
| USER_STATUS | VARCHAR2 | 30 |  |  | USER_STATUS |
| DELETE_FLAG | VARCHAR2 | 1 |  |  | DELETE_FLAG |
| LAYER_CODE | VARCHAR2 | 20 |  |  | LAYER_CODE |
| COMMENT_TEXT | VARCHAR2 | 2000 |  |  | Notes for communicating additional information about the time. |
| RESOURCE_ID | NUMBER |  | 18 |  | The resource for which the time building block applies. |
| RESOURCE_TYPE | VARCHAR2 | 30 |  |  | The type of resource, such as a person. |
| SUBRESOURCE_ID | NUMBER |  | 18 |  | SUBRESOURCE_ID |
| TIME_REPORTER_ID | NUMBER |  | 18 |  | The person who reported the time |
| DATE_FROM | TIMESTAMP |  |  |  | Start date of row |
| DATE_TO | TIMESTAMP |  |  |  | End date of row |
| ORDER_ENTERED | NUMBER |  | 18 |  | ORDER_ENTERED |
| TCSMR_SET_ID | NUMBER |  | 18 |  | The set of Time Consumers that will process this block.  This set of Time Consumers is a subset of the Time Consumers covered the the TCSMR_CONFIG_SET_ID. |
| TCSMR_CONFIG_SET_ID | NUMBER |  | 18 |  | The configuration of time consumers to be used when processing this block |
| DATA_SET_ID | NUMBER |  | 18 |  | Used for archiving |
| LATEST_VERSION | VARCHAR2 | 1 |  |  | Indicates if this is the most recent version of the time building block. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| START_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | The time zone associated to the start time. |
| STOP_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | The time zone associated to the stop time. |
| START_GMT_OFFSET | NUMBER |  | 22 |  | The number of hours the start time is offset from GMT. |
| STOP_GMT_OFFSET | NUMBER |  | 22 |  | The number of hours the stop time is offset from GMT. |
| ZONE_TYPE | VARCHAR2 | 30 |  |  | A code to indicate if the time is associated to a zone or an offset. |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| ACTUAL_DATE | DATE |  |  |  | Used to save the owned date . |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REC_N1 | Non Unique | Default | LATEST_VERSION, TCSMR_SET_ID, ENTERPRISE_ID |
| HWM_TM_REC_N2 | Non Unique | Default | START_TIME, STOP_TIME, RESOURCE_ID |
| HWM_TM_REC_N3 | Non Unique | Default | NVL("DELETE_FLAG",'N'), LATEST_VERSION, GRP_TYPE_ID, TRUNC("STOP_TIME"), TRUNC("START_TIME") |
| HWM_TM_REC_N4 | Non Unique | Default | RESOURCE_ID, GRP_TYPE_ID, START_TIME, STOP_TIME |
| HWM_TM_REC_U1 | Unique | FUSION_TS_TX_DATA | TM_REC_ID, TM_REC_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
