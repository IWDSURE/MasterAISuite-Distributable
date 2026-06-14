# CMP_TCS_ITEM_TAG

Table holds Comp Tcs Item tag records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsitemtag-3473.html#cmptcsitemtag-3473](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsitemtag-3473.html#cmptcsitemtag-3473)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_ITEM_TAG_PK | ITEM_TAG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ITEM_TAG_ID | NUMBER |  | 18 | Yes | ITEM_TAG_ID |
| ITEM_ID | NUMBER |  | 18 |  | ITEM_ID |
| STMT_ID | NUMBER |  | 18 |  | STMT_ID |
| CAT_ID | NUMBER |  | 18 |  | CAT_ID |
| STMT_PERD_ID | NUMBER |  | 18 |  | STMT_PERD_ID |
| TAG_PLACE | VARCHAR2 | 30 |  | Yes | TAG_PLACE |
| ITEM_TAG_NAME | VARCHAR2 | 80 |  |  | ITEM_TAG_NAME |
| CONTRIBUTIONS_TYPE | VARCHAR2 | 30 |  |  | CONTRIBUTIONS_TYPE |
| ITEM_VALUE | VARCHAR2 | 30 |  |  | ITEM_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ITEM_TAG_DEF_ID | NUMBER |  | 18 |  | ITEM_TAG_DEF_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_ITEM_TAG_U1 | Unique | Default | ITEM_TAG_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
