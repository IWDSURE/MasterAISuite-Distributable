# IRC_CMT_RECIPIENTS

This table stores recipient information for the launch.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtrecipients-18367.html#irccmtrecipients-18367](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtrecipients-18367.html#irccmtrecipients-18367)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CMT_RECIPIENTS_PK | RECIPIENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RECIPIENT_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |  |
| LAUNCH_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the LAUNCH_TYPE_CODE. For eg. ORA_JOB_ALERTS. |  |
| LAUNCH_ID | NUMBER |  | 18 | Yes | Stores LAUNCH_ID. Foreign Key to IRC_CMT_LAUNCHES. |  |
| PERSON_ID | NUMBER |  | 18 |  | Stores PERSON_ID of the recipient. Foreign Key to PER_PERSONS. |  |
| DELIVERY_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores delivery channel for the message. Stores delivery type as a lookup code. |  |
| ADDRESS_ID | NUMBER |  | 18 |  | Stores recipient (Email) Address Id of the recipient. Foreign Key to PER_EMAIL_ADDRESS. |  |
| ADDRESS | VARCHAR2 | 240 |  |  | Stores recipient (Email) Address of the recipient. |  |
| PREFERRED_LANGUAGE_CODE | VARCHAR2 | 4 |  |  | Stores preferred language of the recipient. |  |
| TOKEN_ID | NUMBER |  | 18 |  | Stores TOKEN_ID. This column is not used. | Obsolete |
| TOKENS | CLOB |  |  |  | Stores tokens for the recipient. |  |
| MSG_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores status of the message. Stores message status as a lookup code. |  |
| MSG_SENT_TS | TIMESTAMP |  |  |  | Stores message sent time  for this message. |  |
| MSG_DELIVERY_TS | TIMESTAMP |  |  |  | Stores delivery time  for this message. |  |
| MSG_OPEN_TS | TIMESTAMP |  |  |  | Stores open time  for this message. |  |
| MSG_BOUNCE_TS | TIMESTAMP |  |  |  | Stores bounce time for this message. |  |
| MSG_UNSENT_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the reason for not sending the message. It holds different types of unsent reasons as lookup codes. 
      - For emails, it uses the lookup type: ORA_IRC_CMT_MSG_UNSENT_TYPE.
      - For SMS, it uses the lookup type: ORA_HCO_SMS_DELIVERY_TYPE. |  |
| MSG_BOUNCE_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the type of the bounce. Stores bounce type as a lookup code.It uses the lookup type:  ORA_IRC_CMT_MSG_BOUNCE_TYPE |  |
| MSG_BOUNCE_REASON | VARCHAR2 | 2048 |  |  | Stores the reason for the bounce. |  |
| MSG_RETRY_COUNT | NUMBER |  |  |  | stores current message retry count. |  |
| UMS_MSG_ID | VARCHAR2 | 256 |  |  | Stores Unified Message Service (UMS) message Id. |  |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Stores the ESS Job Request ID of the current recipient row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_CMT_RECIPIENTS_FK1 | Non Unique | Default | LAUNCH_ID | Obsolete |
| IRC_CMT_RECIPIENTS_FK2 | Non Unique | Default | PERSON_ID, LAUNCH_ID |  |
| IRC_CMT_RECIPIENTS_FK3 | Non Unique | Default | ADDRESS_ID |  |
| IRC_CMT_RECIPIENTS_N1 | Non Unique | Default | LAUNCH_ID, MSG_STATUS_CODE, MSG_UNSENT_TYPE_CODE, MSG_RETRY_COUNT |  |
| IRC_CMT_RECIPIENTS_N2 | Non Unique | Default | UMS_MSG_ID |  |
| IRC_CMT_RECIPIENTS_N3 | Non Unique | Default | MSG_RETRY_COUNT |  |
| IRC_CMT_RECIPIENTS_N4 | Non Unique | Default | MSG_UNSENT_TYPE_CODE |  |
| IRC_CMT_RECIPIENTS_N5 | Non Unique | Default | ESS_REQUEST_ID |  |
| IRC_CMT_RECIPIENTS_PK | Unique | Default | RECIPIENT_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
