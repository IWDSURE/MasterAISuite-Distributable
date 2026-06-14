# IRC_IM_QSTNR_ATTCHMNTS

This table stores the attachments related to a questionnaire for a selected pariticpant.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimqstnrattchmnts-4364.html#ircimqstnrattchmnts-4364](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimqstnrattchmnts-4364.html#ircimqstnrattchmnts-4364)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_QSTNR_ATTCHMNTS_PK | QSTNR_ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_ATTACHMENT_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| FEEDBACK_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_IM_FDBACK_PRCPNS table. |
| ATTACHMENT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the attachment type as a lookup code. |
| ATTACHMENT_ID | NUMBER |  | 18 |  | Foreign key to FND_DOCUMENT_ENTITIES table. |
| FEEDBACK_REQUEST_ID | NUMBER |  | 18 |  | Foreign key to IRC_IM_FDBACK_REQUESTS table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IM_QSTNR_ATTCHMNTS_FK1 | Non Unique | Default | FEEDBACK_REQUEST_ID |
| IRC_IM_QSTNR_ATTCHMNTS_FK2 | Non Unique | Default | FEEDBACK_PARTICIPANT_ID |
| IRC_IM_QSTNR_ATTCHMNTS_PK | Unique | Default | QSTNR_ATTACHMENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
