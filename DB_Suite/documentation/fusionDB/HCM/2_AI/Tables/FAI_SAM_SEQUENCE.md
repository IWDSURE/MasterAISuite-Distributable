# FAI_SAM_SEQUENCE

This table holds the process sequence attached to a sequence defintion.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamsequence-29499.html#faisamsequence-29499](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamsequence-29499.html#faisamsequence-29499)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_SEQUENCE_PK | SEQUENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEQUENCE_ID | NUMBER |  | 18 | Yes | Primary Key of the Sequence Table |
| SEQUENCE | VARCHAR2 | 1000 |  |  | Name of the Sequence in Sequence Table |
| PARENT_SEQUENCE_ID | NUMBER |  |  |  | Foreign Key to the Parent Sequence Id |
| SEQUENCE_DEFINITION_ID | NUMBER |  |  |  | Foreign Key to Sequence Definition in Sequence Table |
| SEQUENCER | VARCHAR2 | 1000 |  |  | Sequencer Used on the sequence in Sequence Table |
| TYPE | VARCHAR2 | 240 |  |  | Type of the Sequence in Sequence Table |
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
| FAI_SAM_SEQUENCE_FK | Non Unique | FUSION_TS_TX_IDX | SEQUENCE_DEFINITION_ID |
| FAI_SAM_SEQUENCE_FK1 | Non Unique | FUSION_TS_TX_IDX | PARENT_SEQUENCE_ID |
| FAI_SAM_SEQUENCE_N1 | Non Unique | FUSION_TS_TX_IDX | POD, PARENT_SEQUENCE_ID |
| FAI_SAM_SEQUENCE_PK | Unique | FUSION_TS_TX_IDX | SEQUENCE_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
