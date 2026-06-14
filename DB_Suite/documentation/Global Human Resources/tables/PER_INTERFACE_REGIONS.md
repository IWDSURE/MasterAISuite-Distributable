# PER_INTERFACE_REGIONS

Table for storing interface region control records that activate and deactivate parts of a user interface.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinterfaceregions-26100.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinterfaceregions-26100.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INTERFACE_REGIONS_PK | USER_INTERFACE, REGION, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_INTERFACE | VARCHAR2 | 30 |  | Yes | Code for the user interface containing the specified region to control, based on lookup type PER_INTERFACES. |
| REGION | VARCHAR2 | 30 |  | Yes | Code the user interface region to activate or deactivate, based on lookup type PER_INTERFACE_REGIONS. |
| ACTIVE | VARCHAR2 | 1 |  | Yes | Flag to indicate if the region is active or inactive. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_INTERFACE_REGIONS_U1 | Unique | Default | USER_INTERFACE, REGION, ENTERPRISE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
