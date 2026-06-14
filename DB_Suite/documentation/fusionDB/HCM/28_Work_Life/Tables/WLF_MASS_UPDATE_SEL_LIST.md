# WLF_MASS_UPDATE_SEL_LIST

Table to store language-independent information of learning item objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfmassupdatesellist-28120.html#wlfmassupdatesellist-28120](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfmassupdatesellist-28120.html#wlfmassupdatesellist-28120)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_MASS_UPDATE_SEL_LIST_PK | SELECTION_LIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SELECTION_LIST_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| SELECTION_IDENTIFIER_ID | NUMBER |  | 18 |  | SELECTION_IDENTIFIER_ID |
| OBJECT_TYPE | VARCHAR2 | 64 |  |  | OWNER |
| OBJECT_ID | NUMBER |  | 18 |  | OBJECT_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_MASS_UPDATE_SEL_LIST_U1 | Unique | Default | SELECTION_LIST_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
