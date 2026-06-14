# HRT_BOOKMARKS_B

This table is used to store bookmarks created by an employee

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtbookmarksb-26235.html#hrtbookmarksb-26235](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtbookmarksb-26235.html#hrtbookmarksb-26235)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_BOOKMARKS_B_PK | BOOKMARK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BOOKMARK_ID | NUMBER |  | 18 | Yes | Profile Bookmark Id |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PROFILE_ID | NUMBER |  | 18 | Yes | Profile Id |
| URL | VARCHAR2 | 4000 |  | Yes | Bookmark Url |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_BOOKMARKS_B_PK | Unique | Default | BOOKMARK_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
