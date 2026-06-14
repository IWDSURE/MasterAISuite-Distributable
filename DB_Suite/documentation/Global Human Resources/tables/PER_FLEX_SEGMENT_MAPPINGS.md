# PER_FLEX_SEGMENT_MAPPINGS

This table stores mapping between source flexfields to destination flexfields.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perflexsegmentmappings-26450.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perflexsegmentmappings-26450.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_FLEX_SEGMENT_MAPPINGS_PK | FLEX_SEGMENT_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FLEX_SEGMENT_MAPPING_ID | NUMBER |  | 18 | Yes | This uniquely identifies a mapping | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This specifies the id for an enterprise | Active |
| SOURCE_DFF_CODE | VARCHAR2 | 40 |  |  | This field holds the flexfield code of source mapping | Active |
| SOURCE_CONTEXT_CODE | VARCHAR2 | 80 |  |  | This field holds the context code of source mapping | Active |
| SOURCE_SEGMENT_CODE | VARCHAR2 | 30 |  |  | This field holds the segment code of source mapping | Active |
| DESTINATION_DFF_CODE | VARCHAR2 | 40 |  |  | This field holds the flexfield code of destination mapping | Active |
| DESTINATION_CONTEXT_CODE | VARCHAR2 | 80 |  |  | This field holds the context code of destination mapping | Active |
| DESTINATION_SEGMENT_CODE | VARCHAR2 | 40 |  |  | This field holds the segment code of destination mapping | Active |
| MAPPING_TYPE | VARCHAR2 | 30 |  |  | This field holds the mapping type | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_FLEX_SEGMENT_MAPPINGS_PK | Unique | FUSION_TS_TX_IDX | FLEX_SEGMENT_MAPPING_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
