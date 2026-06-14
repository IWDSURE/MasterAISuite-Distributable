# IRC_EXT_API_CONN_POOL_COUNT

Table used to store the number of connections per module currently taken from external API connection pool.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircextapiconnpoolcount-16629.html#ircextapiconnpoolcount-16629](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircextapiconnpoolcount-16629.html#ircextapiconnpoolcount-16629)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EXT_API_CONN_POOL_COUNT_PK | CONN_COUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONN_COUNT_ID | NUMBER |  | 18 | Yes | System generated primary key for this entity |
| CONNECTIONS_COUNT | NUMBER |  | 18 | Yes | Attribute to store current number of connections per expernal API currently used in connection pool |
| EXT_API_NAME | VARCHAR2 | 20 |  | Yes | Attribute to store external API name |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EXT_API_CONN_POOL_COUNT_PK | Unique | Default | CONN_COUNT_ID |
| IRC_EXT_API_CONN_POOL_COUNT_U1 | Unique | Default | EXT_API_NAME, CONNECTIONS_COUNT |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
