# IRC_AF_PAGE_BLOCKS_B

Stores the Page Blocks for Apply Flow.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpageblocksb-20635.html#ircafpageblocksb-20635](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpageblocksb-20635.html#ircafpageblocksb-20635)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AF_PAGE_BLOCKS_B_PK | PAGE_BLOCK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAGE_BLOCK_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| PAGE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_AF_PAGES_B table. |
| PAGE_BLOCK_SEQ_NUM | NUMBER |  | 9 | Yes | Stores the display sequence number of this Block with in each Page. |
| BLOCK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_AF_BLOCKS_B table. |
| HIDE_IN_MOBILE_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates if the block must be hidden in Mobile apply flow. |
| PAGE_BLOCK_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates if the page block is required in apply flow. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AF_PAGE_BLOCKS_B_FK1 | Non Unique | Default | PAGE_ID |
| IRC_AF_PAGE_BLOCKS_B_FK2 | Non Unique | Default | BLOCK_ID |
| IRC_AF_PAGE_BLOCKS_B_PK | Unique | Default | PAGE_BLOCK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
