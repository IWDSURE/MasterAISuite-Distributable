# FAI_SAM_SEQUENCE_DEF_LIST_OBJ

This table holds the sequence definition object

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamsequencedeflistobj-13134.html#faisamsequencedeflistobj-13134](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamsequencedeflistobj-13134.html#faisamsequencedeflistobj-13134)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_SEQ_DEF_LIST_OBJ_PK | SEQUENCE_DEF_LIST_OBJ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEQUENCE_DEF_LIST_OBJ_ID | NUMBER |  | 18 | Yes | Primary Key of Sequence Definition List Object |
| BASE_SEQUENCE_OBJ_ID | NUMBER |  |  |  | Foreign Key of Base Sequence Object Id |
| SEQUENCE_DEFINITION_ID | NUMBER |  |  |  | Foreign Key of sequence definition |
| SEQUENCER_OVERWRITE | VARCHAR2 | 80 |  |  | Overwrite for the sequencer in Sequence Base Table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES Table |
| POD | VARCHAR2 | 24 |  |  | Internal Column Apex Version FAPOD in FA Tables |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_SEQ_DEF_LIST_OBJ_FK | Non Unique | FUSION_TS_TX_IDX | BASE_SEQUENCE_OBJ_ID |
| FAI_SAM_SEQ_DEF_LIST_OBJ_FK1 | Non Unique | FUSION_TS_TX_IDX | SEQUENCE_DEFINITION_ID |
| FAI_SAM_SEQ_DEF_LIST_OBJ_PK | Unique | FUSION_TS_TX_IDX | SEQUENCE_DEF_LIST_OBJ_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
