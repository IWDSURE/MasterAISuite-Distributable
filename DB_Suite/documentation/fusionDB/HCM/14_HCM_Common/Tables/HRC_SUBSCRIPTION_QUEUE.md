# HRC_SUBSCRIPTION_QUEUE

Represents subscription run message details and holds the queueing, processing statuses.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsubscriptionqueue-22726.html#hrcsubscriptionqueue-22726](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsubscriptionqueue-22726.html#hrcsubscriptionqueue-22726)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SUBSCRIPTION_QUEUE_PK | RUN_MSG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_MSG_ID | NUMBER |  | 18 | Yes | Uniquely identifies a subscription message row. |
| RUN_ID | NUMBER |  | 18 |  | Foreign Key to "hrc_subscription_runs".RUN_ID. |
| ENTRY_ID | VARCHAR2 | 50 |  | Yes | Collection GUID ATOM Identifier value. |
| PARENT_MSG_ID | NUMBER |  | 18 |  | Entry Identifier. Foreign Key to HRC_SUBSCRIPTION_QUEUE.RUN_MSG_ID |
| MSG_REF_TYPE | VARCHAR2 | 30 |  |  | Message Reference Type , eg: ORA_FP |
| MSG_REF_KEY | VARCHAR2 | 2000 |  |  | Message Reference Key, eg: HRC_ATOMPUB_COLLECTIONS.FEED_PATH |
| UPDATED | TIMESTAMP |  |  | Yes | Updated entry timestamp. Can be set to a future time. |
| PUBLISHED | TIMESTAMP |  |  | Yes | Indicates the date and time of the creation of the entry. |
| QUEUEING_STATUS | VARCHAR2 | 30 |  |  | Determines the queueing status of the activity run. Valid values are NEW, READY, QUEUED DELIVERED |
| PROCESSING_STATUS | VARCHAR2 | 30 |  |  | Determines the queueing status of the activity run. Valid values are NEW, CHECKING, RETRY, SUCCESS, ERROR |
| STATUS_DETAILS | VARCHAR2 | 2000 |  |  | Determines the status details of the processing. Valid values are QUEUEING_STATUS, PROCESSING_STATUS |
| NO_OF_RETRIES | NUMBER |  | 2 |  | Determines for number times the message is verified for a successful status. |
| NEXT_RETRY_TIME | TIMESTAMP |  |  |  | Determines the time when a retry can occur. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SUBSCRIPTION_QUEUE_N1 | Non Unique | FUSION_TS_TX_IDX | RUN_ID, QUEUEING_STATUS |
| HRC_SUBSCRIPTION_QUEUE_N2 | Non Unique | FUSION_TS_TX_IDX | RUN_ID, PROCESSING_STATUS |
| HRC_SUBSCRIPTION_QUEUE_N3 | Non Unique | FUSION_TS_TX_IDX | RUN_ID, ENTRY_ID |
| HRC_SUBSCRIPTION_QUEUE_N4 | Non Unique | Default | RUN_ID, PARENT_MSG_ID |
| HRC_SUBSCRIPTION_QUEUE_N5 | Non Unique | Default | PARENT_MSG_ID, MSG_REF_TYPE, MSG_REF_KEY |
| HRC_SUBSCRIPTION_QUEUE_PK | Unique | FUSION_TS_TX_IDX | RUN_MSG_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
