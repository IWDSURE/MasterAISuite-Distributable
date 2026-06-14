# HRC_DL_PROCESS_PARAMS

HRC_DL_PROCESS_PARAMS table gives the details about different parameters corresponding to each process in the HRC_DL_PROCESSES. The parameters are in the fom of name-value pairs. They include all parameters passed from UI or UCM and others.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlprocessparams-21597.html#hrcdlprocessparams-21597](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlprocessparams-21597.html#hrcdlprocessparams-21597)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_DATA_SET_PARAMS_PK | PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_ID | NUMBER |  | 18 | Yes | DATA_SET_PARAM_ID |
| PROCESS_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| PARAM_NAME | VARCHAR2 | 200 |  | Yes | PARAM_NAME |
| PARAM_VALUE | VARCHAR2 | 200 |  |  | PARAM_VALUE |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_PROCESS_PARAMS_F1 | Non Unique | Default | PROCESS_ID |
| HRC_DL_PROCESS_PARAMS_N1 | Non Unique | Default | REQUEST_ID, PARAM_NAME |
| HRC_DL_PROCESS_PARAMS_PK | Unique | Default | PARAM_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
