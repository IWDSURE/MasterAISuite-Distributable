# HWP_DATA_MINING_PROCESS

This table contains data mining process values for predictives.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingprocess-22874.html#hwpdataminingprocess-22874](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingprocess-22874.html#hwpdataminingprocess-22874)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_DATA_MINING_PROCESS_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Data Mining process ID. |
| PROCESS_DATE | DATE |  |  |  | Data Mining process date. |
| MODEL_CODE | VARCHAR2 | 200 |  |  | Data mining model code. |
| PRED_ACCURACY | NUMBER |  |  |  | Data mining prediction accuracy. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_DATA_MINING_PROCESS_N1 | Non Unique | Default | MODEL_CODE |
| HWP_DATA_MINING_PROCESS_PK | Unique | Default | PROCESS_ID |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
