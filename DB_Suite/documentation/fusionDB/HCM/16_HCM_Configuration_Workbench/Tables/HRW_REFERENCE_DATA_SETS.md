# HRW_REFERENCE_DATA_SETS

This table stores data on reference data sets for configuration by the enterprise structure configurator

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwreferencedatasets-21375.html#hrwreferencedatasets-21375](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwreferencedatasets-21375.html#hrwreferencedatasets-21375)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_REFERENCE_DATE_SETS_PK | REFERENCE_DATA_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REFERENCE_DATA_SET_ID | NUMBER |  | 18 | Yes | REFERENCE_DATA_SET_ID |
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CODE | VARCHAR2 | 30 |  | Yes | CODE |
| NAME | VARCHAR2 | 100 |  |  | NAME |
| DIMENSION | VARCHAR2 | 100 |  |  | Dimension |
| DIMENSION_TYPE | VARCHAR2 | 20 |  |  | Dimension Type |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
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
| HRW_REFERENCE_DATA_SETS_F1 | Non Unique | Default | CONFIGURATION_ID |
| HRW_REFERENCE_DATA_SETS_F2 | Non Unique | Default | BUSINESS_UNIT_ID |
| HRW_REFERENCE_DATA_SETS_PK | Unique | Default | REFERENCE_DATA_SET_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
