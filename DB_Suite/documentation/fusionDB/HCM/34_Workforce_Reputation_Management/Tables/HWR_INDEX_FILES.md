# HWR_INDEX_FILES

Table to store and retrieve index files in DB.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrindexfiles-6677.html#hwrindexfiles-6677](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrindexfiles-6677.html#hwrindexfiles-6677)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_INDEX_FILES_PK | INDEX_FILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INDEX_FILE_ID | NUMBER |  |  | Yes | The ID of the index file INDEX_FILE_ID |
| NAME | VARCHAR2 | 80 |  |  | The NAME column stores the name of the index file. |
| INDEX_FILE | BLOB |  |  | Yes | The index file stored as a BLOB data. |
| TYPE | VARCHAR2 | 80 |  |  | TYPE column specifies the type of the file. |
| ENTITY | VARCHAR2 | 80 |  |  | The Entity the file is related to. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_INDEX_FILES_U1 | Unique | FUSION_TS_TX_DATA | INDEX_FILE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
