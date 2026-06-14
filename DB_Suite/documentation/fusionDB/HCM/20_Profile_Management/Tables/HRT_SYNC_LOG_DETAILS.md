# HRT_SYNC_LOG_DETAILS

This table stores the details for sync logs

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtsynclogdetails-13435.html#hrtsynclogdetails-13435](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtsynclogdetails-13435.html#hrtsynclogdetails-13435)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SYNC_LOG_DETAILS_PK | SYNC_LOG_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SYNC_LOG_DETAIL_ID | NUMBER |  | 18 | Yes | SYNC_LOG_DETAIL_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| SOURCE_PROFILE_ID | NUMBER |  | 18 |  | SOURCE_PROFILE_ID |
| TARGET_PROFILE_ID | NUMBER |  | 18 |  | TARGET_PROFILE_ID |
| ITEMS_SYNC_COUNT | NUMBER |  | 18 |  | ITEMS_SYNC_COUNT |
| ITEMS_CURATED_COUNT | NUMBER |  | 18 |  | ITEMS_CURATED_COUNT |
| ITEMS_UNLINK_COUNT | NUMBER |  | 18 |  | ITEMS_UNLINK_COUNT |
| ITEMS_SKIPPED_COUNT | NUMBER |  | 18 |  | ITEMS_SKIPPED_COUNT |
| PROFILE_ITEM_SYNC_DETAIL | CLOB |  |  |  | PROFILE_ITEM_SYNC_DETAIL |
| PROFILE_SYNC_LOG_ID | NUMBER |  |  |  | PROFILE_SYNC_LOG_ID |
| MESSAGE_TYPE | VARCHAR2 | 20 |  |  | MESSAGE_TYPE |
| MESSAGE_TEXT | VARCHAR2 | 500 |  |  | MESSAGE_TEXT |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SYNC_LOG_DETAILS_PK | Unique | HRT_SYNC_LOG_DETAILS_PK | SYNC_LOG_DETAIL_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
