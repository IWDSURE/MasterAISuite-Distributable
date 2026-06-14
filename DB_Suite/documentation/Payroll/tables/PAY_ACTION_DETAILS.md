# PAY_ACTION_DETAILS

This stores the overall processing details of an Action performed by the Processes.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactiondetails-27594.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactiondetails-27594.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_DETAILS_PK | ACTION_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_DETAIL_ID | NUMBER |  | 18 | Yes | Surrogate Primary Key |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to the Payroll Action |
| NAME | VARCHAR2 | 80 |  | Yes | Name of the value stored |
| VALUE | VARCHAR2 | 30 |  | Yes | Recorded Value |
| UOM | VARCHAR2 | 30 |  | Yes | Unit of Measure. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| THREAD_NUMBER | NUMBER |  | 18 |  | Worker identifier |
| PROCESS_ACTION_ID | NUMBER |  | 18 |  | PROCESS_ACTION_ID |
| PARENT_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to Pay Action Details |
| DIMENSION1 | VARCHAR2 | 150 |  |  | Business Dimension of the Value |
| DIMENSION2 | VARCHAR2 | 150 |  |  | Business Dimension of the Value |
| DIMENSION3 | VARCHAR2 | 150 |  |  | Business Dimension of the Value |
| DIMENSION4 | VARCHAR2 | 150 |  |  | Business Dimension of the Value |
| DIMENSION5 | VARCHAR2 | 150 |  |  | Business Dimension of the Value |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign Key to Enterprises |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ACTION_DETAILS_N1 | Non Unique | Default | PAYROLL_ACTION_ID |
| PAY_ACTION_DETAILS_N2 | Non Unique | Default | REQUEST_ID |
| PAY_ACTION_DETAILS_U1 | Unique | Default | ACTION_DETAIL_ID |
| PAY_ACTION_DETAILS_UK1 | Unique | Default | ACTION_DETAIL_ID, NAME |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
