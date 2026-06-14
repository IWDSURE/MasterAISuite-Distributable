# IRC_EXT_API_CONN_POOL

Table used to store connections per module for external API connection pool.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircextapiconnpool-22109.html#ircextapiconnpool-22109](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircextapiconnpool-22109.html#ircextapiconnpool-22109)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EXT_API_CONN_POOL_PK | CONNECTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONNECTION_ID | NUMBER |  | 18 | Yes | System generated primary key for this entity |
| EXT_API_NAME | VARCHAR2 | 20 |  | Yes | Attribute to store external API name |
| STATUS_CODE | VARCHAR2 | 20 |  | Yes | Attribute to store connection status |
| EXPIRATION_DATE | TIMESTAMP |  |  | Yes | Attribute to store connection expiration date |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EXT_API_CONN_POOL_PK | Unique | Default | CONNECTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
