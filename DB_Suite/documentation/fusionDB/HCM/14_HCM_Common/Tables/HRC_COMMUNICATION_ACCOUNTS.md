# HRC_COMMUNICATION_ACCOUNTS

This table stores configuration data of the email accounts from which emails will be read for two way communication.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_communication_accounts

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationaccounts-9543.html#hrccommunicationaccounts-9543](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationaccounts-9543.html#hrccommunicationaccounts-9543)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_COMMUNICATION_ACCOUNTS_PK | ACCOUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCOUNT_ID | NUMBER |  | 18 | Yes | Unique Identifier to identify the email entry record |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CLIENT_CONFIGURATION | CLOB |  |  |  | Compilation of client related details as a json string |
| FOLDERS | VARCHAR2 | 500 |  |  | Folders from which email has to be read in case of email communication. |
| SOURCE | VARCHAR2 | 200 |  |  | identifier for the source of the account creation |
| CALLBACK_CLASS | VARCHAR2 | 200 |  |  | identifier for any associated callback class with the account |
| ACCOUNT_IDENTIFIER | VARCHAR2 | 200 |  |  | identifier from the consumer who created the account |
| IS_PROCESS_SPECIFIC | VARCHAR2 | 1 |  |  | flag to identify if created account is specific to a process |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise id against which this email entry record has been created |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| PROVIDER | VARCHAR2 | 20 |  |  | Identifier to recognize the email client type like gmail/outlook |
| ADDRESS | VARCHAR2 | 200 |  |  | Email address from which the messages have to be read |
| IS_ACTIVE | VARCHAR2 | 1 |  |  | Flag that indicates if the communication account is active |
| SCHEDULED_JOB_ID | VARCHAR2 | 18 |  |  | ID of the job which is responsible for polling the mail box. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMMUNICATION_ACCOUNTS_PK | Unique | HRC_COMMUNICATION_ACCOUNTS_PK | ACCOUNT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
