# HRT_PROFILE_MAP_COLUMNS

Profile Upgrade Mapping Columns table stores the column level mapping data.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemapcolumns-24474.html#hrtprofilemapcolumns-24474](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemapcolumns-24474.html#hrtprofilemapcolumns-24474)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_MAP_COLUMNS_PK | MAPPING_COLUMN_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_COLUMN_ID | NUMBER |  | 18 | Yes | MAPPING_COLUMN_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| SECTION_ID | NUMBER |  | 18 | Yes | SECTION_ID |
| COLUMN_NAME | VARCHAR2 | 240 |  | Yes | COLUMN_NAME |
| COLUMN_NAME_TO | VARCHAR2 | 240 |  |  | COLUMN_NAME_TO |
| ATTRIBUTE_LABEL | VARCHAR2 | 240 |  |  | ATTRIBUTE_LABEL |
| AUTO_MATCH | VARCHAR2 | 20 |  |  | AUTO_MATCH |
| DISPLAY_FLAG | VARCHAR2 | 20 |  |  | DISPLAY_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_MAP_COLUMNS_U1 | Unique | Default | MAPPING_COLUMN_ID, BUSINESS_GROUP_ID |
| HRT_PROFILE_MAP_COLUMNS_U2 | Unique | Default | BUSINESS_GROUP_ID, SECTION_ID, COLUMN_NAME |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
