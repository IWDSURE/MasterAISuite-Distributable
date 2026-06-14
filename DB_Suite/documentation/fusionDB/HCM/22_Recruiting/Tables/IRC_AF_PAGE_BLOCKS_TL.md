# IRC_AF_PAGE_BLOCKS_TL

This table stores all the translation data for the Pag Block.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpageblockstl-5702.html#ircafpageblockstl-5702](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpageblockstl-5702.html#ircafpageblockstl-5702)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AF_PAGE_BLOCKS_TL_PK | PAGE_BLOCK_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAGE_BLOCK_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. Foreign key to IRC_AF_PAGE_BLOCKS_B table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| PAGE_BLOCK_TITLE | VARCHAR2 | 240 |  | Yes | Stores the transalatable title of this Page Block. |
| PAGE_BLOCK_INSTRUCTIONS | VARCHAR2 | 1000 |  |  | Stores the transalatable Instruction text for the page block. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AF_PAGE_BLOCKS_TL_PK | Unique | Default | PAGE_BLOCK_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
