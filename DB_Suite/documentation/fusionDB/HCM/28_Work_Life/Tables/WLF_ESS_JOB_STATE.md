# WLF_ESS_JOB_STATE

Table to store state information of ess jobs

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfessjobstate-14860.html#wlfessjobstate-14860](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfessjobstate-14860.html#wlfessjobstate-14860)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_ess_job_state_PK | JOB_STATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_STATE_ID | NUMBER |  | 18 | Yes | JOB_STATE_ID |
| JOB_ID | NUMBER |  | 18 | Yes | JOB_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| STATE | CLOB |  |  |  | STATE |
| SAVE_POINT_ID | NUMBER |  | 9 |  | SAVE_POINT_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| JOB | VARCHAR2 | 400 |  |  | The Job is composed of the ESS Job Package and Job Def |
| STATE_CLASSNAME | VARCHAR2 | 400 |  |  | The fully qualified java classname for the Job State object, used for unmarshalling |
| CONTEXT_TYPE | VARCHAR2 | 30 |  |  | The Job Context Type |
| CONTEXT_INFO | VARCHAR2 | 30 |  |  | The Job Context INFO |
| PARENT_JOB_ID | NUMBER |  | 18 |  | ESS Job Id of the this Job's parent. null if this is a Parent Job |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| wlf_ess_job_state_N1 | Non Unique | Default | JOB, CONTEXT_TYPE, CONTEXT_INFO |
| wlf_ess_job_state_N2 | Non Unique | Default | PARENT_JOB_ID, UPPER("CONTEXT_INFO") |
| wlf_ess_job_state_U1 | Unique | Default | JOB_ID |
| wlf_ess_job_state_U2 | Unique | Default | JOB_STATE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
