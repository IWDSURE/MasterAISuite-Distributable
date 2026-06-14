# IRC_CAND_EMAIL_ATTACHMENTS

This table stores the information about email attachements that are sent and received in the context of an interaction on the Submission, Candidate Pool and Candidate General Profile.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailattachments-16874.html#irccandemailattachments-16874](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailattachments-16874.html#irccandemailattachments-16874)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_EMAIL_ATTACHMENTS_PK | CAND_EMAIL_ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_EMAIL_ATTACHMENT_ID | NUMBER |  | 18 | Yes | Primary key for the IRC_CAND_EMAIL_ATTACHMENTS table. |
| CAND_EMAIL_MESSAGE_ID | NUMBER |  | 18 | Yes | Foreign key into the IRC_CAND_EMAIL_MESSAGES table. There can be multiple attachments associated to an email message. Each attachment could be either inline or file attachment. |
| ATTACHED_DOCUMENT_ID | NUMBER |  | 18 |  | Reference to FND_ATTACHED_DOCUMENTS. |
| FILE_NAME | VARCHAR2 | 1000 |  | Yes | Attachment file name part of email |
| CONTENT_TYPE | VARCHAR2 | 256 |  | Yes | Attachment file content type using MIME type |
| FILE_SIZE | NUMBER |  | 18 | Yes | Attachment file size in bytes in the email |
| INLINE_FLAG | VARCHAR2 | 1 |  | Yes | Flag to indicate whether the attachment is inline. |
| CONTENT_ID | VARCHAR2 | 2000 |  |  | Attachment content identification. |
| STATUS | VARCHAR2 | 20 |  | Yes | Status of the attachment whether its uploaded successfully in UCM or errored out |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | Error message when uploading the attachment. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_EMAIL_ATTACHMENTS_FK1 | Non Unique | Default | CAND_EMAIL_MESSAGE_ID |
| IRC_CAND_EMAIL_ATTACHMENTS_PK | Unique | Default | CAND_EMAIL_ATTACHMENT_ID |
| IRC_CAND_EMAIL_ATTACHMENTS_FK2 | Non Unique | Default | ATTACHED_DOCUMENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
