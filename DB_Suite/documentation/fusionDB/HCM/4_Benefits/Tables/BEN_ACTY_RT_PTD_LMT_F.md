# BEN_ACTY_RT_PTD_LMT_F

BEN_ACTY_RT_PTD_LMT_F identifies what period to date limits apply to an activity base rate.  Example, the employee payroll deduction for a specific savings plan is subjected to a maximum  year to date limit which restricts the maximum contributions allowed for this and other such plans. BEN_ACTY_RT_PTD_LMT_F is the intersection of BEN_ACTY_BASE_RT_F  and BEN_PTD_LMT_F.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactyrtptdlmtf-13250.html#benactyrtptdlmtf-13250](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactyrtptdlmtf-13250.html#benactyrtptdlmtf-13250)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ACTY_RT_PTD_LMT_F_PK | ACTY_RT_PTD_LMT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTY_RT_PTD_LMT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F. |
| PTD_LMT_ID | NUMBER |  | 18 |  | Foreign key to BEN_PTD_LMT_F. |
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
| BEN_ACTY_RT_PTD_LMT_F_N1 | Non Unique | ACTY_BASE_RT_ID |
| BEN_ACTY_RT_PTD_LMT_F_N2 | Non Unique | PTD_LMT_ID |
| BEN_ACTY_RT_PTD_LMT_F_PK | Unique | ACTY_RT_PTD_LMT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
