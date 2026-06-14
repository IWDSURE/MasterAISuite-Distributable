# BEN_PL_COPY_MAP

This table stores the list of objects that require mapping while exporting or importing a plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcopymap-5251.html#benplcopymap-5251](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcopymap-5251.html#benplcopymap-5251)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_COPY_MAP_PK | PL_COPY_MAP_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_COPY_MAP_ID | NUMBER |  | 18 | Yes | PL_COPY_MAP_ID |
| COMP_OBJ_ID | NUMBER |  | 18 |  | Compensation Object ID |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Compensation Object Type |
| COMP_OBJ_NAME | VARCHAR2 | 240 |  |  | Compensation Object Name |
| PL_COPY_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_COPY_PARAMS Table. |
| TABLE_NAME | VARCHAR2 | 240 |  |  | TABLE_NAME |
| SRC_ID | NUMBER |  | 18 |  | Object id in the source DB. |
| TRG_ID | NUMBER |  | 18 |  | Object id in the target DB. |
| SRC_NAME | VARCHAR2 | 240 |  |  | Object name in the source DB. |
| TRG_NAME | VARCHAR2 | 240 |  |  | Object name in the target DB. |
| MAPPING_REQUEST_ID | NUMBER |  | 18 |  | MAPPING_REQUEST_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COLUMN_NAME | VARCHAR2 | 240 |  |  | Column Name |
| SRC_TABLE_NAME | VARCHAR2 | 240 |  |  | Source Table Name |
| MAP_ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | MAP_ATTRIBUTE1 |
| MAP_ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | MAP_ATTRIBUTE2 |
| MAP_ATTRIBUTE3 | VARCHAR2 | 4000 |  |  | MAP_ATTRIBUTE3 |
| MAP_ATTRIBUTE4 | VARCHAR2 | 4000 |  |  | MAP_ATTRIBUTE4 |
| MAP_ATTRIBUTE5 | VARCHAR2 | 4000 |  |  | MAP_ATTRIBUTE5 |
| MAP_ATTRIBUTE_DATE1 | DATE |  |  |  | MAP_ATTRIBUTE_DATE1 |
| MAP_ATTRIBUTE_DATE2 | DATE |  |  |  | MAP_ATTRIBUTE_DATE2 |
| MAP_ATTRIBUTE_DATE3 | DATE |  |  |  | MAP_ATTRIBUTE_DATE3 |
| MAP_ATTRIBUTE_DATE4 | DATE |  |  |  | MAP_ATTRIBUTE_DATE4 |
| MAP_ATTRIBUTE_DATE5 | DATE |  |  |  | MAP_ATTRIBUTE_DATE5 |
| MAP_ATTRIBUTE_NUMBER1 | NUMBER |  | 22 |  | MAP_ATTRIBUTE_NUMBER1 |
| MAP_ATTRIBUTE_NUMBER2 | NUMBER |  | 22 |  | MAP_ATTRIBUTE_NUMBER2 |
| MAP_ATTRIBUTE_NUMBER3 | NUMBER |  | 22 |  | MAP_ATTRIBUTE_NUMBER3 |
| MAP_ATTRIBUTE_NUMBER4 | NUMBER |  | 22 |  | MAP_ATTRIBUTE_NUMBER4 |
| MAP_ATTRIBUTE_NUMBER5 | NUMBER |  | 22 |  | MAP_ATTRIBUTE_NUMBER5 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_COPY_MAP_N1 | Non Unique | Default | SRC_ID, TRG_ID |
| BEN_PL_COPY_MAP_N2 | Non Unique | Default | PL_COPY_ID, TABLE_NAME, COLUMN_NAME, SRC_TABLE_NAME |
| BEN_PL_COPY_MAP_PK | Unique | Default | PL_COPY_MAP_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
