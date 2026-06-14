# HRC_DL_PROCESS_SUMMARY

HRC_DL_PROCESS_SUMMARY table gives the details about different processes or ESS Jobs acting upon the data set or data set business object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlprocesssummary-16855.html#hrcdlprocesssummary-16855](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlprocesssummary-16855.html#hrcdlprocesssummary-16855)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_PROCESS_SUMMARY_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | PROCESS_ID |
| PARENT_PROCESS_ID | NUMBER |  | 18 |  | PARENT_PROCESS_ID |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 |  | DATA_SET_BUS_OBJ_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROCESS_NAME | VARCHAR2 | 30 |  |  | PROCESS_NAME |
| TOTAL_COUNT | NUMBER |  | 9 | Yes | TOTAL_COUNT |
| SUCCESS_COUNT | NUMBER |  | 9 | Yes | SUCCESS_COUNT |
| ERROR_COUNT | NUMBER |  | 9 | Yes | ERROR_COUNT |
| UNPROCESSED_COUNT | NUMBER |  | 9 | Yes | UNPROCESSED_COUNT |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| END_TIME | TIMESTAMP |  |  |  | END_TIME |
| ELAPSED_TIME | VARCHAR2 | 108 |  |  | ELAPSED_TIME |
| THREADS_ALLOCATED | NUMBER |  | 9 |  | THREADS_ALLOCATED |
| THREADS_USED | NUMBER |  | 9 |  | THREADS_USED |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FILE_LOAD_ACTION | VARCHAR2 | 120 |  |  | FILE_LOAD_ACTION |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_PROCESS_SUMMARY_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_PROCESS_SUMMARY_N2 | Non Unique | Default | DATA_SET_ID |
| HRC_DL_PROCESS_SUMMARY_N3 | Non Unique | Default | PARENT_PROCESS_ID |
| HRC_DL_PROCESS_SUMMARY_U1 | Unique | Default | REQUEST_ID |
| HRC_DL_PROCESS_SUMMARY_U2 | Unique | Default | PROCESS_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
