# PAY_ASSIGNED_PAYROLLS_DN_

Stores details of which payrolls an employee is assigned to at a point in time. This allows an employee to transition payrolls even when their periods overlap

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payassignedpayrollsdn-17523.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payassignedpayrollsdn-17523.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ASSIGNED_PAYROLLS_DN_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASSIGNED_PAYROLL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNED_PAYROLL_ID | NUMBER |  | 18 | Yes | ASSIGNED_PAYROLL_ID |
| LSED | DATE |  |  |  | LSED |
| LSPD | DATE |  |  |  | LSPD |
| FINC | DATE |  |  |  | FINC |
| FSED | DATE |  |  |  | FSED |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ASSIGNED_PAYROLLS_DNN1_ | Non Unique | Default | ASSIGNED_PAYROLL_ID |
| PAY_ASSIGNED_PAYROLLS_DN_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASSIGNED_PAYROLL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
