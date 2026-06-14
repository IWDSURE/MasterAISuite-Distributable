# IRC_CAND_EMAIL_MESSAGES

This table stores the emails that are sent and received in the context of an interaction on the Submission, Candidate Pool and Candidate General Profile.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailmessages-13839.html#irccandemailmessages-13839](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailmessages-13839.html#irccandemailmessages-13839)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_EMAIL_MESSAGES_PK | CAND_EMAIL_MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_EMAIL_MESSAGE_ID | NUMBER |  | 18 | Yes | Primary key for the IRC_CAND_EMAIL_MESSAGES table. |
| AGENT_REVIEWED_STATUS | VARCHAR2 | 64 |  |  | Status of the email following the review by the AI Agent. |
| INTERACTION_ID | NUMBER |  | 18 | Yes | Foreign key into the IRC_INTERACTIONS table. Each message is associated to an interaction in this manner. There can be multiple messages associated to an interaction. All the messages in the interaction in turn represents the conversation. |
| SENDER_PERSON_ID | NUMBER |  | 18 | Yes | Foreign key into PER_PERSONS. PersonId for the candidate or recruiter/ hiring manager who is sending this message. |
| SUBJECT | VARCHAR2 | 4000 |  |  | Subject content of message that will be sent. |
| BODY_SNIPPET | VARCHAR2 | 4000 |  |  | Message body snippet for preview on the email summary UI. |
| MESSAGE_IDENTIFIER | VARCHAR2 | 4000 |  | Yes | Denotes a unique Id that is sent along with the message. This is the SMTP Message-Id header for the message sent/received. |
| IN_REPLY_TO_HEADER | VARCHAR2 | 4000 |  |  | The In-Reply-To column denotes the unique message Id that the message in reference is a response to. |
| MESSAGE_DIRECTION | VARCHAR2 | 64 |  | Yes | To distinguish which way the messages are going-- to or from the candidate-- without having to derive the information from SENDER_PERSON_ID and IRC_CAN_MESSAGE_RECIPIENTS. Possible values for this column are ORA_INBOUND or ORA_OUTBOUND. |
| SEND_TIME | TIMESTAMP |  |  | Yes | The time when a message is sent. |
| ESS_JOB_READ_TIME | TIMESTAMP |  |  |  | The time taken for the ESS job to be read |
| DELIVERY_STATUS | VARCHAR2 | 64 |  | Yes | Delivery status of a message that has been sent or received. Different statuses include ORA_UNKOWN, ORA_DELIVERED, ORA_NOT_DELIVERED (at the least these few). |
| READ_FLAG | VARCHAR2 | 1 |  |  | Whether the email has been read by the candidate. |
| BODY_PLAIN_TEXT | CLOB |  |  |  | Stores the Message body in plain text. |
| MASKED_BODY_TEXT | CLOB |  |  |  | Store the body text without PII data |
| BODY_HTML | CLOB |  |  |  | Stores the message body in HTML. |
| REFERENCES_HEADER | CLOB |  |  |  | The References is a store of all the message_ids that are part of the conversation thread for the message sent/received. This is empty for the first message that is sent but should have a value for every subsequent message/interaction in the conversation.  This is important for maintaining the Email Message Headers when replying to  messages from the Messaging UI (this is important for us mimic the behavior of a mail client in order to display a conversation thread in external mailboxes). |
| DELIVERY_ERROR_MESSAGE | CLOB |  |  |  | Error message if the delivery of the message fails. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_EMAIL_MESSAGES_FK1 | Non Unique | Default | INTERACTION_ID |
| IRC_CAND_EMAIL_MESSAGES_FK2 | Non Unique | Default | SENDER_PERSON_ID, TRUNC("CREATION_DATE") |
| IRC_CAND_EMAIL_MESSAGES_N1 | Non Unique | Default | DELIVERY_STATUS, SEND_TIME, CAND_EMAIL_MESSAGE_ID |
| IRC_CAND_EMAIL_MESSAGES_N2 | Non Unique | Default | MESSAGE_IDENTIFIER |
| IRC_CAND_EMAIL_MESSAGES_N3 | Non Unique | Default | TRUNC("CREATION_DATE"), AGENT_REVIEWED_STATUS |
| IRC_CAND_EMAIL_MESSAGES_PK | Unique | Default | CAND_EMAIL_MESSAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
