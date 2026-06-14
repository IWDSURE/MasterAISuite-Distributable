# FAI_SAM_SEQUENCE_DEFINITION

This table hods the sequence definition

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamsequencedefinition-13891.html#faisamsequencedefinition-13891](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamsequencedefinition-13891.html#faisamsequencedefinition-13891)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_SEQUENCE_DEFINITION_PK | SEQUENCE_DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEQUENCE_DEFINITION_ID | NUMBER |  | 18 | Yes | Primary Key of the Sequence Definition |
| TYPE | VARCHAR2 | 20 |  |  | Type of the Sequence Definition |
| BASE_SEQUENCE_DEF_ID | NUMBER |  |  |  | Foreign Key to Base Sequence Definition |
| MONITORING_NAME | VARCHAR2 | 500 |  |  | Name of the Monitoring similar to Payroll Name |
| PERIOD_TYPE | VARCHAR2 | 50 |  |  | Type of the Sequence Period like Monthly Weekly |
| FIRST_START_TIME | TIMESTAMP |  |  |  | First Start Time of the Monitoring Period |
| FIRST_STOP_TIME | TIMESTAMP |  |  |  | First Stop Time of the Monitoring Period |
| SEQUENCER | VARCHAR2 | 1000 |  |  | Sequencer for the sequence definition |
| SEQUENCE_INFO | VARCHAR2 | 2000 |  |  | More information about the sequence |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES Table |
| POD | VARCHAR2 | 24 |  |  | Internal Column Apex Version FAPOD in This Table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_SEQUENCE_DEFINITION_N1 | Non Unique | FUSION_TS_TX_IDX | SEQUENCE_DEFINITION_ID, POD |
| FAI_SAM_SEQ_DEFINITION_FK | Non Unique | FUSION_TS_TX_IDX | BASE_SEQUENCE_DEF_ID |
| FAI_SAM_SEQ_DEFINITION_N2 | Non Unique | FUSION_TS_TX_IDX | MONITORING_NAME, POD |
| FAI_SAM_SEQ_DEFINITION_PK | Unique | FUSION_TS_TX_IDX | SEQUENCE_DEFINITION_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
