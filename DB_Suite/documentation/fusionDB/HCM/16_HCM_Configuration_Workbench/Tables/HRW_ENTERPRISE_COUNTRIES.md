# HRW_ENTERPRISE_COUNTRIES

The list of countries that an enterprise operates in.

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwenterprisecountries-20351.html#hrwenterprisecountries-20351](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwenterprisecountries-20351.html#hrwenterprisecountries-20351)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_ENTERPRISE_COUNTRIES_PK | CONFIGURATION_ID, COUNTRY_CODE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| COUNTRY_CODE | VARCHAR2 | 2 |  | Yes | COUNTRY_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENTERPRISE_REGISTERED | VARCHAR2 | 1 |  | Yes | ENTERPRISE_REGISTERED |
| DIVISION_REGISTERED | VARCHAR2 | 1 |  | Yes | DIVISION_REGISTERED |
| LDG_NAME | VARCHAR2 | 240 |  |  | Legislative Data Group Name |
| DEFAULT_CURRENCY | VARCHAR2 | 15 |  |  | Legislative Data Group default currency |
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
| HRW_ENTERPRISE_COUNTRY_PK | Unique | Default | CONFIGURATION_ID, COUNTRY_CODE |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
