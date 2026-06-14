# BEN_ACTY_RT_DED_SCHED_F

BEN_ACTY_RT_DED_SCHED_F  identifies the deduction schedule(s) to used  to control how frequently a contribution-related activity base rate is to be deducted. BEN_ACTY_RT_DED_SCHED_F is the intersection of BEN_ACTY_BASE_RT_F  and BEN_DED_SCHED_PY_FREQ.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactyrtdedschedf-19856.html#benactyrtdedschedf-19856](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactyrtdedschedf-19856.html#benactyrtdedschedf-19856)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ACTY_RT_DED_SCHED_F_PK | ACTY_RT_DED_SCHED_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTY_RT_DED_SCHED_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| DED_SCHED_PY_FREQ_ID | NUMBER |  | 18 |  | Foreign key to PAY_DED_SCHED_PY_FREQ. |
| ACTY_BASE_RT_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTY_BASE_RT_F. |
| DED_SCHED_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DED_SCHED_CD | VARCHAR2 | 30 |  | Yes | Deduction schedule. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ACTY_RT_DED_SCHED_F_FK2 | Non Unique | Default | DED_SCHED_PY_FREQ_ID |
| BEN_ACTY_RT_DED_SCHED_F_N2 | Non Unique | Default | ACTY_BASE_RT_ID |
| BEN_ACTY_RT_DED_SCHED_F_PK | Unique | Default | ACTY_RT_DED_SCHED_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
