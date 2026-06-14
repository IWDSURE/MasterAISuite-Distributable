# HRC_ALERT_RUN_RECIPIENTS

Contains Alert Run Recipients data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunrecipients-13660.html#hrcalertrunrecipients-13660](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunrecipients-13660.html#hrcalertrunrecipients-13660)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_RECEIPIENTS_PK | RUN_RECIPIENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RUN_RECIPIENT_ID | NUMBER |  | 18 | Yes | System generated primary column | Active |
| RUN_MESSAGE_ID | NUMBER |  | 18 | Yes | Message Identifier. Foreign Key to HRC_ALERT_RUN_MESSAGES.MESSAGE_ID | Active |
| RUN_ID | NUMBER |  | 18 |  | Run Identifier. Foreign Key to HRC_ALERTS_RUNS.RUN_ID |  |
| RECIPIENT_ID | NUMBER |  | 18 | Yes | Recipient Identifier. Foreign Key to HRC_ALERT_RECIPIENTS.RECIPENT_ID | Active |
| STATUS | VARCHAR2 | 30 |  |  | Determines if the message was sent. Valid values are defined in lookup of 
HRC_ALERT_MESSAGE_STATUS | Active |
| SENT_TO | VARCHAR2 | 2000 |  |  | Contains who the message was delivered to. | Active |
| SENT_ON | TIMESTAMP |  |  |  | The timestamp the message was sent. | Active |
| EXT_MSG_TYPE | VARCHAR2 | 30 |  |  | Specifies external Message Type. possible values ORA_WL, ORA_EM |  |
| EXT_MSG_ID | VARCHAR2 | 200 |  |  | Specifies external Message Identifier. Foreign Key to BPELNOTIFICATION.WFTASKID OR MESSAGE.MESSAGEID |  |
| ENTRY_ID | NUMBER |  | 18 |  | Entry Identifier. Foreign Key to HRC_ATOM_ENTRIES.ENTRY_ID | Active |
| HASH_KEY | VARCHAR2 | 200 |  |  | Feed recipient and body hash key. |  |
| HASH_KEY_VERSION | VARCHAR2 | 80 |  |  | Feed recipient and body hash key version |  |
| OBJ_HASH_KEY | VARCHAR2 | 200 |  |  | Object hash key which holds surrogates key hash. |  |
| OBJ_HASH_KEY_VERSION | VARCHAR2 | 80 |  |  | Object hash key which holds surrogates key hash version. |  |
| CHUNK_NUM | NUMBER |  | 18 |  | Chunk Number |  |
| CHUNK_STATUS | VARCHAR2 | 80 |  |  | Chunk Status , Possible values : NEW, IN-PROCESS, SUCCESS, ERROR |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_ALERT_RUN_RECIPIENTS_N3 | Non Unique | Default | RUN_ID |  |
| HRC_ALERT_RUN_RECIPIENTS_N4 | Non Unique | Default | CHUNK_NUM, CHUNK_STATUS |  |
| HRC_ALERT_RUN_RECIPIENTS_PK | Unique | FUSION_TS_TX_IDX | RUN_RECIPIENT_ID | Active |
| HRC_ALERT_RUN_RECIPIENT_FK1 | Non Unique | FUSION_TS_TX_IDX | RUN_MESSAGE_ID | Active |
| HRC_ALERT_RUN_RECIPIENT_FK2 | Non Unique | FUSION_TS_TX_IDX | RECIPIENT_ID | Active |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
