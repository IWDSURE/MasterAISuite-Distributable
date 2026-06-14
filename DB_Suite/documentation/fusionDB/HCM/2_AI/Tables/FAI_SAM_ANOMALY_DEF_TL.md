# FAI_SAM_ANOMALY_DEF_TL

Table to hold the translation of the anomalies definition

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamanomalydeftl-20939.html#faisamanomalydeftl-20939](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamanomalydeftl-20939.html#faisamanomalydeftl-20939)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_ANOMALY_DEF_TL_PK | ANOMALY_DEF_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANOMALY_DEF_ID | NUMBER |  | 18 | Yes | Primary Key Anomaly Definition Table |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| DETECTION_MEANING | VARCHAR2 | 150 |  |  | Meaning of the anomaly detection |
| DEFAULT_REMEDY | VARCHAR2 | 240 |  |  | Anomaly Detection Default Remedy |
| DEFAULT_SYMPTOM | CLOB |  |  |  | Default Symptom Description for detection |
| DESCRIPTION | VARCHAR2 | 3200 |  |  | Anomaly Detection object Description |
| THRESHOLD_DEFINITION | VARCHAR2 | 2000 |  |  | Description of the threshold in anomaly definition |
| THRESHOLD_VALUE_DEFINITION | VARCHAR2 | 2000 |  |  | Description of the threshold value |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES Table |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_ANOMALY_DEF_TL_U1 | Unique | FUSION_TS_SEED | ANOMALY_DEF_ID, LANGUAGE, ORA_SEED_SET1 |
| FAI_SAM_ANOMALY_DEF_TL_U2 | Unique | FUSION_TS_SEED | ANOMALY_DEF_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
