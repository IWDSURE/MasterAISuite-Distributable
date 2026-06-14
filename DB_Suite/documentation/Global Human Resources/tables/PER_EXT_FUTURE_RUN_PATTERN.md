# PER_EXT_FUTURE_RUN_PATTERN

Extract Future Run Pattern table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** per_ext_future_run_pattern

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextfuturerunpattern-21100.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextfuturerunpattern-21100.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_FUTURE_RUN_PATTERN_PK | EXT_FUT_RUN_PATTERN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_FUT_RUN_PATTERN_ID | NUMBER |  | 18 | Yes | EXT_FUT_RUN_PATTERN_ID |
| FLOW_INSTANCE_ID | NUMBER |  | 18 |  | FLOW_INSTANCE_ID |
| FLOW_INSTANCE_NAME | VARCHAR2 | 200 |  |  | FLOW_INSTANCE_NAME |
| BASE_FLOW_ID | NUMBER |  | 18 |  | BASE_FLOW_ID |
| ANALYSIS_RESULT | CLOB |  |  |  | ANALYSIS_RESULT |
| ACTIVE_STATUS | VARCHAR2 | 1 |  |  | ACTIVE_STATUS |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_FUTURE_RUN_PATTERN_FK1 | Non Unique | PER_EXT_FUTURE_RUN_PATTERN_FK1 | FLOW_INSTANCE_ID |
| PER_EXT_FUTURE_RUN_PATTERN_PK | Unique | PER_EXT_FUTURE_RUN_PATTERN_PK | EXT_FUT_RUN_PATTERN_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
