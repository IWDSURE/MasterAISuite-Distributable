# HRC_TXN_CONSOLE_ENTRY_ARCHIVE

This table holds Archive Admin console details

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconsoleentryarchive-6032.html#hrctxnconsoleentryarchive-6032](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconsoleentryarchive-6032.html#hrctxnconsoleentryarchive-6032)

## Primary Key

| Name | Columns |
|------|----------|
| hrc_txn_console_entry_arc_PK | CONSOLE_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONSOLE_ENTRY_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| TRANSACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_TXN_HEADER table |
| OBJECT_NAME | VARCHAR2 | 300 |  |  | The presentable name of the main business object being changed |
| PROCESS_CATEGORY | VARCHAR2 | 200 |  |  | The category grouping this process is in e.g. Employment |
| CONSOLE_TXN_STATUS | VARCHAR2 | 30 |  | Yes | The status of the transaction to control how it appears in the Admin Console. |
| STATUS_CATEGORY | VARCHAR2 | 30 |  | Yes | The category of the status like Pending, Completed, Failed, Draft. |
| CHANGE_EFFECTIVE_DATE | DATE |  |  |  | The effective date of the changes in this transaction |
| TASK_ID | VARCHAR2 | 100 |  |  | The TaskId of the main approval request BPM task |
| TASK_STATE | VARCHAR2 | 100 |  |  | The State of the main approval request BPM task |
| TASK_OUTCOME | VARCHAR2 | 100 |  |  | The final outcome of the main approval request BPM task |
| TASK_APPROVERS | VARCHAR2 | 300 |  |  | The list of approvers of the worklist task |
| OVERRIDE_INITIATOR_USER_NAME | VARCHAR2 | 64 |  |  | transaction initiator user name in case it is different than the value in the WHO columns |
| OVERRIDE_IDENTIFICATION_KEY | VARCHAR2 | 100 |  |  | task identification key in case it is different than transaction id or object id. |
| SR_NUMBER | VARCHAR2 | 200 |  |  | User entered SR number relating to this issue |
| HRC_TXN_CUSTOM_VARCHAR_1 | VARCHAR2 | 200 |  |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_VARCHAR_2 | VARCHAR2 | 200 |  |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_VARCHAR_3 | VARCHAR2 | 200 |  |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_VARCHAR_4 | VARCHAR2 | 200 |  |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_NUMBER_1 | NUMBER |  | 18 |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_NUMBER_2 | NUMBER |  | 18 |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_NUMBER_3 | NUMBER |  | 18 |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_NUMBER_4 | NUMBER |  | 18 |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_DATE_1 | DATE |  |  |  | This column has been added to this table for Custom Use. |
| HRC_TXN_CUSTOM_DATE_2 | DATE |  |  |  | This column has been added to this table for Custom Use. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_CONSOLE_ENTRY_ARCH_N1 | Non Unique | HRC_TXN_CONSOLE_ENTRY_ARCH_N1 | TRANSACTION_ID |
| HRC_TXN_CONSOLE_ENTRY_ARCH_N2 | Non Unique | HRC_TXN_CONSOLE_ENTRY_ARCH_N2 | "CREATION_DATE", UPPER("OBJECT_NAME"), UPPER("PROCESS_CATEGORY") |
| HRC_TXN_CONSOLE_ENTRY_ARCH_UK | Unique | Default | CONSOLE_ENTRY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
