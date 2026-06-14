# HWM_TM_REPROCESS_REQUEST

Table for storing the reprocessing data like Status,Source and Reason for time record groups .

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmreprocessrequest-22069.html#hwmtmreprocessrequest-22069](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmreprocessrequest-22069.html#hwmtmreprocessrequest-22069)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REPROCESS_REQUEST_PK | TM_REPROCESS_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REPROCESS_REQUEST_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Refers to TM_REC_GRP_ID in TM_REC_GRP |
| TM_REC_GRP_VERSION | NUMBER |  | 9 | Yes | Refers to TM_REC_GRP_VERSION in TM_REC_GRP |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RESOURCE_ID | NUMBER |  | 18 | Yes | The resource for which the time record group applies. |
| TM_REC_GRP_STATUS | VARCHAR2 | 30 |  | Yes | TM_REC_GRP_STATUS |
| START_TIME | TIMESTAMP |  |  | Yes | START_TIME |
| AUTO_APPROVE | VARCHAR2 | 1 |  | Yes | Contains a (Y/N) value to specify if elegible for Auto Approval |
| REPROCESS_REASON | VARCHAR2 | 1000 |  |  | REPROCESS_REASON |
| REQUIRES_MANUAL_PROCESSING | VARCHAR2 | 1 |  | Yes | Contains a (Y/N) value to specify if it requires manual processing. |
| REPROCESS_REQUEST_TIME | TIMESTAMP |  |  | Yes | The time at which a request has been submitted for re-processing. |
| REPROCESS_SOURCE | VARCHAR2 | 30 |  |  | The source Event/Ess Jod which has triggered request for re-processing |
| REPROCESS_SOURCE_ID | NUMBER |  | 18 |  | The Id for the Event/Ess Job which has triggered request for re-processing |
| REPROCESS_REQUEST_STATUS | NUMBER |  | 2 | Yes | The current status of the request that has been submitted for reprocess |
| REPROCESS_STATUS | NUMBER |  | 2 | Yes | The current status of the Time RecordGroup (row)  that has been submitted for reprocess. |
| RUN_START_TIME | TIMESTAMP |  |  |  | Start time for reprocessing run for the row |
| RUN_END_TIME | TIMESTAMP |  |  |  | End time for reprocessing run for the row |
| RUN_ERROR | VARCHAR2 | 2000 |  |  | Stores error if any that is encountered during reprocessing. |
| LATEST_FLAG | VARCHAR2 | 1 |  | Yes | Indicates if this is the latest entry of the time record group (there will be a unique combination of TM_REC_GRP_ID and LATEST_FLAG). |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REPROCESS_REQUEST_N1 | Non Unique | Default | UPPER("REPROCESS_REASON"), LATEST_FLAG |
| HWM_TM_REPROCESS_REQUEST_N2 | Non Unique | Default | REPROCESS_STATUS, LATEST_FLAG |
| HWM_TM_REPROCESS_REQUEST_N3 | Non Unique | Default | TM_REC_GRP_ID, TM_REC_GRP_VERSION, LATEST_FLAG, REPROCESS_SOURCE_ID, REPROCESS_STATUS, REPROCESS_REASON |
| HWM_TM_REPROCESS_REQUEST_N4 | Non Unique | Default | REPROCESS_SOURCE_ID |
| HWM_TM_REPROCESS_REQUEST_U1 | Unique | Default | TM_REPROCESS_REQUEST_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
