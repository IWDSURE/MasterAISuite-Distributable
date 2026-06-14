# BEN_ONLINE_WARNINGS

BEN_ONLINE_WARNINGS temporarily stores warning messages written from API's.  The enrollment forms look in that table to see if any messages were written.  If so, it displays the warnings and then deletes the rows from the table.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benonlinewarnings-19787.html#benonlinewarnings-19787](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benonlinewarnings-19787.html#benonlinewarnings-19787)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ONLINE_WARNINGS_PK | SESSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SESSION_ID | NUMBER |  |  | Yes | Database Session Identifier. |
| MESSAGE_TEXT | VARCHAR2 | 2000 |  | Yes | Message text. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ONLINE_WARNINGS_PK | Unique | Default | SESSION_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
