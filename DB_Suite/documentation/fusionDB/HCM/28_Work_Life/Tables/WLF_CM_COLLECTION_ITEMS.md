# WLF_CM_COLLECTION_ITEMS

Table to store collection items.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmcollectionitems-6385.html#wlfcmcollectionitems-6385](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmcollectionitems-6385.html#wlfcmcollectionitems-6385)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CM_COLLECTION_ITEMS_PK | ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ITEM_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| ITEM_TYPE | VARCHAR2 | 32 |  | Yes | Polymorphic discriminator column {COLLECTION, TUTORIAL ... }. |
| PARENT_CONTENT_ID | NUMBER |  | 18 | Yes | Reference to parent/collection entity. |
| CHILD_CONTENT_ID | NUMBER |  | 18 | Yes | Reference to child content entity. |
| POSITION | NUMBER |  | 38 |  | Position of the item in collection identified by PARENT_CONENT_ID. |
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
| WLF_CM_COLLECTION_ITEMS_N1 | Non Unique | Default | ITEM_TYPE |
| WLF_CM_COLLECTION_ITEMS_U1 | Unique | Default | ITEM_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
