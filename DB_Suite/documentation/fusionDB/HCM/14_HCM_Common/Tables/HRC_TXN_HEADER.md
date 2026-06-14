# HRC_TXN_HEADER

Transaction Model table: the top level record identifying the change being made in this transaction. This holds the cached changes recorded from the users data entry.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnheader-25192.html#hrctxnheader-25192](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnheader-25192.html#hrctxnheader-25192)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_HEADER_PK | TRANSACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSACTION_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| FAMILY | VARCHAR2 | 100 |  | Yes | High level grouping used in TAC searches |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| INITIATOR_USER_ID | NUMBER |  | 18 | Yes | The user_id of the user who initiated the transaction |
| APPLICATION_ID | NUMBER |  | 18 | Yes | The identifier of the Application that set up the business data for this transaction |
| MODULE_GROUP | VARCHAR2 | 60 |  | Yes | The Module Group of the module that set up the business data |
| MODULE_IDENTIFIER | VARCHAR2 | 60 |  | Yes | The Module that set up the business data |
| XML_DATA_CACHE | XMLTYPE |  |  |  | The transaction business data and context, as XML_DATA_CACHE |
| PROCESS_ID | NUMBER |  | 18 |  | Foreign key to HRC_ARM_PROCESS_B |
| OBJECT | VARCHAR2 | 100 |  | Yes | The main database table which will be updated by this transaction |
| OBJECT_ID | NUMBER |  | 18 | Yes | The primary key of the record to be updated on the REFERENCE_TABLE |
| SUBJECT | VARCHAR2 | 100 |  | Yes | The type of the business object being worked on by this transaction, e.g. PERSON |
| SUBJECT_ID | NUMBER |  | 18 | Yes | The unique identifier of the business object being worked on by this transaction, e.g. PERSON_ID |
| PARENT_TRANSACTION_ID | NUMBER |  | 18 |  | Connection to the parent transaction record on this table |
| REENTRY_FUNCTION | VARCHAR2 | 160 |  |  | Proxy handler |
| PROCESS_OWNER | VARCHAR2 | 30 |  |  | Composite Process this transaction is part of |
| SECTION_DISPLAY_NAME | VARCHAR2 | 500 |  |  | Display Name of the action being performed |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| IS_TXN_GETTING_ARCHIVED | VARCHAR2 | 20 |  |  | IS_TXN_GETTING_ARCHIVED |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_HEADER_N1 | Non Unique | Default | APPLICATION_ID |
| HRC_TXN_HEADER_N2 | Non Unique | Default | SUBJECT, SUBJECT_ID |
| HRC_TXN_HEADER_N3 | Non Unique | Default | OBJECT_ID, OBJECT |
| HRC_TXN_HEADER_N4 | Non Unique | Default | MODULE_GROUP, MODULE_IDENTIFIER |
| HRC_TXN_HEADER_N5 | Non Unique | Default | INITIATOR_USER_ID |
| HRC_TXN_HEADER_N6 | Non Unique | Default | PARENT_TRANSACTION_ID |
| HRC_TXN_HEADER_N8 | Non Unique | HRC_TXN_HEADER_N8 | UPPER("CREATED_BY"), "CREATION_DATE" |
| HRC_TXN_HEADER_N9 | Non Unique | HRC_TXN_HEADER_N9 | PROCESS_ID, "CREATION_DATE" |
| HRC_TXN_HEADER_PK | Unique | Default | TRANSACTION_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
