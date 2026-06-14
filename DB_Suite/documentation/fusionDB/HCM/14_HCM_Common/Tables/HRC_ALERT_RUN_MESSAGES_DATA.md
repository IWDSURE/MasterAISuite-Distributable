# HRC_ALERT_RUN_MESSAGES_DATA

Stores alert messages to be sent for a run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunmessagesdata-31477.html#hrcalertrunmessagesdata-31477](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunmessagesdata-31477.html#hrcalertrunmessagesdata-31477)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_MSG_DATA_PK | RUN_MESSAGE_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_MESSAGE_DATA_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| RUN_ID | NUMBER |  | 18 | Yes | Run Identifier. Foreign Key to HRC_ALERT_RUNS.RUN_ID |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Template Identifier. Foreign Key to HRC_ALERT_TEMPLATES.TEMPLATE_ID |
| MESSAGE_SEQ | NUMBER |  | 18 |  | Identifies the message sequence. |
| MESSAGE_LANGUAGE | VARCHAR2 | 8 |  |  | Message Lanugage. |
| SUBJECT | VARCHAR2 | 2000 |  |  | Specifies the Subject. |
| BODY | CLOB |  |  |  | Specifies the  message body. |
| STATUS | VARCHAR2 | 30 |  |  | Specifies the message status. Valid values are defined in the lookup ORA_HRC_ALERT_MESSAGE_STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUN_MESSAGES_DATA_N1 | Non Unique | Default | RUN_ID |
| HRC_ALERT_RUN_MESSAGES_DATA_N2 | Non Unique | Default | TEMPLATE_ID |
| HRC_ALERT_RUN_MESSAGES_DATA_PK | Unique | Default | RUN_MESSAGE_DATA_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
