# BEN_PL_COPY_PARAMS

This table stores parameters required for exporting or importing a plan or program.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcopyparams-28178.html#benplcopyparams-28178](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcopyparams-28178.html#benplcopyparams-28178)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_COPY_PARAMS_PK | PL_COPY_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PL_COPY_ID | NUMBER |  | 18 | Yes | PL_COPY_ID |  |
| EFFECTIVE_DATE | DATE |  |  |  | Export data as of date. |  |
| NAME | VARCHAR2 | 240 |  |  | NAME of the import or export job. |  |
| STATUS | VARCHAR2 | 240 |  |  | STATUS of the import or export job. |  |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |  |
| PL_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_F. |  |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |  |
| REUSE_CODE | VARCHAR2 | 240 |  |  | Code that determines whether existing objects can be reused. |  |
| PREFIX | VARCHAR2 | 240 |  |  | PREFIX for imported objects. |  |
| SUFFIX | VARCHAR2 | 240 |  |  | SUFFIX for imported objects. |  |
| TYPE | VARCHAR2 | 240 |  |  | TYPE |  |
| EMAIL | VARCHAR2 | 240 |  |  | EMAIL |  |
| SEND_NOTIFICATIONS | VARCHAR2 | 30 |  |  | SEND_NOTIFICATIONS |  |
| CONFIG_PARAM | VARCHAR2 | 30 |  |  | CONFIG_PARAM |  |
| IMPORT_MAP | VARCHAR2 | 30 |  |  | IMPORT_MAP |  |
| PROVIDE_MAP | VARCHAR2 | 30 |  |  | PROVIDE_MAP |  |
| IMPORT_PL_DESIGN | VARCHAR2 | 30 |  |  | IMPORT_PL_DESIGN |  |
| REVIEW_PL_DESIGN | VARCHAR2 | 30 |  |  | REVIEW_PL_DESIGN |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| FILE_NAME | VARCHAR2 | 240 |  |  | File Name |  |
| FILEPATH | VARCHAR2 | 240 |  |  | File Path | Obsolete |
| FILE_UPLOADED | VARCHAR2 | 20 |  |  | Status of file upload |  |
| ELIGY_PRFL_ID | NUMBER |  | 18 |  | Eligibility Profile ID |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| REQUEST_STATUS | NUMBER |  | 18 |  | ESS request status. |  |
| MAPPING_REQUEST_ID | NUMBER |  | 18 |  | Mapping ESS Request ID |  |
| MAPPING_REQUEST_STATUS | NUMBER |  | 18 |  | Mapping ESS Request Status |  |
| COMP_OBJ_TYPE | VARCHAR2 | 20 |  |  | COMP_OBJ_TYPE |  |
| NAMED_OBJECTS | CLOB |  |  |  | NAMED_OBJECTS |  |
| PARAM_ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | PARAM_ATTRIBUTE1 |  |
| PARAM_ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | PARAM_ATTRIBUTE2 |  |
| PARAM_ATTRIBUTE3 | VARCHAR2 | 4000 |  |  | PARAM_ATTRIBUTE3 |  |
| PARAM_ATTRIBUTE4 | VARCHAR2 | 4000 |  |  | PARAM_ATTRIBUTE4 |  |
| PARAM_ATTRIBUTE5 | VARCHAR2 | 4000 |  |  | PARAM_ATTRIBUTE5 |  |
| PARAM_ATTRIBUTE_DATE1 | DATE |  |  |  | PARAM_ATTRIBUTE_DATE1 |  |
| PARAM_ATTRIBUTE_DATE2 | DATE |  |  |  | PARAM_ATTRIBUTE_DATE2 |  |
| PARAM_ATTRIBUTE_DATE3 | DATE |  |  |  | PARAM_ATTRIBUTE_DATE3 |  |
| PARAM_ATTRIBUTE_DATE4 | DATE |  |  |  | PARAM_ATTRIBUTE_DATE4 |  |
| PARAM_ATTRIBUTE_DATE5 | DATE |  |  |  | PARAM_ATTRIBUTE_DATE5 |  |
| PARAM_ATTRIBUTE_NUMBER1 | NUMBER |  | 22 |  | PARAM_ATTRIBUTE_NUMBER1 |  |
| PARAM_ATTRIBUTE_NUMBER2 | NUMBER |  | 22 |  | PARAM_ATTRIBUTE_NUMBER2 |  |
| PARAM_ATTRIBUTE_NUMBER3 | NUMBER |  | 22 |  | PARAM_ATTRIBUTE_NUMBER3 |  |
| PARAM_ATTRIBUTE_NUMBER4 | NUMBER |  | 22 |  | PARAM_ATTRIBUTE_NUMBER4 |  |
| PARAM_ATTRIBUTE_NUMBER5 | NUMBER |  | 22 |  | PARAM_ATTRIBUTE_NUMBER5 |  |
| PARAM_ATTRIBUTE_BLOB1 | BLOB |  |  |  | For storing log files. |  |
| PARAM_ATTRIBUTE_BLOB2 | BLOB |  |  |  | For storing log files. |  |
| PARAM_ATTRIBUTE_BLOB3 | BLOB |  |  |  | For storing log files. |  |
| PARAM_ATTRIBUTE_BLOB4 | BLOB |  |  |  | For storing log files. |  |
| PARAM_ATTRIBUTE_BLOB5 | BLOB |  |  |  | For storing log files. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_COPY_PARAMS_PK | Unique | Default | PL_COPY_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
