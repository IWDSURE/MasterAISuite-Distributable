# WLF_EMAIL_MESSAGES

Table to store the email messages

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfemailmessages-9809.html#wlfemailmessages-9809](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfemailmessages-9809.html#wlfemailmessages-9809)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_EMAIL_MESSAGES_PK | EMAIL_MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMAIL_MESSAGE_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| PROVIDER_MESSAGE_ID | VARCHAR2 | 1000 |  | Yes | Provider given unique identifier for an email message |
| FAMILY | VARCHAR2 | 80 |  | Yes | Specifies the product family associated with the internet account. |
| THREAD_ID | VARCHAR2 | 512 |  | Yes | Unique identifier for an email message thread. |
| ACCOUNT_ID | NUMBER |  | 18 | Yes | Specifies the account that is setup from "Manage Internet Accounts" UI |
| PROVIDER_CODE | VARCHAR2 | 30 |  | Yes | Lookup Code that specifies email provider. (e.g., GMAIL/MSGRAPH) |
| FULL_MESSAGE | CLOB |  |  | Yes | Complete email message in "full" mode |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_EMAIL_MESSAGES_N1 | Non Unique | Default | ACCOUNT_ID |
| WLF_EMAIL_MESSAGES_N2 | Non Unique | Default | PROVIDER_CODE, PROVIDER_MESSAGE_ID |
| WLF_EMAIL_MESSAGES_U1 | Unique | Default | EMAIL_MESSAGE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
