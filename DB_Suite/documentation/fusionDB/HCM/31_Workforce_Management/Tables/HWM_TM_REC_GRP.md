# HWM_TM_REC_GRP

A grouping of time records, for example, a day groups time records occuring within that day.  A time card groups day time record groups.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrp-28289.html#hwmtmrecgrp-28289](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrp-28289.html#hwmtmrecgrp-28289)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_GRP_PK | TM_REC_GRP_ID, TM_REC_GRP_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| ORIG_TM_REC_GRP_ID | NUMBER |  |  |  | ORIG_TM_REC_GRP_ID : foreign key to retrieve original time record group row |
| ORIG_TM_REC_GRP_VERSION | NUMBER |  |  |  | ORIG_TM_REC_GRP_VERSION : Foreign Key column containing the version of the original time building block. |
| TM_REC_GRP_VERSION | NUMBER |  | 9 | Yes | Primary Key column containing the current version of the time building block.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| GRP_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key |
| COMMIT_TIMESTAMP | TIMESTAMP |  |  |  | Used to find the latest Commit Time.  The same value will be stored in Consumers who deal with repository to  verify if the ID they are having is the latest TRG |
| MEASURE | NUMBER |  |  |  | The measure value of the time building block. |
| LAYER_TM_REC_GRP_ID | NUMBER |  | 18 |  | Foreign Key to a Time Record Group Id in a different layer(Example Raw to Calc Link - if we expec them to be many like this then we should have a usages table). |
| LAYER_TM_REC_GRP_VERSION | NUMBER |  | 9 |  | Foreign key to a TimeRecord Group in a different layer |
| UNIT_OF_MEASURE | VARCHAR2 | 30 |  |  | The units corresponding to the Measure.  HOURS |
| START_TIME | TIMESTAMP |  |  |  | For Range type of building blocks, the start time of the block. |
| STOP_TIME | TIMESTAMP |  |  |  | For Range type of building blocks, the stop time of the block. |
| PARENT_TM_REC_GRP_ID | NUMBER |  | 18 |  | The building block id for the parent block in the time structure hierarchy. |
| PARENT_TM_REC_GRP_VERSION | NUMBER |  | 9 |  | The building block version for the parent block in the time structure hierarchy. |
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

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_TM_REC_GRP_N1 | Non Unique | Default | RESOURCE_ID, LATEST_VERSION, NVL("DELETE_FLAG",'N'), GRP_TYPE_ID, START_TIME, STOP_TIME |  |
| HWM_TM_REC_GRP_N2 | Non Unique | Default | PARENT_TM_REC_GRP_ID, PARENT_TM_REC_GRP_VERSION |  |
| HWM_TM_REC_GRP_N3 | Non Unique | Default | NVL("DELETE_FLAG",'N'), LATEST_VERSION, GRP_TYPE_ID, TRUNC("STOP_TIME"), TRUNC("START_TIME") |  |
| HWM_TM_REC_GRP_N4 | Non Unique | FUSION_TS_TX_IDX | ORIG_TM_REC_GRP_ID, NVL("DELETE_FLAG",'N'), LATEST_VERSION |  |
| HWM_TM_REC_GRP_N5 | Non Unique | FUSION_TS_TX_IDX | NVL("DELETE_FLAG",'N'), GRP_TYPE_ID, TRUNC("STOP_TIME") |  |
| HWM_TM_REC_GRP_N6 | Non Unique | HWM_TM_REC_GRP_N6 | TRUNC("STOP_TIME"), TRUNC("START_TIME") | Obsolete |
| HWM_TM_REC_GRP_U1 | Unique | Default | TM_REC_GRP_ID, TM_REC_GRP_VERSION |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
