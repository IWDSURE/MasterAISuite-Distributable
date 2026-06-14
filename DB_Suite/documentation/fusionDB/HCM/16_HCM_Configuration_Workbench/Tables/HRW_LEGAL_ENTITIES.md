# HRW_LEGAL_ENTITIES

Table to store A legal entity definition

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwlegalentities-8269.html#hrwlegalentities-8269](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwlegalentities-8269.html#hrwlegalentities-8269)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_LEGAL_ENTITIES_PK | LEGAL_ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | LEGAL_ENTITY_ID |
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 100 |  | Yes | NAME |
| COUNTRY_CODE | VARCHAR2 | 2 |  |  | COUNTRY_CODE |
| PARENT_DIVISION_NAME | VARCHAR2 | 100 |  |  | PARENT_DIVISION_NAME |
| PARENT_DIVISION_ID | NUMBER |  | 18 |  | Id of the parent division of the legal entity |
| LEGAL_EMPLOYER | VARCHAR2 | 1 |  |  | LEGAL_EMPLOYER |
| PAYROLL_STATUTORY_UNIT | VARCHAR2 | 1 |  |  | PAYROLL_STATUTORY_UNIT |
| PSU_ASSOC_LDG_NAME | VARCHAR2 | 240 |  |  | Payroll Statutory Unit Associated Legislative Data Group |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LEGAL_ENTITY_IDENTIFIER | VARCHAR2 | 30 |  |  | LEGAL_ENTITY_IDENTIFIER |
| LEGAL_ENTITY_REG_NUMBER | VARCHAR2 | 30 |  |  | LEGAL_ENTITY_REG_NUMBER |
| LEGAL_REPORTING_UNIT_NUM | VARCHAR2 | 30 |  |  | LEGAL_REPORTING_UNIT_NUM |
| ULTIMATE_HOLDING_COMPANY | VARCHAR2 | 1 |  |  | ULTIMATE_HOLDING_COMPANY |
| GENERATED | VARCHAR2 | 1 |  |  | GENERATED |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_LEGAL_ENTITIES_F1 | Non Unique | Default | CONFIGURATION_ID |
| HRW_LEGAL_ENTITIES_F2 | Non Unique | Default | LOCATION_ID |
| HRW_LEGAL_ENTITIES_PK | Unique | Default | LEGAL_ENTITY_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
