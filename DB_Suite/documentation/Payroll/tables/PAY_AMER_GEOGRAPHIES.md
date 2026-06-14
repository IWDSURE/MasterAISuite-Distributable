# PAY_AMER_GEOGRAPHIES

This table contains North America specific payroll geographies (townships and school districts).

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamergeographies-30390.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamergeographies-30390.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_AMER_GEOGRAPHIES_PK | PAYROLL_GEOGRAPHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Unique Identifier for a geography |
| REFERENCE_TYPE | VARCHAR2 | 20 |  |  | REFERENCE_TYPE |
| REFERENCE_CODE | VARCHAR2 | 50 |  |  | REFERENCE_CODE |
| GEO_CODE | VARCHAR2 | 30 |  |  | Geo Code of the Geography |
| GEOGRAPHY_TYPE | VARCHAR2 | 30 |  | Yes | Type of Geography |
| GEOGRAPHY_NAME | VARCHAR2 | 360 |  | Yes | Complete Name of Geography |
| AREA1 | NUMBER |  | 2 | Yes | State Jurisdiction Code |
| AREA2 | NUMBER |  | 3 | Yes | County Jurisdiction Code |
| AREA3 | NUMBER |  | 4 | Yes | City Jurisdiction Code |
| AREA4 | NUMBER |  | 5 |  | School District Code |
| LEGISLATION_CODE | VARCHAR2 | 2 |  | Yes | Code of the country to which the geography belongs |
| START_DATE | DATE |  |  | Yes | Start date from which this geography is valid for use. |
| END_DATE | DATE |  |  | Yes | Date from which this geography is no longer valid. |
| PRIMARY_FLAG | VARCHAR2 | 1 |  |  | Flag indicates whether this name is default for this geography |
| PARENT_GEOGRAPHY_ID | NUMBER |  | 18 |  | Geography Id of County for a geography. Populated only for Townships. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_AMER_GEOGRAPHIES_N1 | Non Unique | Default | AREA1, GEOGRAPHY_TYPE |
| PAY_AMER_GEOGRAPHIES_N2 | Non Unique | Default | TO_CHAR("AREA1"), GEOGRAPHY_TYPE |
| PAY_AMER_GEOGRAPHIES_U1 | Unique | Default | PAYROLL_GEOGRAPHY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
