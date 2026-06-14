# HRT_BATCH_PROCESSES

A batch processes table. To store ESS Jobs

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtbatchprocesses-20251.html#hrtbatchprocesses-20251](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtbatchprocesses-20251.html#hrtbatchprocesses-20251)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_BATCH_PROCESSES_PK | BATCH_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_PROCESS_ID | NUMBER |  | 18 | Yes | Unique Identifier of batch processes |
| PROCESS_TYPE | VARCHAR2 | 64 |  |  | Type of process |
| STATUS_CODE | VARCHAR2 | 64 |  |  | Status code |
| SUBMITTED_BY_USER | VARCHAR2 | 64 |  |  | Submitted by user |
| SUBMITTED_DATE | TIMESTAMP |  |  |  | Date of Submission |
| COMPLETED_DATE | TIMESTAMP |  |  |  | Date of Completion |
| ESS_JOB_ID | NUMBER |  | 18 |  | Identifier of ESS Job |
| ESS_IMPL_CLASS | VARCHAR2 | 240 |  |  | ESS Impl class |
| ESS_APP_MODULE | VARCHAR2 | 240 |  |  | ESS App Module |
| TOTAL_COUNT | NUMBER |  | 18 |  | Total Count |
| FAILED_COUNT | NUMBER |  | 18 |  | Count of Failed Jobs |
| SKIPPED_COUNT | NUMBER |  | 18 |  | Count of skipped Jobs |
| CANCELLED_COUNT | NUMBER |  | 18 |  | Count of cancelled jobs |
| FAILED_IDS | CLOB |  |  |  | ID of failed job |
| SKIPPED_IDS | CLOB |  |  |  | ID of skipped Job |
| CANCELLED_IDS | CLOB |  |  |  | ID of cancelled job |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_BATCH_PROCESSES_PK | Unique | Default | BATCH_PROCESS_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
