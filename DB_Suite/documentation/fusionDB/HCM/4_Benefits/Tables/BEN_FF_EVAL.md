# BEN_FF_EVAL

BEN_FF_EVAL contains statistical data about each formula that was run and its status.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benffeval-23384.html#benffeval-23384](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benffeval-23384.html#benffeval-23384)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_FF_EVAL_PK | REQ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| FORMULA_ID | NUMBER |  | 18 |  | The Formula Foreign key to FF_FORMULAS |
| RUN_TIME | TIMESTAMP |  |  | Yes | Indicates the date and time of the run time of the formula |
| EXECUTE_FLAG | VARCHAR2 | 10 |  |  | The execution status of the formula |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| EVAL_TYPE | VARCHAR2 | 30 |  |  | Indicates the evaluation type of the run. |
| ELIGY_PRFL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ELIGY_PRFL. Used to identify the eligibility profile that is evaluated. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_M. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_FF_EVAL_PK | Unique | Default | REQ_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
