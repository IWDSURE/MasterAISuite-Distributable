# FAI_SAM_ANOMALY_DEF_B

This table hold the anomalies definitions

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamanomalydefb-27566.html#faisamanomalydefb-27566](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamanomalydefb-27566.html#faisamanomalydefb-27566)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_ANOMALY_DEF_B_PK | ANOMALY_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANOMALY_DEF_ID | NUMBER |  | 18 | Yes | Primary Key Anomaly Definition Table |
| DETECTION_KEY | VARCHAR2 | 1000 |  | Yes | Key of the Detection object row |
| SEND_TO | VARCHAR2 | 2400 |  |  | List of email to send the detection |
| PRIORITY | NUMBER |  |  |  | Priority of the anomaly Detection |
| THRESHOLD | VARCHAR2 | 2000 |  |  | Threshold for the anomaly detection |
| THRESHOLD_ON_VALUE | VARCHAR2 | 2000 |  |  | Threshold on specific value of the detection |
| DETECTION_GROUP | VARCHAR2 | 240 |  |  | Group of anomaly detection object |
| DETECTION_LEVEL | VARCHAR2 | 80 |  |  | To whom the detection record belog to |
| OVERWRITE_PRODUCT | VARCHAR2 | 80 |  |  | Threshold Overwrite at the produce level |
| GRACE_PERIOD | NUMBER |  |  |  | Grace Period before rechecking on the detection |
| DETECTION_TYPE | VARCHAR2 | 80 |  |  | Type of anomaly Detection record |
| DETECTION_OBJECT | VARCHAR2 | 2000 |  |  | Object of the anomaly detection object |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES table |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_ANOMALY_DEF_B_N1 | Non Unique | FUSION_TS_TX_IDX | DETECTION_KEY |
| FAI_SAM_ANOMALY_DEF_B_U1 | Unique | FUSION_TS_SEED | ANOMALY_DEF_ID, ORA_SEED_SET1 |
| FAI_SAM_ANOMALY_DEF_B_U2 | Unique | FUSION_TS_SEED | ANOMALY_DEF_ID, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
