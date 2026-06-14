# HRC_TXN_ATTACHMENT

Transaction Model Attachment table holds the attachment index status added by initiator at review page. These attachments are later populated into SOA BPM instance with their status updated to the table entry.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnattachment-21713.html#hrctxnattachment-21713](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnattachment-21713.html#hrctxnattachment-21713)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_ATTACHMENT_PK | ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHMENT_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| OBJECT_ID | NUMBER |  | 18 |  | Object Id |
| TRANSACTION_ID | NUMBER |  | 18 |  | Foreign Key to HRC_TXN_HEADER table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TASK_ID | VARCHAR2 | 64 |  |  | Stores the task id from worklist application |
| ATTACHMENT_STATUS | VARCHAR2 | 64 |  |  | Status of the attachment |
| ATTACHMENTS_NUMBER | NUMBER |  | 5 |  | Attachments Number |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_ATTACHMENT_FK | Non Unique | Default | TRANSACTION_ID |
| HRC_TXN_ATTACHMENT_PK | Unique | Default | ATTACHMENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
