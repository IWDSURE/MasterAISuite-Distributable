# HRC_ALERT_RUN_RECIPIENTS_DATA

Stores recipients data for a run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunrecipientsdata-22279.html#hrcalertrunrecipientsdata-22279](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunrecipientsdata-22279.html#hrcalertrunrecipientsdata-22279)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_RECIP_DATA_PK | RUN_RECIPIENT_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_RECIPIENT_DATA_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| RECIPIENT_SEQ | NUMBER |  | 18 |  | Used no of recipients evaluated for recipient expression |
| RUN_ID | NUMBER |  | 18 | Yes | Run Identifier. Foreign Key to HRC_ALERTS_RUNS.RUN_ID |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Template Identifier. Foreign Key to HRC_ALERT_TEMPLATES.TEMPLATE_ID |
| RECIPIENT_ID | NUMBER |  | 18 | Yes | Recipient Identifier. Foreign Key to HRC_ALERT_RECIPIENTS.RECIPENT_ID |
| RECIPIENT_EXPR_VAL | VARCHAR2 | 2000 |  |  | Recipient Expression value |
| RECIPIENT_LANG_PREF | VARCHAR2 | 8 |  | Yes | Recipient Preference Language |
| GROUP_BY_EXPR_VAL | VARCHAR2 | 2000 |  |  | Recipient Group By Expression value |
| BASE_LANG_FILTER_DATA_ID | NUMBER |  | 18 | Yes | Node Identifier. Foreign Key to HRC_ALERT_RUN_FILTERS_DATA.FILTER_DATA_ID |
| RUN_MESSAGE_DATA_ID | NUMBER |  | 18 |  | Message Identifier. Foreign Key to HRC_ALERT_RUN_MESSAGES.MESSAGE_ID |
| REPLICATE_STATUS | VARCHAR2 | 20 |  |  | Replicate Status Possible values are B (Base Recipient),R - Replicated Recipient |
| EXT_MSG_TYPE | VARCHAR2 | 30 |  |  | Specifies external Message Type. possible values ORA_WL, ORA_EM |
| EXT_MSG_ID | VARCHAR2 | 200 |  |  | Specifies external Message Identifier. Foreign Key to BPELNOTIFICATION.WFTASKID OR MESSAGE.MESSAGEID |
| HASH_KEY | VARCHAR2 | 200 |  |  | Feed recipient and body hash key. |
| HASH_KEY_VERSION | VARCHAR2 | 80 |  |  | Feed recipient and body hash key version. |
| OBJ_HASH_KEY | VARCHAR2 | 200 |  |  | Object hash key which holds surrogates key hash. |
| OBJ_HASH_KEY_VERSION | VARCHAR2 | 80 |  |  | Object hash key which holds surrogates key hash version. |
| CHUNK_NUM | NUMBER |  | 18 |  | Chunk Number |
| CHUNK_STATUS | VARCHAR2 | 80 |  |  | Chunk Status , Possible values : NEW, IN-PROCESS, SUCCESS, ERROR |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUN_RECIPS_DATA_N1 | Non Unique | Default | RUN_ID, CHUNK_NUM, CHUNK_STATUS |
| HRC_ALERT_RUN_RECIPS_DATA_N2 | Non Unique | Default | RUN_ID, BASE_LANG_FILTER_DATA_ID |
| HRC_ALERT_RUN_RECIPS_DATA_N3 | Non Unique | Default | RUN_ID, TEMPLATE_ID, GROUP_BY_EXPR_VAL, RECIPIENT_LANG_PREF, REPLICATE_STATUS |
| HRC_ALERT_RUN_RECIPS_DATA_PK | Unique | Default | RUN_RECIPIENT_DATA_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
