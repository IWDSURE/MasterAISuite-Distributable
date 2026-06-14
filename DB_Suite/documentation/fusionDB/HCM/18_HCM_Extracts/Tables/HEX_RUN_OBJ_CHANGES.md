# HEX_RUN_OBJ_CHANGES

The table stores the object wise sub xml.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunobjchanges-5717.html#hexrunobjchanges-5717](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunobjchanges-5717.html#hexrunobjchanges-5717)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_RUN_OBJ_CHANGES_PK | REPORT_CATEGORY_ID, EXT_RUN_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_RUN_OBJECT_ID | NUMBER |  |  | Yes | The column indicates a unique sequence generated value. |
| PERSON_ID | NUMBER |  | 18 |  | The column indicates the Person ID |
| EXT_RUN_ID | NUMBER |  |  |  | The column indicates the EXT_RUN_ID from HEX_RUNS table. |
| OBJECT_ID | NUMBER |  |  |  | The column indicates the id of the object being processed. |
| REPORT_CATEGORY_ID | NUMBER |  |  | Yes | The column indicates the report category currently being run. |
| CHUNK_NUM | NUMBER |  |  |  | The column indicates the chunk number as part of which the object is being processed. |
| THREAD_NUM | NUMBER |  |  |  | The column indicates the thread number as part of which the object is being processed. |
| ESS_REQUEST_ID | NUMBER |  |  |  | The column idicates the request ID of the sub request. |
| GROUP_TAG_VALUE | VARCHAR2 | 4000 |  |  | The column indicates the reference for the parent child link. |
| OBJ_EXT_STATUS | VARCHAR2 | 1 |  |  | The column indicates the status of the object being processed. |
| RUN_SEQ_NO | NUMBER |  |  |  | The column indicates the version sequence of the object. |
| FRAG_CHECKSUM | VARCHAR2 | 2000 |  |  | The column indicates the checksum for the sub xml for the specific object. |
| CONTENT_VALUE | CLOB |  |  | Yes | The column indicates the sub xml data. |
| CONTENT_TYPE | VARCHAR2 | 30 |  |  | The column indicates the source of the file like XML. |
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
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PREVIOUS_RUN_ID | NUMBER |  |  |  | The column indicates the run id of the previous run. |
| ATTRIBUTE8 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HEX_RUN_OBJ_CHANGES_N1 | Non Unique | Default | REPORT_CATEGORY_ID, EXT_RUN_ID, CHUNK_NUM |  |
| HEX_RUN_OBJ_CHANGES_N2 | Non Unique | Default | REPORT_CATEGORY_ID, OBJECT_ID, RUN_SEQ_NO |  |
| HEX_RUN_OBJ_CHANGES_N3 | Non Unique | Default | REPORT_CATEGORY_ID, GROUP_TAG_VALUE | Obsolete |
| HEX_RUN_OBJ_CHANGES_N4 | Non Unique | Default | REPORT_CATEGORY_ID, OBJ_EXT_STATUS | Obsolete |
| HEX_RUN_OBJ_CHANGES_N5 | Non Unique | Default | REPORT_CATEGORY_ID, ATTRIBUTE_CATEGORY, ATTRIBUTE1 | Obsolete |
| HEX_RUN_OBJ_CHANGES_N6 | Non Unique | Default | REPORT_CATEGORY_ID, PERSON_ID |  |
| HEX_RUN_OBJ_CHANGES_N7 | Non Unique | Default | REPORT_CATEGORY_ID, EXT_RUN_ID, OBJECT_ID |  |
| HEX_RUN_OBJ_CHANGES_PK | Unique | Default | REPORT_CATEGORY_ID, EXT_RUN_OBJECT_ID |  |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
