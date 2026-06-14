# HEX_RUN_OBJ_PROCESS

The table stores the processing data for both full and changes only.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunobjprocess-13009.html#hexrunobjprocess-13009](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunobjprocess-13009.html#hexrunobjprocess-13009)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_RUN_OBJ_PROCESS_PK | EXT_RUN_ID, EXT_RUN_OBJ_PRC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_RUN_OBJ_PRC_ID | NUMBER |  |  | Yes | The column indicates a unique sequence generated value. |
| EXT_RUN_ID | NUMBER |  |  | Yes | The column indicates the EXT_RUN_ID from HEX_RUNS table. |
| CONTENT_VALUE | CLOB |  |  |  | The column indicates the sub xml data. |
| CONTENT_TYPE | VARCHAR2 | 30 |  |  | The column indicates the source of the file like XML. |
| GROUP_TAG_VALUE | VARCHAR2 | 4000 |  |  | The column indicates the reference for the parent child link. |
| OBJECT_ID | NUMBER |  |  |  | The column indicates the id of the object being processed. |
| PROCESS_STATUS | VARCHAR2 | 30 |  |  | The column indicates the status of the sub process. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HEX_RUN_OBJ_PROCESS_N1 | Non Unique | Default | EXT_RUN_ID, GROUP_TAG_VALUE | Obsolete |
| HEX_RUN_OBJ_PROCESS_N2 | Non Unique | Default | EXT_RUN_ID, OBJECT_ID |  |
| HEX_RUN_OBJ_PROCESS_N3 | Non Unique | Default | EXT_RUN_ID, GROUP_TAG_VALUE, PROCESS_STATUS |  |
| HEX_RUN_OBJ_PROCESS_N4 | Non Unique | Default | EXT_RUN_ID, ATTRIBUTE_CATEGORY, ATTRIBUTE1 | Obsolete |
| HEX_RUN_OBJ_PROCESS_PK | Unique | Default | EXT_RUN_ID, EXT_RUN_OBJ_PRC_ID |  |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
