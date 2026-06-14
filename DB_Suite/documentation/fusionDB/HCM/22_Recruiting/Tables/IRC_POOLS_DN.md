# IRC_POOLS_DN

Table to store denormalized data related to pool.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpoolsdn-4252.html#ircpoolsdn-4252](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpoolsdn-4252.html#ircpoolsdn-4252)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_POOLS_DN_PK | POOL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_ID | NUMBER |  | 18 | Yes | Primary key for this table. Foreign key to HRT_POOLS_B table. |
| TOTAL_CAND_COUNT | NUMBER |  |  | Yes | Stores the total pool member count. |
| TOTAL_NEW_CAND_COUNT | NUMBER |  |  | Yes | Stores the total NEW pool member count. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_POOLS_DN_PK | Unique | Default | POOL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
