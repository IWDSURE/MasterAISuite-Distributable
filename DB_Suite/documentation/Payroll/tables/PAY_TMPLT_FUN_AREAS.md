# PAY_TMPLT_FUN_AREAS

Functional are contains various patterns for a given feature. A template can have various functional areas to segregate data provided by this solution. E.g. A Payroll element template can have a functional area for the back dated pay and another for advance pay.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltfunareas-26122.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltfunareas-26122.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_FUN_AREAS_PK | FUN_AREA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FUN_AREA_ID | NUMBER |  | 18 | Yes | FUN_AREA_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | TEMPLATE_ID |
| FUN_AREA_NAME | VARCHAR2 | 20 |  | Yes | FUN_AREA_NAME |
| BASE_FUN_AREA_NAME | VARCHAR2 | 20 |  | Yes | BASE_FUN_AREA_NAME |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| DEFAULT_PATTERN_ID | NUMBER |  | 18 |  | DEFAULT_PATTERN_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TMPLT_FUN_AREAS_PK | Unique | Default | FUN_AREA_ID |
| PAY_TMPLT_FUN_AREAS_U1 | Unique | Default | BASE_FUN_AREA_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
