# CMP_PERSON_REGION_ITEMS

Stores worksheet layout changes done by managers.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppersonregionitems-14428.html#cmppersonregionitems-14428](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppersonregionitems-14428.html#cmppersonregionitems-14428)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PERSON_REGION_ITEMS_PK | CUSTOM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CUSTOM_ID | NUMBER |  | 18 | Yes | CUSTOM_ID |
| CUSTOM_TYPE | VARCHAR2 | 30 |  | Yes | CUSTOM_TYPE |
| CUSTOM_KEY | NUMBER |  | 18 | Yes | CUSTOM_KEY |
| REGION_NAME | VARCHAR2 | 60 |  | Yes | REGION_NAME |
| ITEM_NAME | VARCHAR2 | 60 |  | Yes | ITEM_NAME |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| VISIBLE_FLAG | VARCHAR2 | 1 |  |  | VISIBLE_FLAG |
| UPDATE_ALLOWED_FLAG | VARCHAR2 | 1 |  |  | UPDATE_ALLOWED_FLAG |
| COLUMN_WIDTH | NUMBER |  |  |  | COLUMN_WIDTH |
| WRAP_FLAG | VARCHAR2 | 1 |  |  | WRAP_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PERSON_REGION_ITEMS_N1 | Non Unique | Default | PERSON_ID, CUSTOM_KEY, CUSTOM_TYPE, REGION_NAME |
| CMP_PERSON_REGION_ITEMS_PK | Unique | Default | CUSTOM_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
