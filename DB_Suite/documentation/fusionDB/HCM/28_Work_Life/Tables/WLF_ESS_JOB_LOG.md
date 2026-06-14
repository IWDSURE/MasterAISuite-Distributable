# WLF_ESS_JOB_LOG

Table to store status and errors from ESS jobs

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfessjoblog-21994.html#wlfessjoblog-21994](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfessjoblog-21994.html#wlfessjoblog-21994)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ESS_JOB_LOG_PK | ESS_JOB_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ESS_JOB_LOG_ID | NUMBER |  | 18 | Yes | Ess job log pk |
| JOB_ID | NUMBER |  | 18 |  | The ess job id |
| LOG_LEVEL | NUMBER |  | 18 |  | Logging level, -1 for severe errors, greater than or equal to 0 for other errors or info |
| LOG | VARCHAR2 | 4000 |  |  | Log message |
| LOG_TIMESTAMP | TIMESTAMP |  |  |  | Timestamp of the log message |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ESS_JOB_LOG_N1 | Non Unique | Default | JOB_ID |
| WLF_ESS_JOB_LOG_U1 | Unique | Default | ESS_JOB_LOG_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
