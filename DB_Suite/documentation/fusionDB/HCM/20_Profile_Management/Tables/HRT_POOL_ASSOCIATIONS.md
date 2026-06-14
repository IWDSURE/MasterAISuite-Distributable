# HRT_POOL_ASSOCIATIONS

This is profiles core table contains talent pools associations.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolassociations-20633.html#hrtpoolassociations-20633](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolassociations-20633.html#hrtpoolassociations-20633)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_POOL_ASSOCIATIONS_PK | ENTERPRISE_ID, POOL_ASSOCIATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_ASSOCIATION_ID | NUMBER |  | 18 | Yes | POOL_ASSOCIATION_ID |
| POOL_ID | NUMBER |  | 18 | Yes | Pool Identifier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Pool Object Type |
| OBJECT_ID | NUMBER |  | 18 | Yes | Object Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_POOL_ASSOCIATIONS_N2 | Non Unique | Default | POOL_ID, ENTERPRISE_ID |
| HRT_POOL_ASSOCIATIONS_PK | Unique | Default | ENTERPRISE_ID, POOL_ASSOCIATION_ID |
| HRT_POOL_ASSOCIATIONS_U1 | Unique | FUSION_TS_TX_DATA | OBJECT_ID, ENTERPRISE_ID, OBJECT_TYPE, POOL_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
