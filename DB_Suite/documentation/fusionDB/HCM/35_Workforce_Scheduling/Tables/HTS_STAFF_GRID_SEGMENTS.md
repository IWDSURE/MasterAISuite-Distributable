# HTS_STAFF_GRID_SEGMENTS

Table holding the Schedule Staffing grid detail segments information for the grid context

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffgridsegments-4160.html#htsstaffgridsegments-4160](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffgridsegments-4160.html#htsstaffgridsegments-4160)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFF_GRID_SEGMENTS_PK | GRID_SEGMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRID_SEGMENT_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Staffing Plan |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| DESCRIPTIVE_FLEXFIELD_CODE | VARCHAR2 | 40 |  | Yes | Flex Filed Code |
| STAFF_CONTEXT_CODE | VARCHAR2 | 80 |  | Yes | Context Code |
| SEGMENT_CODE | VARCHAR2 | 30 |  | Yes | Segment Code |
| SEQUENCE_NUMBER | NUMBER |  | 3 | Yes | Segment Sequence Number |
| MIN_VOLUME | NUMBER |  | 9 | Yes | Minimum Volume |
| MAX_VOLUME | NUMBER |  | 9 | Yes | Maximum Volume |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_STAFF_GRID_SEGMENTS_PK | Unique | Default | GRID_SEGMENT_ID |
| HTS_STAFF_GRID_SEGMENTS_U1 | Unique | Default | DESCRIPTIVE_FLEXFIELD_CODE, STAFF_CONTEXT_CODE, SEGMENT_CODE, SEQUENCE_NUMBER |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
