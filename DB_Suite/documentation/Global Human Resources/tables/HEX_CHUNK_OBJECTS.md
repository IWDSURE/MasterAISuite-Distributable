# HEX_CHUNK_OBJECTS

The table stores the chunk wise object information.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexchunkobjects-30801.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexchunkobjects-30801.html)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_CHUNK_OBJECTS_PK | JOB_ID, CHUNK_NUMBER, OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  |  | Yes | The column indicates the JOB_ID from the HEX_JOBS table. |
| OBJECT_ID | NUMBER |  |  | Yes | The column indicates the id of the object being processed. |
| EXEC_SEQUENCE | NUMBER |  |  |  | The column indicates the execution sequence and required if threading block is sorted. |
| CHUNK_NUMBER | NUMBER |  |  | Yes | The column indicates the number of the chunk which contains the current object. |
| CHUNK_OBJECT_PROCESS_STATUS | VARCHAR2 | 30 |  |  | The column indicates the process status of the object(C-Completed/E-Errored). |
| GROUP_TAG_VALUE | VARCHAR2 | 4000 |  |  | The column is a reference for the parent child block link. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTR1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR2 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR6 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR7 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR8 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR9 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR10 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HEX_CHUNK_OBJECTS_PK | Unique | FUSION_TS_TX_DATA | JOB_ID, CHUNK_NUMBER, OBJECT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
