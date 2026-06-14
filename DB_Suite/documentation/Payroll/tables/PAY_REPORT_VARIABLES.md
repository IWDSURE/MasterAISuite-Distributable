# PAY_REPORT_VARIABLES

This holds the information to generate the report via the Archiver processes, such as report template, source data, etc.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportvariables-8614.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportvariables-8614.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REPORT_VARIABLES_PK | REPORT_VARIABLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| REPORT_VARIABLE_ID | NUMBER |  | 18 | Yes | REPORT_VARIABLE_ID |  |
| REPORT_DEFINITION_ID | NUMBER |  | 18 | Yes | REPORT_DEFINITION_ID |  |
| DEFINITION_TYPE | VARCHAR2 | 30 |  | Yes | DEFINITION_TYPE |  |
| NAME | VARCHAR2 | 80 |  | Yes | NAME |  |
| VALUE | VARCHAR2 | 250 |  | Yes | VALUE |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| LEGISLATION_CODE | VARCHAR2 | 150 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REPORT_VARIABLES_PK | Unique | Default | REPORT_VARIABLE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
