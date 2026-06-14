# PER_EMPL_CHILD_TXN_DATA

This table stores all the child transactions data.This is not a date effective table

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplchildtxndata-9286.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplchildtxndata-9286.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EMPL_CHILD_TXN_DATA_PK | EMPL_CHILD_TXN_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMPL_CHILD_TXN_DATA_ID | NUMBER |  | 18 | Yes | This is a system generated primary key for this table |
| PARENT_TXN_ID | NUMBER |  | 18 | Yes | This is parent transaction id for the child record to be inserted. |
| PARENT_OBJ_ID | NUMBER |  | 18 |  | This is parent object id for the child record to be inserted. |
| CHILD_PERSON_ID | NUMBER |  | 18 |  | This is child person id for the child record to be inserted. |
| CHILD_OBJ_ID | NUMBER |  | 18 |  | This is child object id for the child record to be inserted |
| STATUS | VARCHAR2 | 100 |  |  | This indicates the status of the transaction. |
| COMMENTS | VARCHAR2 | 2000 |  |  | This indicates any specific note for the child transaction record. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EMPL_CHILD_TXN_DATA_U1 | Unique | Default | EMPL_CHILD_TXN_DATA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
