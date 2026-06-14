# IRC_CAND_ACTIONS

This table contains information about candidate that requires asynchronous confirmation.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandactions-29467.html#irccandactions-29467](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandactions-29467.html#irccandactions-29467)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_ACTIONS_PK | CAND_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_ACTION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key association with IRC_CANDIDATES table. Required to retrieve (store/delete) the updated Email address for a particular candidate once the candidate confirms the new Email either via mail or CSS. |
| ACTION_CODE | VARCHAR2 | 64 |  | Yes | Action specifies the purpose of the row in the new table.
For e.g. If it stores updated email address, then the value would be UPDATE_EMAIL. |
| ACTION_PAYLOAD | VARCHAR2 | 1000 |  |  | This is used to store non-PII information. |
| ACTION_SECURE_PAYLOAD | VARCHAR2 | 1000 |  |  | This is used to store PII data. For e.g. When new email is entered, the email is stored in this column. |
| ACTION_STATUS_CODE | VARCHAR2 | 64 |  | Yes | This field along with 'ACTION_PAYLOAD' gives us the current status of a candidate's action. |
| ACTION_START_DATE | TIMESTAMP |  |  | Yes | Stores the timestamp when the Action was triggered. This is one of two columns to track the progress made on the Action. |
| ACTION_END_DATE | TIMESTAMP |  |  |  | Stores the timestamp when the Action was completed/withdrawn. This is one of two columns to track the progress made on the Action. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_COUNT | NUMBER |  | 9 |  | Counter to track number of times a candidate tries to perform an action. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_ACTIONS_PK | Unique | Default | CAND_ACTION_ID |
| IRC_CAND_ACTIONS_UK1 | Unique | Default | PERSON_ID, ACTION_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
