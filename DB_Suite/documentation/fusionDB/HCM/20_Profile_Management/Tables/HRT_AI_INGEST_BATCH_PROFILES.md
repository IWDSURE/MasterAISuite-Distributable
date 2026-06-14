# HRT_AI_INGEST_BATCH_PROFILES

The profile or contetnt type ids for the inhest batches

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtaiingestbatchprofiles-18516.html#hrtaiingestbatchprofiles-18516](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtaiingestbatchprofiles-18516.html#hrtaiingestbatchprofiles-18516)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_AI_INGEST_BATCH_PRF_PK | BATCH_ID, PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ID | NUMBER |  | 18 | Yes | Primary key, Batch Id from HRT_AI_INGEST_BATCHES |
| PROFILE_ID | NUMBER |  | 18 | Yes | Primary key, Profile ID or ContentTypeId |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_AI_INGEST_BATCH_PRF_PK | Unique | Default | BATCH_ID, PROFILE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
