# HRC_SUBSCRIPTION_RUN_INFO

Represents subscription run details including the state of pagination for the current run and feed details.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsubscriptionruninfo-22076.html#hrcsubscriptionruninfo-22076](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsubscriptionruninfo-22076.html#hrcsubscriptionruninfo-22076)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SUBSCRIPTION_RUN_INFO_PK | RUN_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_INFO_ID | NUMBER |  | 18 | Yes | Uniquely identifies a run details row. |
| RUN_ID | NUMBER |  | 18 | Yes | Foreign Key to "hrc_subscription_runs".RUN_ID. |
| FEED_PATH | VARCHAR2 | 2000 |  | Yes | The path name for the collection or feed. |
| FEED_RETRIEVAL_TYPE | VARCHAR2 | 20 |  |  | Indicates the feed retreival date type |
| RETRIEVAL_DATE | TIMESTAMP |  |  |  | Indicates the last date and time of the minimum visited pagination update. |
| UPDATED_MIN | TIMESTAMP |  |  |  | Indicates the last date and time of the minimum visited pagination update. |
| PAGE_SIZE | NUMBER |  | 3 |  | Indicates the last visited pagination page size value. |
| PAGE_NUM | NUMBER |  | 3 |  | Indicates the last visited pagination page number value. |
| START_RETRIEVAL_DATE | TIMESTAMP |  |  |  | Indicates the start date and time of the minimum visited pagination update. |
| START_UPDATED_MIN | TIMESTAMP |  |  |  | Indicates the start date and time of the minimum visited pagination update. |
| START_PAGE_SIZE | NUMBER |  | 3 |  | Indicates the start visited pagination page size value. |
| START_PAGE_NUM | NUMBER |  | 3 |  | Indicates the start visited pagination page number value. |
| ENTRY_COUNT | NUMBER |  | 18 |  | Determines the number of entries count for the run. |
| ERROR_COUNT | NUMBER |  | 18 |  | Determines the number of entries error count for the run. |
| FILTER_COUNT | NUMBER |  | 18 |  | Determines the number of entries filter count for the run. |
| RETRY_COUNT | NUMBER |  | 18 |  | Determines the count of retries for the same run with the same status and no new entries found. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SUBSCRIPTION_RUN_INFO_N1 | Non Unique | FUSION_TS_TX_IDX | RUN_ID, FEED_PATH |
| HRC_SUBSCRIPTION_RUN_INFO_PK | Unique | FUSION_TS_TX_IDX | RUN_INFO_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
