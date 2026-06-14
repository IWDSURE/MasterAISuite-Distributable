# HRT_EXTERNAL_FIELD_MAPPING

This table stores external attributes mapping between HRT_EXTERNAL_FIELDS_B and HRT_PROFILE_ITEMS tables. When external application invokes API call with actual values with these external attributes, the API will use this mapping 
table to write back the values.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtexternalfieldmapping-22758.html#hrtexternalfieldmapping-22758](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtexternalfieldmapping-22758.html#hrtexternalfieldmapping-22758)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_EXTERNAL_FIELD_MAPPIN_PK | EXTERNAL_FIELD_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTERNAL_FIELD_MAPPING_ID | NUMBER |  | 18 | Yes | System generated primary key |
| EXTERNAL_FIELD_ID | NUMBER |  | 18 |  | Foreign key to HRT_EXTERNAL_FIELDS_B table |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_ITEM_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_PROFILE_ITEMS table |
| COLUMN_NAME | VARCHAR2 | 30 |  | Yes | Column name of HRT_PROFILE_ITEMS table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_EXTERNAL_FIELD_MAPPIN_PK | Unique | Default | EXTERNAL_FIELD_MAPPING_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
