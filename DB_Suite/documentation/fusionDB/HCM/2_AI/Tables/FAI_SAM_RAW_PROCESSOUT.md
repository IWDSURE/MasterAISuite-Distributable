# FAI_SAM_RAW_PROCESSOUT

This table stores processout records for sam ai consumption

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawprocessout-8011.html#faisamrawprocessout-8011](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawprocessout-8011.html#faisamrawprocessout-8011)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_PROCESSOUT_DATA_PK | RAW_PROCESSOUT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RAW_PROCESSOUT_ID | NUMBER |  | 18 | Yes | Primary Key of the process out data |
| CONTEXT | VARCHAR2 | 2000 |  |  | Context in which process out data were executed |
| KEY | VARCHAR2 | 2000 |  |  | Unique key of the process out data |
| VALUE | VARCHAR2 | 2400 |  |  | Value of the process out data for a key |
| DATE_DATA | DATE |  |  |  | Date on which this record was executed |
| COLLECTION_TIME | TIMESTAMP |  |  |  | Time of the collection of the process out |
| STATUS | VARCHAR2 | 80 |  |  | Status of the executed record in processout |
| CONSUMER_DATA_KEY | VARCHAR2 | 240 |  |  | Reference Key on the consumer side |
| ANOMALY_LOOP | VARCHAR2 | 80 |  |  | Loop back on accuracy of the anomaly |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES table |
| RAW_LOAD_ID | NUMBER |  | 18 |  | Foreign Key to the fai_sam_raw_load table |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_PROCESSOUT_DATA_PK | Unique | FUSION_TS_TX_IDX | RAW_PROCESSOUT_ID |
| FAI_SAM_RAW_PROCESSOUT_FK | Non Unique | FUSION_TS_TX_IDX | RAW_LOAD_ID |
| FAI_SAM_RAW_PROCESSOUT_N1 | Non Unique | FUSION_TS_TX_IDX | CONSUMER_DATA_KEY |

---

[← Back to Index](../2_AI_Tables_Index.md)
