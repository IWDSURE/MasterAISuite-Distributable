# HRC_LOADER_ERROR_LINES

This table will contain the errors for any data that is encountered during a data load.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloadererrorlines-30986.html#hrcloadererrorlines-30986](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloadererrorlines-30986.html#hrcloadererrorlines-30986)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_ERROR_LINES_PK | BATCH_ERROR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ERROR_ID | NUMBER |  | 18 | Yes | BATCH_ERROR_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| LOADER_BATCH_ID | NUMBER |  | 18 | Yes | LOADER_BATCH_ID |
| BATCH_LINE_ID | NUMBER |  | 18 |  | BATCH_LINE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ORIGINATING_SYSTEM | VARCHAR2 | 200 |  |  | ORIGINATING_SYSTEM |
| ROW_STATUS | VARCHAR2 | 100 |  |  | ROW_STATUS |
| MSG_TEXT | VARCHAR2 | 500 |  |  | MSG_TEXT |
| STACKTRACE | VARCHAR2 | 4000 |  |  | STACKTRACE |
| MSG_ERROR_ID | NUMBER |  | 18 |  | MSG_ERROR_ID |
| PARAMETER_01 | VARCHAR2 | 200 |  |  | PARAMETER_01 |
| PARAMETER_02 | VARCHAR2 | 200 |  |  | PARAMETER_02 |
| PARAMETER_03 | VARCHAR2 | 200 |  |  | PARAMETER_03 |
| PARAMETER_04 | VARCHAR2 | 200 |  |  | PARAMETER_04 |
| PARAMETER_05 | VARCHAR2 | 200 |  |  | PARAMETER_05 |
| PARAMETER_06 | VARCHAR2 | 200 |  |  | PARAMETER_06 |
| PARAMETER_07 | VARCHAR2 | 200 |  |  | PARAMETER_07 |
| PARAMETER_08 | VARCHAR2 | 200 |  |  | PARAMETER_08 |
| PARAMETER_09 | VARCHAR2 | 200 |  |  | PARAMETER_09 |
| PARAMETER_10 | VARCHAR2 | 200 |  |  | PARAMETER_10 |
| ERROR_STACK | CLOB |  |  |  | Stores the complete error stack trace. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_ERROR_LINES_N1 | Non Unique | Default | LOADER_BATCH_ID, ORIGINATING_SYSTEM |
| HRC_LOADER_ERROR_LINES_N2 | Non Unique | Default | LOADER_BATCH_ID, BATCH_LINE_ID |
| HRC_LOADER_ERROR_LINES_PK | Unique | Default | BATCH_ERROR_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
