# PAY_GEOGRAPHIES

This table contains payroll geographies (state, county, city, school district, township and political subdivision)

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographies-23125.html#paygeographies-23125](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographies-23125.html#paygeographies-23125)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GEOGRAPHIES_PK | GEOGRAPHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEOGRAPHY_ID | VARCHAR2 | 18 |  | Yes | Unique Identifier for a geography. |
| COUNTRY_CODE | VARCHAR2 | 30 |  | Yes | The Country Code of the Geography. |
| GEOGRAPHY_TYPE | VARCHAR2 | 100 |  | Yes | Identifies the Type of the Geography. |
| BASE_NAME | VARCHAR2 | 200 |  | Yes | The Base Name of the Geography. |
| DISPLAY_NAME | VARCHAR2 | 200 |  | Yes | The Display Name of the Geography. |
| PRIM_IDENT_TYPE | VARCHAR2 | 50 |  |  | Primary Identity Type of the Geography. |
| PRIM_IDENT_VALUE | VARCHAR2 | 100 |  |  | Primary Identity Value of the Geography. |
| OTHER_IDENTS | VARCHAR2 | 200 |  |  | Other Identity Value of the Geography. |
| AREA1 | NUMBER |  | 18 |  | State Jurisdiction Code of the Geography. |
| AREA2 | NUMBER |  | 18 |  | County Jurisdiction Code of the Geography. |
| AREA3 | NUMBER |  | 18 |  | City Jurisdiction Code of the Geography. |
| AREA4 | NUMBER |  | 18 |  | School District Code of the Geography. |
| GEO_CODE | VARCHAR2 | 100 |  |  | The Geography Code of the Geography. |
| EQV_GEOGRAPHY_ID | NUMBER |  | 18 |  | The Geography Equivalent to the current record. |
| PARENT_GEOGRAPHY_ID | NUMBER |  | 18 |  | Parent Geography of the current record. |
| START_DATE | DATE |  |  |  | Start date from which this geography is valid to use. |
| END_DATE | DATE |  |  |  | End date after which this geography is no longer vald. |
| DISABLED_FLAG | VARCHAR2 | 2 |  |  | Flag indicates whether the geography is valid to use. |
| TCA_GEOGRAPHY_ID | NUMBER |  | 18 |  | Foreign key to hz_geographies table. |
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
|---|---|---|---|
| PAY_GEOGRAPHIES_U1 | Unique | Default | GEOGRAPHY_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
