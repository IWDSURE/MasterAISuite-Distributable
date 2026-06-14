# PER_CHK_CONTENT_ITEMS_B

PER_CHK_CONTENT_ITEMS_B : This is base table for checklist content items

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcontentitemsb-4139.html#perchkcontentitemsb-4139](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcontentitemsb-4139.html#perchkcontentitemsb-4139)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_CONTENT_ITEMS_B_PK | CHK_CONTENT_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHK_CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | CHK_CONTENT_ITEM_ID |  |
| CONTENT_ITEM_CODE | VARCHAR2 | 80 |  | Yes | Unique code for seed data purpose |  |
| CHK_CONTENT_DEFN_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CHK_CONTENT_DEFNS_B.CHK_CONTENT_DEFN_ID |  |
| SEQUENCE | NUMBER |  | 9 |  | Item Sequence |  |
| NOTE_CONTENT_DEFN_ID | NUMBER |  | 18 |  | Foreign Key to PER_CHK_CONTENT_DEFNS_B.CHK_CONTENT_DEFN_ID |  |
| CONTENT_URL | VARCHAR2 | 240 |  |  | Content URL |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_CONTENT_ITEMS_B_N1 | Non Unique | FUSION_TS_TX_DATA | CHK_CONTENT_DEFN_ID |
| PER_CHK_CONTENT_ITEMS_B_PK | Unique | FUSION_TS_TX_DATA | CHK_CONTENT_ITEM_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
