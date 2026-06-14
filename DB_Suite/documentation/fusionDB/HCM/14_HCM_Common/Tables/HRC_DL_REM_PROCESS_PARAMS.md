# HRC_DL_REM_PROCESS_PARAMS

When "Remove Person" ESS job is invoked, this table stores information of the corresponding Run Parameters

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremprocessparams-31789.html#hrcdlremprocessparams-31789](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremprocessparams-31789.html#hrcdlremprocessparams-31789)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_PROCESS_PARAMS_PK | PROCESS_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_PARAM_ID | NUMBER |  |  | Yes | PROCESS_PARAM_ID |
| PROCESS_ID | NUMBER |  |  | Yes | PROCESS_ID |
| PARAM_NAME | VARCHAR2 | 100 |  | Yes | PARAM_NAME |
| PARAM_VALUE | VARCHAR2 | 4000 |  | Yes | PARAM_VALUE |
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
| HRC_DL_REM_PROC_PARAMS_N1 | Non Unique | Default | PARAM_NAME, PARAM_VALUE |
| HRC_DL_REM_PROC_PARMS_U1 | Unique | Default | PROCESS_PARAM_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
