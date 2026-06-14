# HRY_PAYROLL_ACT_PURGE_INFO

For Storing information about extract payroll action for purge process.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypayrollactpurgeinfo-9146.html#hrypayrollactpurgeinfo-9146](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypayrollactpurgeinfo-9146.html#hrypayrollactpurgeinfo-9146)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRY_PAYROLL_ACT_PURGE_INFO_ID | NUMBER |  | 18 |  | ID Value for table hry_payroll_act_purge_info |
| TEMPORARY_ACTION_FLAG | VARCHAR2 | 2 |  |  | This is Object Action type O,P and T for given payroll action id |
| EXT_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to table PAY_PAYROLL_ACTIONS |
| PPA_ROW_ID | VARCHAR2 | 80 |  |  | Stores ROW_ID of table PAY_PAYROLL_ACTIONS |
| REPORT_CATEGORY_ID | NUMBER |  | 18 |  | Report Category Id of pay_payroll_actions record. |
| PPA_EFFECTIVE_DATE | DATE |  |  |  | Effective Date of table pay_payroll_actions record. |
| EXTRACT_TYPE | VARCHAR2 | 8 |  |  | Extract Run Type Full F or Incremental I. |
| RETENTION_PERIOD | NUMBER |  | 10 |  | No. of days for retaining the extract run results. |
| CHANGES_ONLY_RETAIN_ROWS | NUMBER |  | 10 |  | Retain Rows Applicable To Changes Only Extacts. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PAYROLL_ACT_PURGE_INFO_U1 | Unique | Default | HRY_PAYROLL_ACT_PURGE_INFO_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
