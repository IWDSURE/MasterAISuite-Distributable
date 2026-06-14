# FAI_SAM_BASE_SEQ_DEF_LIST_OBJ

Table that holds the base sequence definition list object

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisambaseseqdeflistobj-28364.html#faisambaseseqdeflistobj-28364](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisambaseseqdeflistobj-28364.html#faisambaseseqdeflistobj-28364)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_BASE_SEQ_LIST_OBJ_PK | BASE_SEQ_DEF_LIST_OBJ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BASE_SEQ_DEF_LIST_OBJ_ID | NUMBER |  | 18 | Yes | Primary Key for the Base sequence Defintion List Object |
| BASE_SEQUENCE_OBJ_ID | NUMBER |  |  |  | Foreign Key to fai_sam_base_sequence_obj_b table |
| BASE_SEQUENCE_DEF_ID | NUMBER |  |  |  | Foreign Key to fai_sam_base_sequence_def_b table |
| SEQUENCER_OVERWRITE | VARCHAR2 | 80 |  |  | The Sequencer to Overwrite default sequencer from base sequence defintion |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_BASE_SEQ_LIST_OBJ_FK | Non Unique | FUSION_TS_TX_IDX | BASE_SEQUENCE_OBJ_ID |
| FAI_SAM_BASE_SEQ_LIST_OBJ_FK1 | Non Unique | FUSION_TS_TX_IDX | BASE_SEQUENCE_DEF_ID |
| FAI_SAM_BASE_SEQ_LIST_OBJ_PK | Unique | FUSION_TS_TX_IDX | BASE_SEQ_DEF_LIST_OBJ_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
