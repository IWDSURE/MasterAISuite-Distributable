# HRC_DL_UI_LOGICAL_LINES

This table contains additional information like Source Reference values, corresponding to a logical row. The data in this table will be used to display on the UI and to ensure easy and quick search operations.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdluilogicallines-5602.html#hrcdluilogicallines-5602](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdluilogicallines-5602.html#hrcdluilogicallines-5602)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_UI_LOGICAL_LINES_PK | LOGICAL_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOGICAL_LINE_ID | NUMBER |  |  | Yes | LOGICAL_LINE_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  |  | Yes | DATA_SET_BUS_OBJ_ID |
| SOURCE_REFERENCE001 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE001 |
| SOURCE_REFERENCE002 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE002 |
| SOURCE_REFERENCE003 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE003 |
| SOURCE_REFERENCE004 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE004 |
| SOURCE_REFERENCE005 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE005 |
| SOURCE_REFERENCE006 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE006 |
| SOURCE_REFERENCE007 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE007 |
| SOURCE_REFERENCE008 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE008 |
| SOURCE_REFERENCE009 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE009 |
| SOURCE_REFERENCE010 | VARCHAR2 | 200 |  |  | SOURCE_REFERENCE010 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_UI_LOGICAL_LINES_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_UI_LOGICAL_LINES_N2 | Non Unique | Default | SOURCE_REFERENCE001 |
| HRC_DL_UI_LOGICAL_LINES_N3 | Non Unique | Default | SOURCE_REFERENCE002 |
| HRC_DL_UI_LOGICAL_LINES_N4 | Non Unique | Default | SOURCE_REFERENCE003 |
| HRC_DL_UI_LOGICAL_LINES_N5 | Non Unique | Default | SOURCE_REFERENCE004 |
| HRC_DL_UI_LOGICAL_LINES_U1 | Unique | Default | LOGICAL_LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
