# HXT_SERIALIZED_LAYOUTS

This table is to store the serialized object of layout information

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtserializedlayouts-13725.html#hxtserializedlayouts-13725](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtserializedlayouts-13725.html#hxtserializedlayouts-13725)

## Primary Key

| Name | Columns |
|------|----------|
| hxt_serialized_layouts_PK | SERIALIZED_LAYOUT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SERIALIZED_LAYOUT_ID | NUMBER |  | 18 | Yes | SERIALIZED_LAYOUT_ID |
| TCLAYFLD_ATTRIBUTE_CATEGORY | VARCHAR2 | 50 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| TCLAYST_ID | NUMBER |  | 18 | Yes | This column refers to the TimecardLayoutsetId |
| TCLAY_ID | NUMBER |  | 18 | Yes | This column referts to the timecardLayoutID |
| TCLAY_TYPE | VARCHAR2 | 500 |  | Yes | This column refers to the timecard layout type |
| SCHEMA_VERSION | VARCHAR2 | 30 |  | Yes | This column refers to the timecard layout schema version |
| LAYOUT_CACHE | CLOB |  |  | Yes | This column refers to the Layout object |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hxt_serialized_layouts_U1 | Unique | Default | SERIALIZED_LAYOUT_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
