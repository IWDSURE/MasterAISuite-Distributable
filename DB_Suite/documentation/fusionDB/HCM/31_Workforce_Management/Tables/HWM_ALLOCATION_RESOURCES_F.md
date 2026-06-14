# HWM_ALLOCATION_RESOURCES_F

Time Allocations Resource table is effective dated table that associates a resource to Time allocation definition in Time Allocations Header table

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationresourcesf-27857.html#hwmallocationresourcesf-27857](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationresourcesf-27857.html#hwmallocationresourcesf-27857)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ALLOCATION_RESOURCES_F_PK | ALLOCATION_RESOURCES_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ALLOCATION_RESOURCES_ID | NUMBER |  | 18 | Yes | ALLOCATION_RESOURCES_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support | Active |
| RESOURCE_ID | NUMBER |  | 18 | Yes | Primary Key column contaning Resource Id/Person Id.  This column is not updateable. | Active |
| SUBRESOURCE_ID | NUMBER |  | 18 |  | SUBRESOURCE_ID |  |
| ALLOCATION_ID | NUMBER |  | 18 | Yes | Name of  Time Allocation ID |  |
| INACTIVE_FLAG | NUMBER |  | 1 |  | Mark if the allocation assignment is inactive |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_ALLOCATION_RESOURCES_F_PK | Unique | FUSION_TS_TX_DATA | ALLOCATION_RESOURCES_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE | Active |
| HWM_ALLOCATION_RESOURCES_F_U1 | Unique | Default | RESOURCE_ID, SUBRESOURCE_ID, ALLOCATION_ID, EFFECTIVE_START_DATE |  |
| HWM_ALLOCATION_RESOURCES_F_U2 | Unique | Default | RESOURCE_ID, SUBRESOURCE_ID, EFFECTIVE_START_DATE |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
