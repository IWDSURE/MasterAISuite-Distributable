# IRC_ERROR_LOGS

Table for logging errors across recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircerrorlogs-4457.html#ircerrorlogs-4457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircerrorlogs-4457.html#ircerrorlogs-4457)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ERROR_LOGS_PK | ERROR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ERROR_ID | NUMBER |  | 18 | Yes | System generated primary key for this entity. |
| ERR_EXTRA_INFO1 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| ERR_EXTRA_INFO2 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| ERR_EXTRA_INFO3 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| ERR_EXTRA_INFO4 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| ERR_EXTRA_INFO5 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| ERR_EXTRA_INFO6 | CLOB |  |  |  | Attribute to store additional information. |
| ERR_EXTRA_INFO7 | CLOB |  |  |  | Attribute to store additional information. |
| OBJECT_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores object type code for the error. Example IRC_OFFERS. |
| OBJECT_ID | NUMBER |  | 18 |  | Stores object Id for the error. Example OFFER_ID. |
| MODULE_CODE | VARCHAR2 | 30 |  |  | Stores module code for the error. Example IRC. |
| MESSAGE_TEXT | VARCHAR2 | 1000 |  |  | Stores message text for the error. |
| MESSAGE_CATEGORY | VARCHAR2 | 60 |  |  | Stores message category for the error. |
| ERROR_STACK | CLOB |  |  |  | Stores error stack of the error. |
| ERROR_MESSAGE_TYPE | VARCHAR2 | 240 |  |  | Stores Error message type - Error or Warning. |
| ERROR_MESSAGE_CODE | VARCHAR2 | 240 |  |  | Stores Error message code from the resource bundle or fnd messages. |
| ERROR_MESSAGE_TOKENS | CLOB |  |  |  | Stores tokens used for the Error message. |
| OCCURANCE_DATE | TIMESTAMP |  |  |  | OCCURANCE_DATE |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Stores status code of the error. Example ORA_ACTIVE, ORA_RESOLVED. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ERROR_LOGS_N1 | Non Unique | Default | OBJECT_TYPE_CODE, OBJECT_ID, MODULE_CODE |
| IRC_ERROR_LOGS_PK | Unique | Default | ERROR_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
