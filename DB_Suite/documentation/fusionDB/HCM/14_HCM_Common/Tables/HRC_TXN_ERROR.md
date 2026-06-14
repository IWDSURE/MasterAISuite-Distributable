# HRC_TXN_ERROR

HRC_TXN_ERROR table is used to store the Warnings/Errors of a transaction that got in transaction framework code.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnerror-21755.html#hrctxnerror-21755](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnerror-21755.html#hrctxnerror-21755)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_ERROR_PK | ERROR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ERROR_ID | NUMBER |  | 18 | Yes | Primary Key to the current table. |  |
| TRANSACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_TXN_HEADER table. |  |
| FAULT_CODE | VARCHAR2 | 20 |  |  | Category of the Warnings/Errors |  |
| TASK_ID | VARCHAR2 | 64 |  |  | Errors/Warnings  got with a TaskId of the Notification | Obsolete |
| ECID | VARCHAR2 | 100 |  |  | Errors/Warnings  got with a Ecid of the Composite | Obsolete |
| COMPOSITE_INSTANCE_ID | VARCHAR2 | 100 |  |  | Errors/Warnings  got with a Composite instance Id of the Composite | Obsolete |
| COMPOSITE | VARCHAR2 | 100 |  |  | Errors/Warnings  got with a Composite instance Id of the Composite | Obsolete |
| COMPOSITE_VERSION | VARCHAR2 | 34 |  |  | Errors/Warnings  got with a Composite version of the Composite | Obsolete |
| COMPONENT | VARCHAR2 | 100 |  |  | functional component of the Error/Warning |  |
| ERROR_SOURCE | VARCHAR2 | 32 |  | Yes | The source of the Error or Warning |  |
| FAULTED_OPERATION | VARCHAR2 | 32 |  |  | The action from which the Error/Warning occurred |  |
| ERROR_DETAILS | CLOB |  |  |  | More details of the Error/Warning |  |
| FAULT_DATE | TIMESTAMP |  |  | Yes | The date on which the Fault has occured. |  |
| IS_RECOVERABLE | VARCHAR2 | 5 |  |  | Flag to indicate whether the Error/Warning is recoverable or not |  |
| STATUS | VARCHAR2 | 20 |  | Yes | The Status of the Error or Warning |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the process belongs.  
Foreign key to PER_ENTERPRISES. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_ERROR_FK1 | Non Unique | Default | TRANSACTION_ID |
| HRC_TXN_ERROR_U1 | Unique | Default | ERROR_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
