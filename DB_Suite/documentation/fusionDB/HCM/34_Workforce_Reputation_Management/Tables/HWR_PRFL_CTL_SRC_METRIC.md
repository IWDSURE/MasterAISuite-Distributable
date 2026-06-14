# HWR_PRFL_CTL_SRC_METRIC

The profile control source metric table stores the metric info.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprflctlsrcmetric-13779.html#hwrprflctlsrcmetric-13779](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprflctlsrcmetric-13779.html#hwrprflctlsrcmetric-13779)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PRFL_CTL_SRC_METRIC_PK | PRFL_ID, CONTROL_KEY, SOURCE_TYPE_ID, METRIC_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PRFL_ID | VARCHAR2 | 500 |  | Yes | The profile ID for this metric. |  |
| TYPE_OF_RECORD | NUMBER |  | 18 | Yes | Type indicating the type of the post-control record |  |
| CONTROL_KEY | VARCHAR2 | 64 |  | Yes | The control type key for this metric. |  |
| SOURCE_TYPE_ID | NUMBER |  | 18 | Yes | The id of source type for this metric. |  |
| SCORE_VALUE | NUMBER |  |  |  | The score value for score metric. | Obsolete |
| POST_COUNT | NUMBER |  |  |  | The number of post counted for compliance summary metric. |  |
| ISSUE_COUNT | NUMBER |  |  |  | The number of issue counted for compliance summary metric. |  |
| GLOBAL_PERCENTILE | NUMBER |  |  |  | The global percentile for score metric. |  |
| LOCAL_PERCENTILE | NUMBER |  |  |  | The local percentile for score metric. |  |
| METRIC_DATE | TIMESTAMP |  |  | Yes | The date this metric was recorded. |  |
| METRIC_ATTRIBUTE_1 | VARCHAR2 | 80 |  |  | This column is to contain Metric Attribute 1. |  |
| METRIC_ATTRIBUTE_2 | VARCHAR2 | 80 |  |  | This column is to contain Metric Attribute 2. |  |
| METRIC_ATTRIBUTE_3 | VARCHAR2 | 80 |  |  | This column is to contain Metric Attribute 3. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PRFL_CTL_SRC_METRIC_N1 | Non Unique | FUSION_TS_TX_DATA | METRIC_DATE |
| HWR_PRFL_CTL_SRC_METRIC_N2 | Non Unique | FUSION_TS_TX_DATA | TYPE_OF_RECORD, CONTROL_KEY |
| HWR_PRFL_CTL_SRC_METRIC_N3 | Non Unique | FUSION_TS_TX_DATA | PRFL_ID, SOURCE_TYPE_ID |
| HWR_PRFL_CTL_SRC_METRIC_U1 | Unique | FUSION_TS_TX_DATA | PRFL_ID, CONTROL_KEY, SOURCE_TYPE_ID, METRIC_DATE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
