# WLF_SUPPLIER_RESOURCES

Table to store details of resources

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfsupplierresources-24671.html#wlfsupplierresources-24671](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfsupplierresources-24671.html#wlfsupplierresources-24671)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SUPPLIER_RESOURCES_PK | SUPPLIER_RESOURCES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUPPLIER_RESOURCES_ID | NUMBER |  | 18 | Yes | Supplier Resource PK |
| RESOURCE_ID | NUMBER |  | 18 | Yes | Resource Id |
| SUPPLIER_ID | NUMBER |  | 18 | Yes | Person Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SUPPLIER_RESOURCES_FK1 | Non Unique | Default | RESOURCE_ID |
| WLF_SUPPLIER_RESOURCES_FK2 | Non Unique | Default | SUPPLIER_ID |
| WLF_SUPPLIER_RESOURCES_U1 | Unique | Default | SUPPLIER_RESOURCES_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
