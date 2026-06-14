# HRW_COUNTRY_DIVISION_MATRIX

Used to generate legal entities

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwcountrydivisionmatrix-15340.html#hrwcountrydivisionmatrix-15340](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwcountrydivisionmatrix-15340.html#hrwcountrydivisionmatrix-15340)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_COUNTRY_DIVISION_MATR_PK | CONFIGURATION_ID, COUNTRY_CODE, DIVISION_ENTERPRISE_NAME |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| COUNTRY_CODE | VARCHAR2 | 2 |  | Yes | COUNTRY_CODE |
| DIVISION_ENTERPRISE_NAME | VARCHAR2 | 100 |  | Yes | DIVISION_ENTERPRISE_NAME |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENTERPRISE | VARCHAR2 | 1 |  |  | ENTERPRISE |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_COUNTRY_DIVISION_F2 | Non Unique | Default | LEGAL_ENTITY_ID |
| HRW_COUNTRY_DIVISION_PK | Unique | Default | CONFIGURATION_ID, COUNTRY_CODE, DIVISION_ENTERPRISE_NAME |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
