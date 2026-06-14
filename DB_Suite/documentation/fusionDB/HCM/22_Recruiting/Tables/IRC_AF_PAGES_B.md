# IRC_AF_PAGES_B

Stores the Pages for Apply Flow.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpagesb-3490.html#ircafpagesb-3490](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpagesb-3490.html#ircafpagesb-3490)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AF_PAGES_B_PK | PAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAGE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SECTION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_AF_SECTIONS_B table. |
| PAGE_SEQ_NUM | NUMBER |  | 9 | Yes | Store the display sequence number of this Page with in each Section. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AF_PAGES_B_FK1 | Non Unique | Default | SECTION_ID |
| IRC_AF_PAGES_B_PK | Unique | Default | PAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
