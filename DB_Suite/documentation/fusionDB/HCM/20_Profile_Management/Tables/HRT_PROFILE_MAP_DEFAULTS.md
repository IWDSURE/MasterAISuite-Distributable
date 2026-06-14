# HRT_PROFILE_MAP_DEFAULTS

Profile Upgrade Mapping Defaults table stores the metadata data to assist column level mapping.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemapdefaults-11783.html#hrtprofilemapdefaults-11783](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemapdefaults-11783.html#hrtprofilemapdefaults-11783)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_MAP_DEFAULT_PK | MAPPING_DEFAULT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_DEFAULT_ID | NUMBER |  | 18 | Yes | MAPPING_DEFAULT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | CONTENT_TYPE_ID |
| COLUMN_NAME | VARCHAR2 | 240 |  |  | COLUMN_NAME |
| COLUMN_NAME_TO | VARCHAR2 | 240 |  | Yes | COLUMN_NAME_TO |
| FIELD_NAME | VARCHAR2 | 240 |  |  | ALIAS_NAME |
| FIELD_NAME_LABEL | VARCHAR2 | 500 |  |  | COLUMN_NAME_LABEL |
| PROFILE_TYPE_FLAG | VARCHAR2 | 30 |  |  | PROFILE_TYPE_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_MAP_DEFAULT_U1 | Unique | Default | MAPPING_DEFAULT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_PROFILE_MAP_DEFAULT_U11 | Unique | Default | MAPPING_DEFAULT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
