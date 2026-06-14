# FAI_IM_AUDIT

This table is for tracking ingestion and storing historical data.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiimaudit-13551.html#faiimaudit-13551](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiimaudit-13551.html#faiimaudit-13551)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_IM_AUDIT_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | Auto generated primary key for this table Incremented by 1 for every new row. |
| FILE_NAME | VARCHAR2 | 400 |  | Yes | Name of the file (For eg, 1617962340770.json) |
| APP_NAME | VARCHAR2 | 50 |  | Yes | Name of the app (orc or talent) |
| ENTITY_NAME | VARCHAR2 | 50 |  | Yes | Name of the Entity for the file (Among person and model) |
| STEP | VARCHAR2 | 50 |  | Yes | The search engine for which the file ingestion status
is depicted. (can be vectorStore)
Also, it can be stage if the file location is currently in stage folder |
| STATUS | NUMBER |  | 20 | Yes | It depicts the success/failure status for the file for the given step
1000 - file is in stage
1111 -  File has successfully reached OSCS
1112 - File has failed to reach/index to OSCS |
| STATUS_DETAILS | VARCHAR2 | 4000 |  |  | If the file is failed in indexing/ parsing - the error is tracked here.
If status is 1112 → Error represents the number of retries done (1 to 5 and 
Reprocess OSCS File exceeded 5times) |
| RECORD_COUNT | NUMBER |  | 22 |  | It represents the number of records in the file |
| STAGE_TIMESTAMP | TIMESTAMP |  |  |  | It depicts the date and time of the file ingestion in stage folder |
| INDEXED_TIMESTAMP | TIMESTAMP |  |  |  | It depicts the date and time of the file ingestion to OSCS |
| VECTOR_VERSION_STATUS | VARCHAR2 | 20 |  |  | It depicts the level of vector generation of the file.
If "null", V2 vectors are generated.
If "V1V2", both V1 and V2 vectors are generated.
If "V1V2DAS", V2 vectors are generated and V1 embeddings are ready for generation
If "V2V2Complete", V2 vectors and V1 embedding are generated and waiting to reach OSCS
If "V1V2_DAS_ERROR", V2 vectors are generated and file failed to move to DAS.
If "V1V2_COMPLETE_ERROR", V2 vectors and V1 embeddings are generated and file failed to move to complete folder
If "V1V2_INDEX_ERROR", V2 vectors and V1 embeddings are generated and file failed to reach OSCS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_IM_AUDIT_N1 | Non Unique | Default | STEP, ENTITY_NAME, STATUS |
| FAI_IM_AUDIT_PK | Unique | Default | ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
