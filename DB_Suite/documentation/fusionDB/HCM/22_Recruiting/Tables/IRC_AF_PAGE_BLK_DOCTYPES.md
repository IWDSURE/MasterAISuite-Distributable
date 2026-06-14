# IRC_AF_PAGE_BLK_DOCTYPES

Table to store the custom block properties for Document Types Block.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpageblkdoctypes-9387.html#ircafpageblkdoctypes-9387](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpageblkdoctypes-9387.html#ircafpageblkdoctypes-9387)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AF_PAGE_BLK_DOCTYPES_PK | PAGE_BLOCK_DOCTYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAGE_BLOCK_DOCTYPE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PAGE_BLOCK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_AF_PAGE_BLOCKS_B table. |
| CATEGORY_CODE | VARCHAR2 | 30 |  | Yes | Stores category code of the of the document. |
| REQUIRED_FLAG | VARCHAR2 | 1 |  | Yes | Stores the flag value if Document Type block is required to be submitted by the candidate or not |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AF_PAGE_BLK_DOCTYPES_FK1 | Non Unique | Default | PAGE_BLOCK_ID |
| IRC_AF_PAGE_BLK_DOCTYPES_PK | Unique | Default | PAGE_BLOCK_DOCTYPE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
