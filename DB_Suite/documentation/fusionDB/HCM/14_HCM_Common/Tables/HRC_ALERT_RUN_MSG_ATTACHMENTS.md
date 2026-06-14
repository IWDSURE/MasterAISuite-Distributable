# HRC_ALERT_RUN_MSG_ATTACHMENTS

Stores attachments of a message for a run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunmsgattachments-19440.html#hrcalertrunmsgattachments-19440](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunmsgattachments-19440.html#hrcalertrunmsgattachments-19440)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_MSG_ATTACHM_PK | MSG_ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| MSG_ATTACHMENT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| NAME | VARCHAR2 | 2000 |  |  | Attachment Name |  |
| RUN_ID | NUMBER |  | 18 | Yes | Run Identifier. Foreign Key to HRC_ALERTS_RUNS.RUN_ID |  |
| RUN_MESSAGE_ID | NUMBER |  | 18 | Yes | Message Identifier. Foreign Key to HRC_ALERT_RUN_MESSAGES.MESSAGE_ID |  |
| ATTACHMENT_TYPE | VARCHAR2 | 200 |  |  | Attachment type |  |
| MSG_CHAR_DATA | CLOB |  |  |  | Stores Char Data |  |
| MSG_BINARY_DATA | BLOB |  |  |  | Stores Binary Data |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUN_MSG_ATTACH_N1 | Non Unique | Default | RUN_ID |
| HRC_ALERT_RUN_MSG_ATTACH_PK | Unique | Default | MSG_ATTACHMENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
