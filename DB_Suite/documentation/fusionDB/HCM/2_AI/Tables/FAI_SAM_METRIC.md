# FAI_SAM_METRIC

This table holds the functional metrics

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisammetric-14532.html#faisammetric-14532](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisammetric-14532.html#faisammetric-14532)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_METRIC_PK | METRIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| METRIC_ID | NUMBER |  | 18 | Yes | Primary Key of the Metric Table |
| KEY | VARCHAR2 | 240 |  | Yes | Metric Name or Key in Metric Table |
| VALUE | NUMBER |  | 18 | Yes | Value of the Metric in Metric Table |
| TYPE | VARCHAR2 | 80 |  |  | Type of the Metric in Metric Table |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of the Metric in Metric Table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES Table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_METRIC_N1 | Non Unique | FUSION_TS_TX_IDX | TYPE, KEY, CREATION_DATE |
| FAI_SAM_METRIC_PK | Unique | FUSION_TS_TX_IDX | METRIC_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
