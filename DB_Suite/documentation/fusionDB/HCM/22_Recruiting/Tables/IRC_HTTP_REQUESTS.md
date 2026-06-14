# IRC_HTTP_REQUESTS

This table stores http request information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irchttprequests-26903.html#irchttprequests-26903](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irchttprequests-26903.html#irchttprequests-26903)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_HTTP_REQUESTS_PK | HTTP_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HTTP_REQUEST_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CONSUMER_REFERENCE_ID | NUMBER |  | 18 |  | ID of the consumer using the REQUEST |
| URL | VARCHAR2 | 1000 |  | Yes | Full URL of the request. Can include tokens. |
| HTTP_METHOD | VARCHAR2 | 40 |  | Yes | HTTP Method of the request, like GET, POST etc., |
| AUTH_TYPE | VARCHAR2 | 40 |  | Yes | Authentication type used for the http request. |
| BASIC_AUTH_KEY | VARCHAR2 | 1000 |  |  | Key of the Basic Auth used for this http request. |
| BASIC_AUTH_VALUE | CLOB |  |  |  | Value of the Basic Auth used for this http request. |
| BEARER_TOKEN | CLOB |  |  |  | Bearer token used to authenticate this http request. |
| BODY_TYPE | VARCHAR2 | 40 |  | Yes | Type of the body supported for the http request. |
| BODY_SUBTYPE | VARCHAR2 | 40 |  |  | Sub-type of the body of the http request. This applies only when the TYPE is raw. |
| BODY | CLOB |  |  |  | Body or payload of the http request. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_HTTP_REQUESTS_FK1 | Non Unique | Default | CONSUMER_REFERENCE_ID |
| IRC_HTTP_REQUESTS_PK | Unique | Default | HTTP_REQUEST_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
