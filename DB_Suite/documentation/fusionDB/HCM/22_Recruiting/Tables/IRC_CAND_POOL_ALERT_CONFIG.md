# IRC_CAND_POOL_ALERT_CONFIG

Table to store the candidate pool associated alert configuration

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolalertconfig-20456.html#irccandpoolalertconfig-20456](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolalertconfig-20456.html#irccandpoolalertconfig-20456)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_POOL_ALERT_CONFIG_PK | POOL_ALERT_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_ALERT_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table, system generated. |
| POOL_ID | NUMBER |  | 18 | Yes | Foreign key to hrt_pools_b |
| ACTIVE_FLAG | VARCHAR2 | 1 |  | Yes | Column to indicate if job notifications are enabled for candidate pools. |
| END_DATE | DATE |  |  |  | Stores end date for the candidate pool job notifications |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_POOL_ALERT_CONFIG_FK1 | Non Unique | Default | POOL_ID |
| IRC_CAND_POOL_ALERT_CONFIG_PK | Unique | Default | POOL_ALERT_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
