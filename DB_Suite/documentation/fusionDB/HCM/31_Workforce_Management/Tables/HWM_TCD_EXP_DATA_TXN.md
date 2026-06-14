# HWM_TCD_EXP_DATA_TXN

This table contains details for Time Clock Device export data for Transactions

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdatatxn-18521.html#hwmtcdexpdatatxn-18521](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdatatxn-18521.html#hwmtcdexpdatatxn-18521)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCD_EXP_DATA_TXN_PK | TCD_EXP_DATA_TXN_ID, TCD_EXP_DATA_TXN_BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCD_EXP_DATA_TXN_ID | NUMBER |  | 18 | Yes | The time device export data transaction id |
| PER_BDG_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | PER_BDG_LAST_UPDATE_DATE |
| DATA_MODE | VARCHAR2 | 30 |  |  | Data collection or export mode like full , updates, specific. |
| STATUS | VARCHAR2 | 20 |  |  | Export or Collection Data Status |
| TCD_EXP_DATA_TXN_TYPE | VARCHAR2 | 15 |  |  | TCD_EXP_DATA_TXN_TYPE |
| TCD_PROC_PROFILE_ID | NUMBER |  | 18 |  | TCD_PROC_PROFILE_ID |
| TCD_SOURCE_ID | VARCHAR2 | 40 |  |  | TCD_SOURCE_ID |
| EXPORT_BATCH_COUNT | NUMBER |  | 9 |  | Number of batches in the data export. |
| TCD_EXP_DATA_TXN_BATCH_ID | NUMBER |  | 9 | Yes | The time device export data transaction batch id |
| TCD_EXP_DATA_DEF_ID | NUMBER |  | 18 |  | The time device export data definition id |
| TCD_EXP_DATA_ESS_PROCESS_ID | NUMBER |  | 18 |  | The time device export data process id |
| EXPORT_BEGIN_TIME | TIMESTAMP |  |  |  | The export begin date and time |
| EXPORT_END_TIME | TIMESTAMP |  |  |  | The export end date and time |
| PER_REC_COUNT | NUMBER |  | 9 |  | The number of person records in a given export transaction and batch |
| PER_BDG_REC_COUNT | NUMBER |  | 9 |  | The number of person badge records in a given export transaction and batch |
| PAY_REC_COUNT | NUMBER |  | 9 |  | The number of payroll records in a given export transaction and batch |
| SCH_REC_COUNT | NUMBER |  | 9 |  | The number of shedule records in a given export transaction and batch |
| PER_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | The latest of last update date for person records in a given export transaction |
| PAY_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | The latest of last update date for payroll records in a given export transaction |
| SCH_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | The latest of last update date for schedule records in a given export transaction |
| SCH_SHFT_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | The latest of last update date for schedule shift records in a given export transaction |
| SCH_SHFT_REC_COUNT | NUMBER |  | 9 |  | The number of schedule shift records in a given export transaction and batch |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCD_EXP_DATA_TXN_U1 | Unique | Default | TCD_EXP_DATA_TXN_ID, TCD_EXP_DATA_TXN_BATCH_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
