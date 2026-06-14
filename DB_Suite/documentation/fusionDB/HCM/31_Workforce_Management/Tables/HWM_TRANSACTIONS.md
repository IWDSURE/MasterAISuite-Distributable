# HWM_TRANSACTIONS

Instances of a process execution to load time records into the workforce management repository

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtransactions-23779.html#hwmtransactions-23779](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtransactions-23779.html#hwmtransactions-23779)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSACTION_ID | NUMBER |  | 18 | Yes | TRANSACTION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PROCESS_ID | NUMBER |  | 18 | Yes | PROCESS_ID |
| PROCESS_MODE_ID | NUMBER |  | 18 |  | PROCESS_MODE_ID |
| TRANSACTION_DATE | DATE |  |  |  | TRANSACTION_DATE |
| PARENT_TRANSACTION_ID | NUMBER |  | 18 |  | PARENT_TRANSACTION_ID |
| STATUS | VARCHAR2 | 60 |  |  | STATUS |
| RUN_IDENTIFIER | VARCHAR2 | 60 |  |  | RUN_IDENTIFIER |
| EXCEPTION_DESCRIPTION | VARCHAR2 | 60 |  |  | EXCEPTION_DESCRIPTION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| DATA_SET_ID | NUMBER |  |  |  | DATA_SET_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TRANSACTIONS_PK | Unique | Default | TRANSACTION_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
