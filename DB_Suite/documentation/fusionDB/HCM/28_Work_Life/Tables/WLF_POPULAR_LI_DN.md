# WLF_POPULAR_LI_DN

This table stores the details of learning assignment completions in weekly increments in a given popularity category.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpopularlidn-31474.html#wlfpopularlidn-31474](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpopularlidn-31474.html#wlfpopularlidn-31474)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_POPULAR_LI_DN_PK | POPULAR_LI_DN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPULAR_LI_DN_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| CATEGORY_ID | NUMBER |  | 18 | Yes | Spcifies the identifier of the popularity category |
| CATEGORY_CODE | VARCHAR2 | 30 |  | Yes | Specifies the popularity category of the learning item |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Specifies identifier of the learning item |
| LEARNING_ITEM_TYPE | VARCHAR2 | 32 |  |  | Specifies the learning item type (e.g., Course, Specialization, Community, etc.,) |
| LEARNING_ITEM_SUB_TYPE | VARCHAR2 | 30 |  |  | Specifies the learning item sub type for the learning item type like Community (e.g., Topic Community, Category Community, etc.,) |
| LEARNING_ITEM_NAME | VARCHAR2 | 250 |  |  | Specifies name of the learning item in US language |
| METRIC_DATE | DATE |  |  | Yes | Specifies the effective date of the calculated metrics |
| COMPLETION_COUNT | NUMBER |  |  |  | Specifies the total number of assignment completions during past one week |
| MEMBERSHIP_COUNT | NUMBER |  |  |  | Specifies the total number of memberships in the given learning community |
| LATEST_COMM_ITEM_ADDED_DATE | DATE |  |  |  | Specifies the date when the latest catalog item is added to the community |
| LATEST_COMM_ITEM_FEATURED_DATE | DATE |  |  |  | Specifies the date when the latest catalog item is marked as featured in the community |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_POPULAR_LI_DN_U1 | Unique | Default | POPULAR_LI_DN_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
