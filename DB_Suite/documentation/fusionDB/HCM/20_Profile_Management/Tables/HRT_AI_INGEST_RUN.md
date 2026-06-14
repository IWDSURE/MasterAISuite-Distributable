# HRT_AI_INGEST_RUN

Table used to track talent profile data ingestion runs for sending to AI.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtaiingestrun-11462.html#hrtaiingestrun-11462](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtaiingestrun-11462.html#hrtaiingestrun-11462)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_AI_INGEST_RUN_PK | INGEST_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INGEST_RUN_ID | NUMBER |  | 18 | Yes | System generated primary key |
| PARENT_REQUEST_ID | NUMBER |  | 18 |  | ESS Request Id of the Parent Job |
| FEATURE | VARCHAR2 | 30 |  |  | Signify the feature like Best Profile Matches or Skill Suggestion |
| ENTITY_TYPE | VARCHAR2 | 30 |  |  | Entity type like PERSON_PROFILE, JOB_MODEL_PROFILE, COMPETENCY_ITEM_CATALOG |
| ENTITY_TYPE_SELECTION | VARCHAR2 | 64 |  |  | Entity type slection like ALL, PERSON_PROFILE, JOB_MODEL_PROFILE, COMPETENCY_ITEM_CATALOG |
| COMPLETION_STATUS | VARCHAR2 | 64 |  |  | Completion Status of the Ingestion run |
| OVERALL_COMPLETION_STATUS | VARCHAR2 | 64 |  |  | Overall Completion Status of the Ingestion runs of an ESS Request |
| FROM_DATE | TIMESTAMP |  |  |  | From Date of profile updates |
| TO_DATE | TIMESTAMP |  |  |  | To  Date of profile updates |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_AI_INGEST_RUN_U1 | Unique | Default | INGEST_RUN_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
