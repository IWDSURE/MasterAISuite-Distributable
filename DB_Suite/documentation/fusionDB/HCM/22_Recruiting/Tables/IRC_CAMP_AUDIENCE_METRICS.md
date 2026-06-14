# IRC_CAMP_AUDIENCE_METRICS

Table to store the campaign audience metrics

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudiencemetrics-29904.html#irccampaudiencemetrics-29904](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampaudiencemetrics-29904.html#irccampaudiencemetrics-29904)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_AUDIENCE_METRICS_PK | METRIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| METRIC_ID | NUMBER |  | 18 | Yes | Primary key for this table. Sysytem generated. |
| AUDIENCE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_AUDIENCE_SOURCE table |
| METRIC_TYPE | VARCHAR2 | 30 |  | Yes | Stores the type of the metric. It can be ORA_LOC_METRICS or ORA_BU_METRICS |
| COUNT | NUMBER |  |  | Yes | Stores the count of candidates for the given metric |
| ENTITY_ID | NUMBER |  | 18 | Yes | Stores the primary key of the metric entity |
| ENTITY_NAME | VARCHAR2 | 2000 |  | Yes | Stores the metric entity name |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_AUDIENCE_METRICS_FK1 | Non Unique | Default | AUDIENCE_ID |
| IRC_CAMP_AUDIENCE_METRICS_PK | Unique | Default | METRIC_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
