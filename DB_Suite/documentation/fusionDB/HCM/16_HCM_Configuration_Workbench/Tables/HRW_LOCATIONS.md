# HRW_LOCATIONS

Table to store location definitions

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwlocations-26588.html#hrwlocations-26588](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwlocations-26588.html#hrwlocations-26588)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_LOCATIONS_PK | LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_ID | NUMBER |  | 18 | Yes | LOCATION_ID |
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| TCA_LOCATION_ID | NUMBER |  | 18 |  | TCA Location ID |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| REFERENCE_DATA_SET_ID | NUMBER |  | 18 |  | REFERENCE_DATA_SET_ID |
| LOCATION_CODE | VARCHAR2 | 100 |  | Yes | LOCATION_CODE |
| STYLE | VARCHAR2 | 100 |  |  | STYLE |
| ADDRESS_LINE1 | VARCHAR2 | 100 |  |  | ADDRESS_LINE1 |
| ADDRESS_LINE2 | VARCHAR2 | 100 |  |  | ADDRESS_LINE2 |
| ADDRESS_LINE3 | VARCHAR2 | 100 |  |  | ADDRESS_LINE3 |
| ADDRESS_LINE4 | VARCHAR2 | 100 |  |  | ADDRESS_LINE4 |
| BUILDING | VARCHAR2 | 100 |  |  | BUILDING |
| FLOOR_NUMBER | VARCHAR2 | 100 |  |  | FLOOR_NUMBER |
| TOWN_OR_CITY | VARCHAR2 | 100 |  |  | TOWN_OR_CITY |
| REGION1 | VARCHAR2 | 100 |  |  | REGION1 |
| REGION2 | VARCHAR2 | 100 |  |  | REGION2 |
| REGION3 | VARCHAR2 | 100 |  |  | REGION3 |
| POSTAL_CODE | VARCHAR2 | 100 |  |  | POSTAL_CODE |
| COUNTRY_CODE | VARCHAR2 | 2 |  | Yes | COUNTRY_CODE |
| ADDL_ADDRESS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | ADDL_ADDRESS_ATTRIBUTE1 |
| ADDL_ADDRESS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | ADDL_ADDRESS_ATTRIBUTE2 |
| ADDL_ADDRESS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | ADDL_ADDRESS_ATTRIBUTE3 |
| ADDL_ADDRESS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | ADDL_ADDRESS_ATTRIBUTE4 |
| ADDL_ADDRESS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | ADDL_ADDRESS_ATTRIBUTE5 |
| TIMEZONE_CODE | VARCHAR2 | 50 |  |  | TIMEZONE_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_LOCATIONS_F1 | Non Unique | Default | CONFIGURATION_ID |
| HRW_LOCATIONS_PK | Unique | Default | LOCATION_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
