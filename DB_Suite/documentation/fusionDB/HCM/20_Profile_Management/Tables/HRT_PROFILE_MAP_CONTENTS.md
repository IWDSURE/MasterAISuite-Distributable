# HRT_PROFILE_MAP_CONTENTS

Profile Upgrade Mapping Contents table stores the profile section level mapping data.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemapcontents-16812.html#hrtprofilemapcontents-16812](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemapcontents-16812.html#hrtprofilemapcontents-16812)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_UPG_MAP_CONTE_PK | MAPPING_CONTENT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_CONTENT_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PROFILE_TYPE_ID | NUMBER |  | 18 | Yes | PROFILE_TYPE_ID |
| SECTION_ID | NUMBER |  | 18 | Yes | SECTION_ID |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | CONTENT_TYPE_ID |
| PROFILE_TYPE_ID_TO | NUMBER |  | 18 |  | PROFILE_TYPE_ID_TO |
| CONTENT_TYPE_ID_TO | NUMBER |  | 18 |  | CONTENT_TYPE_ID_TO |
| SECTION_ID_TO | NUMBER |  | 18 |  | SECTION_ID_TO |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| SECTION_MIGRATE | VARCHAR2 | 30 |  |  | SECTION_MIGRATE |
| ITEM_VIEW_NAME | VARCHAR2 | 50 |  |  | ITEM_VIEW_NAME |
| CONTENT_VALUE_SET_ID | NUMBER |  | 18 |  | CONTENT_VALUE_SET_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_MAP_CONTENTS_U1 | Unique | Default | MAPPING_CONTENT_ID, BUSINESS_GROUP_ID |
| HRT_PROFILE_MAP_CONTENTS_U2 | Unique | Default | BUSINESS_GROUP_ID, CONTENT_TYPE_ID, SECTION_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
