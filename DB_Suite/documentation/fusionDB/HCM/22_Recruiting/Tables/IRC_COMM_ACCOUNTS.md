# IRC_COMM_ACCOUNTS

Stores all the accounts of the communication providers.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccommaccounts-27091.html#irccommaccounts-27091](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccommaccounts-27091.html#irccommaccounts-27091)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_COMM_ACCOUNTS_PK | COMM_ACCOUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMM_ACCOUNT_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| FOOTER_TEXT_ENABLED_FLAG | VARCHAR2 | 1 |  |  | To enable or disable footer text in an outbound SMS message |
| FOOTER_TEXT | VARCHAR2 | 1000 |  |  | Footer text in an oubound SMS message |
| ACCOUNT_GUID | VARCHAR2 | 64 |  | Yes | Application generated GUID of the provider account. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the communication provider account. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | Description for the communication provider account. |
| ACCOUNT_CONFIG | CLOB |  |  |  | Communication provider account  configuration information  including credentials of the account. |
| STATUS_CODE | VARCHAR2 | 40 |  | Yes | Status of the communication provider account.The corresponding lookup type is IRC_COMM_ACCOUNT_STATUS_TYPE. |
| MESSAGE_MAX_LENGTH | NUMBER |  | 6 |  | Max length for a message set by provider. |
| COMM_PROVIDER_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_COMM_PROVIDERS |
| DELETE_MSG_ON_READ_FLAG | VARCHAR2 | 1 |  |  | Determine whether the messages for this account should be delete after they are read. |
| ENABLE_TWO_WAY_COMM_FLAG | VARCHAR2 | 1 |  |  | Determine whether the messages for this account supports 2 way sms communication |
| AGENT_COMM_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether agent communication is enabled for the account or not. |
| COMM_ACCOUNT_TYPE | VARCHAR2 | 32 |  |  | Type of the communication provider account.Determine whether account provider is Recruiting provider or Communicate provider. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_COMM_ACCOUNTS_FK1 | Non Unique | Default | COMM_PROVIDER_ID |
| IRC_COMM_ACCOUNTS_PK | Unique | Default | COMM_ACCOUNT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
