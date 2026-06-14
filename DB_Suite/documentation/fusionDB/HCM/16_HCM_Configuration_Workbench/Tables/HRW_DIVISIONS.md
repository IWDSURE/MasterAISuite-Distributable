# HRW_DIVISIONS

An Enterprise Configuration Division contains the information for a division defined within an Enterprise Configuration. A division refers to a business orientated sub-division within an enterprise, in which each division organizes itself differently to deliver products and services or address different markets. A division is incorporated in one or more countries.

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwdivisions-30062.html#hrwdivisions-30062](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwdivisions-30062.html#hrwdivisions-30062)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_DIVISIONS_PK | DIVISION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIVISION_ID | NUMBER |  | 18 | Yes | DIVISION_ID |
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 100 |  |  | NAME |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_DIVISIONS_F1 | Non Unique | Default | CONFIGURATION_ID |
| HRW_DIVISIONS_F2 | Non Unique | Default | LOCATION_ID |
| HRW_DIVISIONS_PK | Unique | Default | DIVISION_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
