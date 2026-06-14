# HRT_POOL_SUBSCRIBERS

This is profiles core table contains subscribers of talent pool.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolsubscribers-22701.html#hrtpoolsubscribers-22701](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolsubscribers-22701.html#hrtpoolsubscribers-22701)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_POOL_SUBSCRIBERS_PK | ENTERPRISE_ID, POOL_SUBSCRIBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_SUBSCRIBER_ID | NUMBER |  | 18 | Yes | POOL_SUBSCRIBER_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| POOL_ID | NUMBER |  | 18 | Yes | Pool Identifier |
| SOURCE_ID | NUMBER |  | 18 | Yes | Source Code |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_POOL_SUBSCRIBERS_N2 | Non Unique | Default | SOURCE_ID, ENTERPRISE_ID |
| HRT_POOL_SUBSCRIBERS_PK | Unique | Default | ENTERPRISE_ID, POOL_SUBSCRIBER_ID |
| HRT_POOL_SUBSCRIBERS_U1 | Unique | Default | POOL_ID, ENTERPRISE_ID, SOURCE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
