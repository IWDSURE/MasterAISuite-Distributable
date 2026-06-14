# IRC_CMT_LAUNCH_CONTENTS

This table stores message content information for the launch.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunchcontents-17301.html#irccmtlaunchcontents-17301](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunchcontents-17301.html#irccmtlaunchcontents-17301)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CMT_LAUNCH_CONTENTS_PK | CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| BODY_SEARCH_TEXT | VARCHAR2 | 3000 |  |  | Message body in plain text for text search |
| SUBJECT_SEARCH_TEXT | VARCHAR2 | 2500 |  |  | Subject in plain text for text search |
| LAUNCH_ID | NUMBER |  | 18 | Yes | Stores LAUNCH_ID. Foreign Key to IRC_CMT_LAUNCH. |
| SUBJECT | VARCHAR2 | 2000 |  |  | Stores subject part for the message. |
| BODY | CLOB |  |  |  | Stores body part for the message. |
| COMMON_TOKENS | CLOB |  |  |  | Stores common token values for the launch in JSON format. |
| LANGUAGE_CODE | VARCHAR2 | 4 |  |  | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SENDER_EMAIL | VARCHAR2 | 240 |  |  | Sender's email address, which will be used to communicate with the sender. |
| SENDER_DISPLAY_NAME | VARCHAR2 | 240 |  |  | This field holds the display name of the sender. |
| REPLY_TO_EMAIL | VARCHAR2 | 240 |  |  | Email address to which the reply email can be sent. |
| REPLY_TO_DISPLAY_NAME | VARCHAR2 | 240 |  |  | Display Name of the email to which the reply email can be sent. |
| IS_DEFAULT | VARCHAR2 | 1 |  |  | Specifies the contents are default if the preferred language is not available. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CMT_LAUNCH_CONTENTS_FK1 | Non Unique | Default | LAUNCH_ID |
| IRC_CMT_LAUNCH_CONTENTS_PK | Unique | Default | CONTENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
