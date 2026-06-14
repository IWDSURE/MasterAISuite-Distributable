# HRC_DL_ROLLBACK_LOG_LINES

This table contains Logical Rows for the data provided in DAT file. Each Logical Row corresponds to one or more physical lines in HRC_DL_ROLLBACK_PHY_LINES. It stores information for the back up data for existing data base data during Load process

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrollbackloglines-5612.html#hrcdlrollbackloglines-5612](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrollbackloglines-5612.html#hrcdlrollbackloglines-5612)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_ROLLBACK_LOG_LINES_PK | LOGICAL_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOGICAL_LINE_ID | NUMBER |  | 18 | Yes | LOGICAL_LINE_ID |
| PARENT_LOGICAL_LINE_ID | NUMBER |  | 18 | Yes | PARENT_LOGICAL_LINE_ID |
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | VO_MAPPING_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_ROLLBACK_LOG_LINES_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_ROLLBACK_LOG_LINES_PK | Unique | Default | LOGICAL_LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
