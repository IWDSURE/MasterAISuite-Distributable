# FAI_SAM_MONITORING_PERIOD

This table holds the monitoring period

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisammonitoringperiod-13822.html#faisammonitoringperiod-13822](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisammonitoringperiod-13822.html#faisammonitoringperiod-13822)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_MONITORING_PERIOD_PK | MONITORING_PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MONITORING_PERIOD_ID | NUMBER |  | 18 | Yes | Primary Key of the monitoring period table |
| SEQUENCE_DEFINITION_ID | NUMBER |  |  | Yes | Foreign Key on fai_sam_sequence_definition table |
| PERIOD_TYPE | VARCHAR2 | 80 |  |  | Period Type of the monitoring period |
| START_TIME | TIMESTAMP |  |  | Yes | Start Time of the monitoring period |
| STOP_TIME | TIMESTAMP |  |  | Yes | Stop Time of the monitoring period |
| PERIOD_ORDER | NUMBER |  |  |  | Order of the monitoring period in the set of a sequence defintion |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES Table |
| POD | VARCHAR2 | 24 |  |  | Internal Column Apex Version FAPOD in FA |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_MONITORING_PERIOD_FK | Non Unique | FUSION_TS_TX_IDX | SEQUENCE_DEFINITION_ID |
| FAI_SAM_MONITORING_PERIOD_N1 | Non Unique | FUSION_TS_TX_IDX | POD, SEQUENCE_DEFINITION_ID |
| FAI_SAM_MONITORING_PERIOD_PK | Unique | FUSION_TS_TX_IDX | MONITORING_PERIOD_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
