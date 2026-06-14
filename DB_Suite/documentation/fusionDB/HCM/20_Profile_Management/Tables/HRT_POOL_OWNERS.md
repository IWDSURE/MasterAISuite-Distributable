# HRT_POOL_OWNERS

This is profiles core table contains owners of talent pools.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolowners-23282.html#hrtpoolowners-23282](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolowners-23282.html#hrtpoolowners-23282)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_POOL_OWNERS_PK | ENTERPRISE_ID, POOL_OWNER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_OWNER_ID | NUMBER |  | 18 | Yes | Pool Owner Id - generated system primary key. |
| POOL_ID | NUMBER |  | 18 | Yes | Pool Identifier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OWNER_PERSON_ID | NUMBER |  | 18 | Yes | Person ID of the owner. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| FAVORITE_FLAG | VARCHAR2 | 20 |  |  | Indicates if the pool is a favorite of the user. |
| SOURCE_CODE | VARCHAR2 | 30 |  |  | Source code represents the source from were row is created or updated. |
| SOURCE_KEY | VARCHAR2 | 200 |  |  | Source Key represents the object Id from were row is created or updated. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_POOL_OWNERS_N1 | Non Unique | Default | OWNER_PERSON_ID, ENTERPRISE_ID |
| HRT_POOL_OWNERS_PK | Unique | Default | ENTERPRISE_ID, POOL_OWNER_ID |
| HRT_POOL_OWNERS_U1 | Unique | Default | OWNER_PERSON_ID, POOL_ID, ENTERPRISE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
