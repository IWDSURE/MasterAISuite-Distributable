# PAY_GEOGRAPHY_SPANS

This table contains muliple country/city mappings within a geography.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** DEFAULT

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographyspans-8661.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographyspans-8661.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GEOGRAPHY_SPANS_PK | GEOGRAPHY_SPAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEOGRAPHY_SPAN_ID | NUMBER |  | 18 | Yes | Unique Identifier for geography span. |
| GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Foreign key to pay_geographies. |
| AREA1 | NUMBER |  | 18 |  | State Jurisdiction Code of Geography Span. |
| AREA2 | NUMBER |  | 18 |  | County Jurisdiction Code of Geography Span. |
| AREA3 | NUMBER |  | 18 |  | City Jurisdiction Code of Geography Span. |
| AREA4 | NUMBER |  | 18 |  | School District Code of Geography Span. |
| SPAN_TYPE | VARCHAR2 | 100 |  | Yes | The Span Type of Geography Span. |
| START_RANGE | VARCHAR2 | 30 |  |  | The Start Range of Geography Span. |
| END_RANGE | VARCHAR2 | 30 |  |  | The End Range of Geography Span. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_GEOGRAPHY_SPANS_U1 | Unique | Default | GEOGRAPHY_SPAN_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
