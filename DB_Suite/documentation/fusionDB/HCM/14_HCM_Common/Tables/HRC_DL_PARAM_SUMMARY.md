# HRC_DL_PARAM_SUMMARY

HRC_DL_PARAM_SUMMARY table is populated with values of parameters at the time of Import and Load process for each business object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlparamsummary-24774.html#hrcdlparamsummary-24774](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlparamsummary-24774.html#hrcdlparamsummary-24774)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_PARAM_SUMMARY_PK | PARAM_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_SUMMARY_ID | NUMBER |  | 18 | Yes | PARAM_SUMMARY_ID |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 |  | DATA_SET_BUS_OBJ_ID |
| PROCESS_ID | NUMBER |  | 18 |  | PROCESS_ID |
| PARAM_NAME | VARCHAR2 | 200 |  | Yes | PARAM_NAME |
| PARAM_VALUE | VARCHAR2 | 200 |  | Yes | PARAM_VALUE |
| PARAM_SOURCE | VARCHAR2 | 30 |  |  | PARAM_SOURCE |
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
| HRC_DL_PARAM_SUMMARY_N1 | Non Unique | Default | DATA_SET_ID |
| HRC_DL_PARAM_SUMMARY_N2 | Non Unique | Default | DATA_SET_BUS_OBJ_ID, PROCESS_ID, PARAM_NAME |
| HRC_DL_PARAM_SUMMARY_U1 | Unique | Default | PARAM_SUMMARY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
