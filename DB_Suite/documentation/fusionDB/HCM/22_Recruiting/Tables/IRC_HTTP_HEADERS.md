# IRC_HTTP_HEADERS

This tables stores http headers for a http request.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irchttpheaders-30328.html#irchttpheaders-30328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irchttpheaders-30328.html#irchttpheaders-30328)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_HTTP_HEADERS_PK | HTTP_HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HTTP_HEADER_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| NAME | VARCHAR2 | 1000 |  | Yes | Name of the http request header param. |
| VALUE | CLOB |  |  | Yes | Value of the http request header param. |
| HTTP_REQUEST_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_HTTP_REQUESTS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_HTTP_HEADERS_FK1 | Non Unique | Default | HTTP_REQUEST_ID |
| IRC_HTTP_HEADERS_PK | Unique | Default | HTTP_HEADER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
