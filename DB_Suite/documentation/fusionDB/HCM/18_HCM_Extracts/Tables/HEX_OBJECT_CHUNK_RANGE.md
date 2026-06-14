# HEX_OBJECT_CHUNK_RANGE

The table stores the pre process ranges for the threading object ids.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexobjectchunkrange-22556.html#hexobjectchunkrange-22556](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexobjectchunkrange-22556.html#hexobjectchunkrange-22556)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_OBJECT_CHUNK_RANGE_PK | PREPROCESS_RANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREPROCESS_RANGE_ID | NUMBER |  | 18 | Yes | The column indicates a unique sequence generated value. |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | The column indicates the object type. Valid values are Person_Id, Assignment_Id, Rel_Action_Id. |
| MIN_RANGE | NUMBER |  | 18 |  | The column indicates the minimum value of the object type specified.(Information only column). |
| MAX_RANGE | NUMBER |  | 18 |  | The column indicates the maximum value of the object type specified.(Information only column) |
| LAST_STATS | TIMESTAMP |  |  |  | The column indicates the last stats computation date for the table values. |
| START_VALUE | NUMBER |  | 18 |  | The column indicates the start value within the range. |
| END_VALUE | NUMBER |  | 18 |  | The column indicates the end value within the range. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_OBJECT_CHUNK_RANGE_PK | Unique | Default | PREPROCESS_RANGE_ID |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
