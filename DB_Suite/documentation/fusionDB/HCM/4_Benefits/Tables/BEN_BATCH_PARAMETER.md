# BEN_BATCH_PARAMETER

BEN_BATCH_PARAMETER identifies the number of threads, the chunk size per thread, and maximum  number of errors allowed per thread before that thread is errored,  for each benefits concurrent  manager process and business group.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchparameter-31644.html#benbatchparameter-31644](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchparameter-31644.html#benbatchparameter-31644)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_PARAMETER_PK | BATCH_PARAMETER_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_PARAMETER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BATCH_EXE_CD | VARCHAR2 | 30 |  |  | Batch process name. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| THREAD_CNT_NUM | NUMBER |  | 18 |  | Number of threads. |
| MAX_ERR_NUM | NUMBER |  | 18 |  | Maximum error number. |
| CHUNK_SIZE | NUMBER |  | 18 |  | Size of each chunk for concurrent process. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BATCH_PARAMETER_PK1 | Unique | Default | BATCH_PARAMETER_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| BEN_BATCH_PARAMETER_PK11 | Unique | Default | BATCH_PARAMETER_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
