# HRC_SUBSCRIPTION_RUNS

Represents subscription runs and its status with requestor information.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsubscriptionruns-6259.html#hrcsubscriptionruns-6259](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsubscriptionruns-6259.html#hrcsubscriptionruns-6259)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SUBSCRIPTION_RUNS_PK | RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ID | NUMBER |  | 18 | Yes | Uniquely identifies a subscription run row. |
| RUN_TYPE | VARCHAR2 | 30 |  | Yes | Determines the Run Type. The valid values are FEED, QUEUE |
| LATEST_RUN | VARCHAR2 | 30 |  |  | Determines if the latest run. The valid values are Y, N |
| PROCESS_ID | VARCHAR2 | 200 |  | Yes | Unique identifier for grouping feeds. |
| PARENT_RUN_ID | NUMBER |  | 18 |  | Foreign Key to "hrc_subscription_runs".RUN_ID. |
| PROCESS_NAME | VARCHAR2 | 200 |  | Yes | Uniquely identifies a subscription run row. |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | Determines the Run Type. The valid values are FEED, QUEUE |
| USER_IDENTIFIER | VARCHAR2 | 2000 |  |  | Identifies the user for the run row. |
| START_TIME | TIMESTAMP |  |  |  | Indicates the start date and time of the run. |
| END_TIME | TIMESTAMP |  |  |  | Indicates the end date and time of the run. |
| MSG_COUNT | NUMBER |  | 18 |  | Determines the number of messages processed for the run. |
| STATUS | VARCHAR2 | 30 |  |  | Determines the status of the activity run. |
| STATUS_DETAILS | VARCHAR2 | 2000 |  |  | Determines the status details of the activity run. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SUBSCRIPTION_RUNS_N1 | Non Unique | FUSION_TS_TX_IDX | RUN_TYPE, PROCESS_ID, LATEST_RUN |
| HRC_SUBSCRIPTION_RUNS_N2 | Non Unique | FUSION_TS_TX_IDX | USER_IDENTIFIER |
| HRC_SUBSCRIPTION_RUNS_PK | Unique | FUSION_TS_TX_IDX | RUN_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
