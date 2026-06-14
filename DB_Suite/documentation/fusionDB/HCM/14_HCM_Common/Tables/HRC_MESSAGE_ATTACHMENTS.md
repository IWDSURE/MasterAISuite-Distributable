# HRC_MESSAGE_ATTACHMENTS

This is the table where attachment information of each communication messages will be stored. The attachment information will be stored as base64.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_message_attachments

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageattachments-25660.html#hrcmessageattachments-25660](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageattachments-25660.html#hrcmessageattachments-25660)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_ATTACHMENTS_PK | ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHMENT_ID | NUMBER |  | 18 | Yes | Unique Id for the file attached as part of communication process |
| COMMUNICATION_ID | NUMBER |  | 18 |  | Unique Id for identifying the communication message |
| FILE_NAME | VARCHAR2 | 100 |  |  | Indicates the name of the attached file. |
| CONTENT | CLOB |  |  |  | Content of the attachment in base64 format. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTACHMENT_KEY | VARCHAR2 | 50 |  |  | Unique key for the file attached as part of communication process |
| MIME_TYPE | VARCHAR2 | 100 |  |  | Indicates the type of attachment and content type of attachment. |
| FOLDER_PATH | VARCHAR2 | 300 |  |  | Indicate the path of the folder structure where the attachment is stored. |
| VERSION | NUMBER |  |  |  | Indicates the version number of the file attached via the communication process. |
| ATTACHMENT_TYPE | VARCHAR2 | 50 |  |  | Indicate the type of the attachment whether ucm or fnd etc. |
| ATTACHMENT_SIZE | NUMBER |  |  |  | Indicates the value of the size of attachment given |
| URI | VARCHAR2 | 2000 |  |  | Indicates the value of uri or url given as part of the communication process |
| DO_SENDER_HAVE_ACCESS | VARCHAR2 | 1 |  |  | Indicates whether the sender is having access for this specific attachment or not. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_ATTACHMENTS_FK1 | Non Unique | HRC_MESSAGE_ATTACHMENTS_FK1 | COMMUNICATION_ID |
| HRC_MESSAGE_ATTACHMENTS_PK | Unique | HRC_MESSAGE_ATTACHMENTS_PK | ATTACHMENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
