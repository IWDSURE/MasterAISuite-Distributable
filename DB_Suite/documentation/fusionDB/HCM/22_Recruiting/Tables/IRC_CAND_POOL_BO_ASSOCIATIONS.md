# IRC_CAND_POOL_BO_ASSOCIATIONS

Table to store the candidate pool associated business object items

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolboassociations-10659.html#irccandpoolboassociations-10659](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolboassociations-10659.html#irccandpoolboassociations-10659)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_POOL_BO_ASSOC_PK | POOL_BO_ASSOCIATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_BO_ASSOCIATION_ID | NUMBER |  | 18 | Yes | Primary key for this table, System generated. |
| POOL_ALERT_CONFIG_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAND_POOL_ALERT_CONFIG |
| OBJECT_TYPE | VARCHAR2 | 32 |  | Yes | Stores the business object type. It can be LEARN, JOURNEY etc. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of business objects i.e. Learning Item Id, Journey Id. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_POOL_BO_ASSOC_PK | Unique | Default | POOL_BO_ASSOCIATION_ID |
| IRC_CAND_POOL_BO_ASSOC_U1 | Unique | Default | POOL_ALERT_CONFIG_ID, OBJECT_TYPE, OBJECT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
