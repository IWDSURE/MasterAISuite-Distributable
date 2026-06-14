# HWR_GBL_PRFL_MTOR_RNK_B

This table is for Mentor Suggestion List for Reputation and Social Roles

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflmtorrnkb-8409.html#hwrgblprflmtorrnkb-8409](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflmtorrnkb-8409.html#hwrgblprflmtorrnkb-8409)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_GBL_PRFL_MTOR_RNK_B_PK | GBL_PRFL_ID, TYPE_OF_RECORD, CONTROL_KEY |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | This is global profile id of the user |
| HWR_ORG_ID | VARCHAR2 | 500 |  | Yes | This column is the org id of the user |
| MNGR_ORG_ID | VARCHAR2 | 500 |  | Yes | This column is the org id of the manager of the user |
| TYPE_OF_RECORD | NUMBER |  | 18 | Yes | This column is the Id indicating the type of the post-control record |
| CONTROL_KEY | VARCHAR2 | 255 |  | Yes | This column is theKey of the control key this record is representing |
| MEAN_GLOBAL_PERCENTILE | NUMBER |  | 18 |  | Mean Global Percentile for score metric at global profile level on the last computed date |
| MEAN_SOC_MED_SCORE | NUMBER |  | 18 |  | Mean Social Media Relevance score at global profile level on the last computed date |
| METRIC_DATE | TIMESTAMP |  |  | Yes | This column is the Date this metric record is for |
| METRIC_ATTR_1 | VARCHAR2 | 80 |  |  | This column is the Metric attribute 1 |
| METRIC_ATTR_2 | VARCHAR2 | 80 |  |  | This column is the Metric attribute 2 |
| METRIC_ATTR_3 | VARCHAR2 | 80 |  |  | This column is the Metric attribute 3 |
| METRIC_ATTR_4 | VARCHAR2 | 80 |  |  | This column is the Metric attribute 4 |
| METRIC_ATTR_5 | VARCHAR2 | 80 |  |  | This column is the Metric attribute 5 |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_GBL_PRFL_MTOR_RNK_B_N1 | Non Unique | FUSION_TS_TX_DATA | TYPE_OF_RECORD, CONTROL_KEY |
| HWR_GBL_PRFL_MTOR_RNK_B_N2 | Non Unique | FUSION_TS_TX_DATA | MNGR_ORG_ID |
| HWR_GBL_PRFL_MTOR_RNK_B_N3 | Non Unique | FUSION_TS_TX_DATA | HWR_ORG_ID |
| HWR_GBL_PRFL_MTOR_RNK_B_U1 | Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID, TYPE_OF_RECORD, CONTROL_KEY |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
