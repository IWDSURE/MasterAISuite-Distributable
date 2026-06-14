# PAY_AMER_GEOGRAPHY_RANGES

This table contains zip codes for North America specific payroll geographies (townships).

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamergeographyranges-17788.html#payamergeographyranges-17788](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamergeographyranges-17788.html#payamergeographyranges-17788)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_AMER_GEOGRAPHY_RANGES_PK | PAYROLL_GEOGRAPHY_RANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_GEOGRAPHY_RANGE_ID | NUMBER |  | 18 | Yes | Unique Geography Range Identifier |
| GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_AMER_GEOGRAPHIES |
| START_RANGE | VARCHAR2 | 10 |  | Yes | Column for recording the lowest value in the zip code range |
| END_RANGE | VARCHAR2 | 10 |  | Yes | Column for recording the highest value in the zip code range |
| START_DATE | DATE |  |  | Yes | Effective start date of the geographic range |
| END_DATE | DATE |  |  | Yes | Effective end date of the geographic range |
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
|---|---|---|---|
| PAY_AMER_GEOGRAPHY_RANGES_U1 | Unique | Default | PAYROLL_GEOGRAPHY_RANGE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
