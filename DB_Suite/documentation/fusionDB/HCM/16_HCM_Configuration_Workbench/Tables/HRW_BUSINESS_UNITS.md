# HRW_BUSINESS_UNITS

Table to store a business unit definition

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwbusinessunits-20873.html#hrwbusinessunits-20873](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwbusinessunits-20873.html#hrwbusinessunits-20873)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_BUSINESS_UNITS_PK | BUSINESS_UNIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUSINESS_UNIT_ID | NUMBER |  | 18 | Yes | BUSINESS_UNIT_ID |
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| DIMENSION_ONE | VARCHAR2 | 100 |  |  | DIMENSION_ONE |
| DIMENSION_TWO | VARCHAR2 | 100 |  |  | DIMENSION_TWO |
| CODE | VARCHAR2 | 30 |  | Yes | CODE |
| NAME | VARCHAR2 | 100 |  | Yes | NAME |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| WORKER_ASSIGNMENT_ENABLED | VARCHAR2 | 20 |  |  | WORKER_ASSIGNMENT_ENABLED |
| DEFAULT_LEDGER | VARCHAR2 | 100 |  |  | DEFAULT_LEDGER |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| DEFAULT_SETID | VARCHAR2 | 100 |  |  | DEFAULT_SETID |
| REFERENCE_DATA_SET_ID | NUMBER |  | 18 |  | Id for the Default Set Id |
| GENERATED | VARCHAR2 | 1 |  |  | GENERATED |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_BUSINESS_UNITS_F1 | Non Unique | Default | CONFIGURATION_ID |
| HRW_BUSINESS_UNITS_F2 | Non Unique | Default | LOCATION_ID |
| HRW_BUSINESS_UNITS_PK | Unique | Default | BUSINESS_UNIT_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
