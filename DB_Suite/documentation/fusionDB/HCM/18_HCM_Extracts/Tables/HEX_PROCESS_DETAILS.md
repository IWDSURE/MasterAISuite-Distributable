# HEX_PROCESS_DETAILS

The table stores the runtime diagnostic, designtime diagnostic, exported extract, generated CSV Template, and other process file.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexprocessdetails-7996.html#hexprocessdetails-7996](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexprocessdetails-7996.html#hexprocessdetails-7996)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_PROCESS_DETAILS_PK | PROCESS_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_DETAIL_ID | NUMBER |  | 32 | Yes | The column indicates a unique sequence generated value. |
| PROCESS_CODE | VARCHAR2 | 250 |  |  | The column indicates the process code of generic engine. |
| ESS_PROCESS_ID | NUMBER |  | 32 |  | The column indicates the ess_process_id from the ESS Job. |
| ENTITY_CODE | VARCHAR2 | 250 |  |  | The column indicates the entity code of the generic process. |
| ENTITY_ID | NUMBER |  | 18 |  | The column indicates the entity value of the generic process. |
| SEQUENCE | NUMBER |  | 18 |  | The column indicates the sequence of the generic process run. |
| LATEST | VARCHAR2 | 1 |  |  | The column indicates the whether the run is latest or not. |
| PROCESS_OUTPUT | CLOB |  |  |  | The column contains the output content of the generic process. |
| OUTPUT_CHUNK_NUM | NUMBER |  | 18 |  | The column indicates the chunk number of the output if chunked. |
| STORAGE_TYPE | VARCHAR2 | 100 |  |  | The column indicates the storage type of the output file. |
| OUTPUT_TYPE | VARCHAR2 | 100 |  |  | The column indicates the output type of the output file. |
| STATUS | VARCHAR2 | 100 |  |  | The column indicates the status of the generic process, |
| OUTPUT_NAME | VARCHAR2 | 240 |  |  | The column indicates the output name of the output file. |
| ATTRIBUTE1 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 250 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_PROCESS_DETAILS_N1 | Non Unique | HEX_PROCESS_DETAILS_PK1 | ESS_PROCESS_ID, ENTITY_ID, ENTITY_CODE |
| HEX_PROCESS_DETAILS_PK | Unique | Default | PROCESS_DETAIL_ID |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
