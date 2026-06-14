# HRC_TXN_HEADER_ARCHIVE

Transaction Model Archive table: contain the archives of changes being made in this transaction

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnheaderarchive-20515.html#hrctxnheaderarchive-20515](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnheaderarchive-20515.html#hrctxnheaderarchive-20515)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_HEADER_ARCHIVE_PK | TRANSACTION_ID, ARCHIVE_STEP_NUMBER |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSACTION_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| IS_TXN_GETTING_PURGED | VARCHAR2 | 20 |  |  | Flag to indicate if archived transaction is a candidate for getting purged. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ARCHIVE_STEP_NUMBER | NUMBER |  | 18 | Yes | This records sequence number within the archived transaction |
| INITIATOR_USER_ID | NUMBER |  | 18 | Yes | The user_id of the user who initiated the transaction |
| APPLICATION_ID | NUMBER |  | 18 | Yes | The identifier of the Application that set up the business data for this transaction |
| MODULE_GROUP | VARCHAR2 | 60 |  | Yes | The Module Group of the module that set up the business data |
| MODULE_IDENTIFIER | VARCHAR2 | 60 |  | Yes | The Module that set up the business data |
| PROCESS_ID | NUMBER |  | 18 |  | Foreign key to HRC_ARM_PROCESS_B |
| OBJECT | VARCHAR2 | 100 |  | Yes | The main database table which will be updated by this transaction |
| OBJECT_ID | NUMBER |  | 18 | Yes | The primary key of the record to be updated on the REFERENCE_TABLE |
| SUBJECT | VARCHAR2 | 100 |  | Yes | The type of the business object being worked on by this transaction, e.g. PERSON |
| SUBJECT_ID | NUMBER |  | 18 | Yes | The unique identifier of the business object being worked on by this transaction, e.g. PERSON_ID |
| PARENT_TRANSACTION_ID | NUMBER |  | 18 |  | Connection to the parent transaction record on this table |
| REENTRY_FUNCTION | VARCHAR2 | 160 |  |  | This column is used to store the Reentry function. |
| PROCESS_OWNER | VARCHAR2 | 30 |  |  | Composite Process this transaction is part of |
| SECTION_DISPLAY_NAME | VARCHAR2 | 500 |  |  | Display Name of the action being performed |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ARCHIVE_DATE | TIMESTAMP |  |  | Yes | Indicates the date and time the transaction record was archived. |
| XML_DATA_CACHE | XMLTYPE |  |  |  | The transaction business data and context, as XML |
| FAMILY | VARCHAR2 | 100 |  | Yes | High level grouping used in TAC searches |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_HEADER_ARCHIVE_PK | Unique | Default | TRANSACTION_ID, ARCHIVE_STEP_NUMBER |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
