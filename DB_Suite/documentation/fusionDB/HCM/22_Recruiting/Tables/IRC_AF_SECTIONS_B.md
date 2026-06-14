# IRC_AF_SECTIONS_B

Stores the Sections for Apply Flow.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafsectionsb-4525.html#ircafsectionsb-4525](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafsectionsb-4525.html#ircafsectionsb-4525)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AF_SECTIONS_B_PK | SECTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SECTION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| AF_VERSION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_AF_VERSIONS table. |
| SECTION_SEQ_NUM | NUMBER |  | 9 | Yes | Store the display Sequence number of this Section with in each apply flow  version. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AF_SECTIONS_B_FK1 | Non Unique | Default | AF_VERSION_ID |
| IRC_AF_SECTIONS_B_PK | Unique | Default | SECTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
