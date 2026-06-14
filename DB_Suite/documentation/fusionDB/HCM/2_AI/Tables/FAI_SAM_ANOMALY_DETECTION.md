# FAI_SAM_ANOMALY_DETECTION

This table holds the AI anomalies detection

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamanomalydetection-13396.html#faisamanomalydetection-13396](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamanomalydetection-13396.html#faisamanomalydetection-13396)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_ANOMALY_DETECTION_PK | ANOMALY_DETECTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANOMALY_DETECTION_ID | NUMBER |  | 18 | Yes | Primary Key for anomaly detection |
| DETECTION_OBJECT_ID | NUMBER |  |  |  | Detection Object Id, for process it is the FK with fai_sam_one_view_process table |
| DETECTION_KEY | VARCHAR2 | 80 |  |  | Definition Key of the Anomaly Detection |
| DETAIL_INFO | VARCHAR2 | 2000 |  |  | More Information about the detection |
| SEQUENCE_ID | NUMBER |  |  |  | Foreign Key to the fai_sam_sequence table |
| ANOMALY_LOOP | VARCHAR2 | 80 |  |  | Loop back to the AI on accuracy of the detection |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES table |
| POD | VARCHAR2 | 24 |  |  | Internal Column Apex Version FAPOD in FA |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_ANOMALY_DETECTION_N1 | Non Unique | FUSION_TS_TX_IDX | POD, DETECTION_KEY, DETECTION_OBJECT_ID |
| FAI_SAM_ANOMALY_DETECTION_PK | Unique | FUSION_TS_TX_IDX | ANOMALY_DETECTION_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
