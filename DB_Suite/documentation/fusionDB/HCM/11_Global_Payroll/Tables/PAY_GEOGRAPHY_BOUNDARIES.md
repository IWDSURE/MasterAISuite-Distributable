# PAY_GEOGRAPHY_BOUNDARIES

This table stores the boundareis for the geographies.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** DEFAULT

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographyboundaries-22111.html#paygeographyboundaries-22111](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographyboundaries-22111.html#paygeographyboundaries-22111)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GEOGRAPHY_BOUNDARIES_PK | BOUNDARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BOUNDARY_ID | NUMBER |  | 18 | Yes | Unique Identifier for a Boundary. |
| COUNTRY | VARCHAR2 | 30 |  | Yes | The Country code for the Boundary. |
| AREA1 | VARCHAR2 | 100 |  |  | The State Jurisdiction Code for the Boundary. |
| AREA2 | VARCHAR2 | 100 |  |  | The County Jurisdiction Code for the Boundary. |
| AREA3 | VARCHAR2 | 100 |  |  | The City Jurisdiction Code for the Boundary. |
| AREA4 | VARCHAR2 | 100 |  |  | The School District Code for the Boundary. |
| CATEGORY | VARCHAR2 | 100 |  | Yes | The Category for the boundary. |
| CODE | VARCHAR2 | 100 |  |  | The Geography code for the boundary. |
| NAME | VARCHAR2 | 200 |  | Yes | The Unique Name for the boundary. |
| SOURCE_KEY | VARCHAR2 | 200 |  |  | The Shape File providers unique identifier. |
| BOUNDARY | UDT |  |  |  | Specifies coordinates of the location defined by the boundary. Special datatype required to store. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| TAXING_FLAG | VARCHAR2 | 200 |  |  | Indicates if the region is a taxing jurisdiction. |
| START_DATE | DATE |  |  |  | Start date from which this geography boundary is valid to use. |
| END_DATE | DATE |  |  |  | End date after which this geography boundary is no longer vald. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_GEOGRAPHY_BOUNDARIES_U1 | Unique | Default | BOUNDARY_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
