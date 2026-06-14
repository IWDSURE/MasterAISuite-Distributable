# FAI_IM_DELETE_ENTITY

This table depicts the Candidate IDs or Person IDs that need to be deleted/ are deleted by the GDPR workflow.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiimdeleteentity-26107.html#faiimdeleteentity-26107](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiimdeleteentity-26107.html#faiimdeleteentity-26107)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_IM_DELETE_ENTITY_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | Auto generated primary key for this table 
Incremented by 1 for every new row. |
| APP_NAME | VARCHAR2 | 50 |  | Yes | Name of the app (orc or talent) |
| ENTITY_NAME | VARCHAR2 | 50 |  | Yes | Name of the Entity to delete (Among candidates, persons) |
| DELETE_ENTITY_ID | VARCHAR2 | 100 |  | Yes | Either Candidate ID in ORC or Person ID in Talent for GDPR |
| REQUEST_TIMESTAMP | TIMESTAMP |  |  |  | Depicts the date and time of the candidateID being 
requested to delete via GDPR workflow |
| FULFILL_TIMESTAMP | TIMESTAMP |  |  |  | Depicts the date and time of the candidateID being 
deleted by GDPR workflow from OSCS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_IM_DELETE_ENTITY_PK | Unique | Default | ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
