# HRC_DL_PROCESSES

HRC_DL_PROCESSES table gives the details about different processes or ESS Jobs acting upon the data set or data set business object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlprocesses-26563.html#hrcdlprocesses-26563](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlprocesses-26563.html#hrcdlprocesses-26563)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_PROCESSES_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | PROCESS_ID |
| PROCESS_NAME | VARCHAR2 | 500 |  |  | Process Name |
| PARENT_PROCESS_ID | NUMBER |  | 18 |  | PARENT_PROCESS_ID |
| PROCESS_STATUS | VARCHAR2 | 30 |  |  | Contains data only when process is cancelled. Only allowed value is ORA_CANCELLED |
| CANCEL_REQUESTED | VARCHAR2 | 1 |  | Yes | Identifies if a Cancel is requested for this process |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 |  | DATA_SET_BUS_OBJ_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| UNIT_PROCESS_TIME | NUMBER |  | 18 |  | UNIT_PROCESS_TIME |
| CHECK_POINT | VARCHAR2 | 100 |  |  | Stores the Check Point value for different Processes. Processes include ESS jobs, transfer, import, load and sub child requests |
| LAST_LOGGED_EXECUTION_NUM | NUMBER |  | 8 |  | The last execution attempt that was recorded in the process log |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_PROCESSES_F1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_PROCESSES_F2 | Non Unique | Default | DATA_SET_ID |
| HRC_DL_PROCESSES_F3 | Non Unique | Default | PARENT_PROCESS_ID |
| HRC_DL_PROCESSES_PK | Unique | Default | PROCESS_ID |
| HRC_DL_PROCESSES_U1 | Unique | Default | REQUEST_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
