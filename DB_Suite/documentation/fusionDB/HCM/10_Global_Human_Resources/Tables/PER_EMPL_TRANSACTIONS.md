# PER_EMPL_TRANSACTIONS

This table stores the transaction XML CLOB data.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perempltransactions-30075.html#perempltransactions-30075](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perempltransactions-30075.html#perempltransactions-30075)

## Primary Key

| Name | Columns |
|------|----------|
| per_empl_transactions_PK | EMPL_TRANSACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMPL_TRANSACTION_ID | NUMBER |  | 18 | Yes | This is a system generated primary key for this table. |
| TRANSACTION_ID | NUMBER |  | 18 | Yes | This is parent transaction id for the child record to be inserted. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| EMPL_XML_DATA | XMLTYPE |  |  |  | The transaction business data and context, as EMPL_XML_DATA. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| per_empl_transactions_U1 | Unique | Default | EMPL_TRANSACTION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
