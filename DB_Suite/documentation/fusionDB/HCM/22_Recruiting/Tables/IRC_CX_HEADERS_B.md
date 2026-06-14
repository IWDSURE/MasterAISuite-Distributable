# IRC_CX_HEADERS_B

Table in which custom headers are stored, headers are defined for the particular theme.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxheadersb-22584.html#irccxheadersb-22584](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxheadersb-22584.html#irccxheadersb-22584)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_HEADERS_B_PK | HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HEADER_ID | NUMBER |  | 18 | Yes | The primary key, system generated value. |
| THEME_ID | NUMBER |  | 18 | Yes | Foreign key to the irc_cx_site_themes table. |
| TYPE | VARCHAR2 | 200 |  | Yes | The type of this header for example ORA_GLOBAL or ORA_ADDITIONAL. |
| NAME | VARCHAR2 | 1000 |  |  | The name of this header that must be set by administrator, can be null for global ones. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_HEADERS_B_N1 | Non Unique | Default | TYPE |
| IRC_CX_HEADERS_B_PK | Unique | Default | HEADER_ID |
| IRC_CX_HEADERS_B_FK1 | Non Unique | Default | THEME_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
