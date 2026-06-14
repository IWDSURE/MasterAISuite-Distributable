# IRC_CAND_EMAIL_RECIPIENTS

This table stores the recipients of an email that is sent or received.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailrecipients-9655.html#irccandemailrecipients-9655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailrecipients-9655.html#irccandemailrecipients-9655)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_EMAIL_RECIPIENTS_PK | CAND_EMAIL_RECIPIENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_EMAIL_RECIPIENT_ID | NUMBER |  | 18 | Yes | Primary key for IRC_CAND_EMAIL_RECIPIENTS table. |
| CAND_EMAIL_MESSAGE_ID | NUMBER |  | 18 | Yes | Foreign key into IRC_CAND_EMAIL_MESSAGES. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key into PER_PERSONS. PersonId for the candidate or recruiter/ hiring manager that is the recipient of this message as part of the interaction. |
| RECIPIENT_TYPE | VARCHAR2 | 40 |  | Yes | Indicates whether the recipient is in the TO, CC, or BCC list. Possible values are TO, CC, BCC. |
| RELAYED_FLAG | VARCHAR2 | 1 |  |  | Indicate whether this recipient was relayed the message, instead of being part of the recipients list on the original message. Important to display to whom the message was forwarded/relayed to when the conversation participant was not part of the senders/ recipients list. |
| RELAYED_MESSAGE_IDENTIFIER | VARCHAR2 | 4000 |  |  | The RelayedMessageIdentifier denotes a unique Id that is sent along with the relayed message. This is populated for every relayed email message with the SMTP MessageId. |
| RELAYED_TIME | TIMESTAMP |  |  |  | Indicate the time that the message was relayed. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_EMAIL_RECIPIENTS_FK1 | Non Unique | Default | CAND_EMAIL_MESSAGE_ID |
| IRC_CAND_EMAIL_RECIPIENTS_FK2 | Non Unique | Default | PERSON_ID |
| IRC_CAND_EMAIL_RECIPIENTS_N1 | Non Unique | Default | RELAYED_MESSAGE_IDENTIFIER |
| IRC_CAND_EMAIL_RECIPIENTS_PK | Unique | Default | CAND_EMAIL_RECIPIENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
