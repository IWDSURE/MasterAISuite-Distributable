# BEN_DED_SCHED_PY_FREQ

BEN_DED_SCHED_PY_FREQ  correlates a payroll cycle to an activity base rate's  deduction  schedule.  This information is used to determine when comp deductions are  scheduled to be processed for persons assigned to a payroll  cycle.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendedschedpyfreq-27048.html#bendedschedpyfreq-27048](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendedschedpyfreq-27048.html#bendedschedpyfreq-27048)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DED_SCHED_PY_FREQ_PK | DED_SCHED_PY_FREQ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DED_SCHED_PY_FREQ_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_DED_SCHED_PY_FREQ. |
| PY_FREQ_CD | VARCHAR2 | 30 |  | Yes | Payroll frequency. |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Default Y or N. |
| ACTY_RT_DED_SCHED_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTY_RT_DED_SCHED_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_DED_SCHED_PY_FREQ_N1 | Non Unique | ACTY_RT_DED_SCHED_ID |
| BEN_DED_SCHED_PY_FREQ_PK | Unique | DED_SCHED_PY_FREQ_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
