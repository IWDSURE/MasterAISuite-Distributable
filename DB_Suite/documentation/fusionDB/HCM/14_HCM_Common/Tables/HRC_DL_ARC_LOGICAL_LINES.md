# HRC_DL_ARC_LOGICAL_LINES

This table contains Logical Rows for the data provided in DAT file. Each Logical Row corresponds to one or more physical lines in HRC_DL_PHYSICAL_LINES. It also holds information of its status value during IMPORT, LOAD and VALIDATE which helps to calculate status counts for a given data set business Object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlarclogicallines-14095.html#hrcdlarclogicallines-14095](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlarclogicallines-14095.html#hrcdlarclogicallines-14095)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_ARC_LOGICAL_LINES_PK | LOGICAL_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOGICAL_LINE_ID | NUMBER |  | 18 | Yes | LOGICAL_LINE_ID |
| PARENT_LOGICAL_LINE_ID | NUMBER |  | 18 | Yes | PARENT_LOGICAL_LINE_ID |
| IMPORTED_STATUS | VARCHAR2 | 30 |  | Yes | IMPORTED_STATUS |
| VALIDATED_LOADED_STATUS | VARCHAR2 | 30 |  | Yes | VALIDATED_LOADED_STATUS |
| ROLLBACK_STATUS | VARCHAR2 | 30 |  |  | ROLLBACK_STATUS |
| SKIPPED_STATUS | VARCHAR2 | 1 |  | Yes | SKIPPED_STATUS |
| CORRECTED_STATUS | VARCHAR2 | 1 |  | Yes | CORRECTED_STATUS |
| CHUNK_ID | NUMBER |  | 18 | Yes | CHUNK_NUM |
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | VO_MAPPING_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROCESSING_ORDER | NUMBER |  | 18 |  | PROCESSING_ORDER |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| UI_USER_KEY | VARCHAR2 | 240 |  |  | UI_USER_KEY |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_IDENTIFIER | VARCHAR2 | 100 |  |  | OBJECT_IDENTIFIER |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_ARC_LOGICAL_LINES_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_ARC_LOGICAL_LINES_N2 | Non Unique | Default | PARENT_LOGICAL_LINE_ID |
| HRC_DL_ARC_LOGICAL_LINES_PK | Unique | Default | LOGICAL_LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
