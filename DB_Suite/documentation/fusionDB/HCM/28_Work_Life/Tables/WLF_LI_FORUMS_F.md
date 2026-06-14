# WLF_LI_FORUMS_F

Table to store forum learning items.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliforumsf-20284.html#wlfliforumsf-20284](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliforumsf-20284.html#wlfliforumsf-20284)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_FORUMS_F_PK | FORUM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORUM_ID | NUMBER |  | 18 | Yes | FORUM_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | LEARNING_ITEM_ID |
| FORUM_TYPE | VARCHAR2 | 30 |  | Yes | FORUM_TYPE |
| PARENT_LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | CATALOG_LEARNING_ITEM_ID |
| STATUS_UPDATED_BY | VARCHAR2 | 30 |  |  | Indicates who updated the status of the forum. Ex: Ess Job,Specialist |
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
| WLF_LI_FORUMS_F_N1 | Non Unique | Default | LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| WLF_LI_FORUMS_F_N2 | Non Unique | Default | PARENT_LEARNING_ITEM_ID, FORUM_TYPE |
| WLF_LI_FORUMS_F_U1 | Unique | Default | FORUM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
