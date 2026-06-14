# PAY_ENTRY_PCT_DIST

This table contains a percentage break down of an entry value across one or more payroll terms or assignments. These percentages are used for costing. The values have two decimal places of precision and must total 100 exactly across all the rows for the element entry.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payentrypctdist-16673.html#payentrypctdist-16673](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payentrypctdist-16673.html#payentrypctdist-16673)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ENTRY_PCT_DIST_PK | ENTRY_PCT_DIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTRY_PCT_DIST_ID | NUMBER |  | 18 | Yes | ENTRY_PCT_DIST_ID |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  | Yes | END_DATE |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 | Yes | ELEMENT_ENTRY_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| PERCENTAGE | NUMBER |  | 5 |  | PERCENTAGE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ENTRY_PCT_DIST_N1 | Non Unique | Default | ELEMENT_ENTRY_ID |
| PAY_ENTRY_PCT_DIST_PK | Unique | Default | ENTRY_PCT_DIST_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
