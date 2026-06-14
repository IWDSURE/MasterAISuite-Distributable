# HRC_LOADER_LOGICAL_OBJECTS

Logical and Business Object metadata for the File Based Loader.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderlogicalobjects-21091.html#hrcloaderlogicalobjects-21091](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderlogicalobjects-21091.html#hrcloaderlogicalobjects-21091)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_LOGICAL_OBJECTS_PK | LOGICAL_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LOGICAL_OBJECT_ID | NUMBER |  | 18 | Yes | LOGICAL_OBJECT_ID |  |
| LOGICAL_OBJECT_NAME | VARCHAR2 | 200 |  | Yes | LOGICAL_OBJECT_NAME |  |
| BUSINESS_OBJECT_NAME | VARCHAR2 | 200 |  | Yes | BUSINESS_OBJECT_NAME |  |
| COLUMN_NAME | VARCHAR2 | 30 |  | Yes | COLUMN_NAME |  |
| REF_BUSINESS_OBJECT_NAME | VARCHAR2 | 200 |  | Yes | REF_BUSINESS_OBJECT_NAME |  |
| KEY_TYPE | VARCHAR2 | 30 |  | Yes | KEY_TYPE |  |
| CURRENT_LEVEL | NUMBER |  | 4 | Yes | CURRENT_LEVEL |  |
| LEVEL_NAME | VARCHAR2 | 200 |  | Yes | LEVEL_NAME |  |
| ATTR_EXPRESSION | VARCHAR2 | 4000 |  |  | ATTR_EXPRESSION |  |
| FUSION_COLUMN_NAME | VARCHAR2 | 30 |  | Yes | FUSION_COLUMN_NAME |  |
| FUSION_BASE_TABLE_NAME | VARCHAR2 | 30 |  |  | FUSION_BASE_TABLE_NAME |  |
| DATE_EFFECTIVE | VARCHAR2 | 30 |  |  | DATE_EFFECTIVE |  |
| PROCESSING_ORDER | NUMBER |  | 4 |  | PROCESSING_ORDER |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_LOGICAL_OBJS_PK | Unique | Default | LOGICAL_OBJECT_ID |
| HRC_LOADER_LOGICAL_OBJS_U1 | Unique | Default | LOGICAL_OBJECT_NAME, BUSINESS_OBJECT_NAME, COLUMN_NAME, LOGICAL_OBJECT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
