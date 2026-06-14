# HRC_ALERT_KEEPS

Contains alert expiry/time to live data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertkeeps-27396.html#hrcalertkeeps-27396](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertkeeps-27396.html#hrcalertkeeps-27396)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_KEEPS_PK | KEEP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| KEEP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| SENT_IN_RUN_ID | NUMBER |  | 18 |  | Used to keep track of messages sent in this runId. |
| ALERT_ID | NUMBER |  | 18 | Yes | Alert Identifier. Foreign Key to HRC_ALERTS_B.ALERT_ID |
| RECIPIENT_ID | NUMBER |  | 18 | Yes | Recipient Identifier. Foreign Key to HRC_ALERT_RECIPIENTS.ALERT_ID |
| SENT_TO | VARCHAR2 | 2000 |  | Yes | Contains who the Keep is for. |
| KEEP_COUNT | NUMBER |  | 18 |  | Specifes number times not sent to recpient |
| EXPIRES_ON | TIMESTAMP |  |  | Yes | The timestamp the Keep expires on |
| HASH_KEY | VARCHAR2 | 200 |  |  | Feed recipient and body hash key. |
| HASH_KEY_VERSION | VARCHAR2 | 80 |  |  | Feed recipient and body hash key version. |
| OBJ_HASH_KEY | VARCHAR2 | 200 |  |  | Object hash key which holds surrogates key hash. |
| OBJ_HASH_KEY_VERSION | VARCHAR2 | 80 |  |  | Object hash key which holds surrogates key hash version. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_KEEPS_FK2 | Non Unique | Default | RECIPIENT_ID |
| HRC_ALERT_KEEPS_N1 | Non Unique | FUSION_TS_TX_DATA | EXPIRES_ON |
| HRC_ALERT_KEEPS_PK | Unique | Default | KEEP_ID |
| HRC_ALERT_KEEPS_U1 | Unique | FUSION_TS_TX_DATA | ALERT_ID, RECIPIENT_ID, SENT_TO, HASH_KEY |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
