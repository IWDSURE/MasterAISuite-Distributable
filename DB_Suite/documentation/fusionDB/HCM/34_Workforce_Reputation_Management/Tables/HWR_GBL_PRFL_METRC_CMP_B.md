# HWR_GBL_PRFL_METRC_CMP_B

This table is for Metric_Score at Global Profile List for Issue count + Post count - Compliance_data

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflmetrccmpb-20557.html#hwrgblprflmetrccmpb-20557](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflmetrccmpb-20557.html#hwrgblprflmetrccmpb-20557)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_GBL_PRFL_METRC_CMP_B_PK | GBL_PRFL_ID, TYPE_OF_RECORD, CONTROL_KEY, METRIC_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | This column is the global profile id of the user |
| HWR_ORG_ID | VARCHAR2 | 500 |  | Yes | This column is the org id of the user |
| TYPE_OF_RECORD | NUMBER |  | 18 | Yes | This column is the id indicating the type of the post-control record |
| CONTROL_KEY | VARCHAR2 | 80 |  | Yes | This column is the key of the control key this record is representing |
| TOTAL_POST_COUNT | NUMBER |  | 10 | Yes | This column is the total post count for score metric at global profile level |
| TOTAL_ISSUE_COUNT | NUMBER |  | 10 | Yes | This column is the total issue count for score metric at global profile level |
| VELOCITY | NUMBER |  | 18 |  | This column is the mean velocity for score metric at global profile level |
| METRIC_DATE | TIMESTAMP |  |  | Yes | This column is the date this metric record is for |
| GBL_CMP_METRIC_ATTR_1 | VARCHAR2 | 80 |  |  | This column is the global comp metric attribute 1 |
| GBL_CMP_METRIC_ATTR_2 | VARCHAR2 | 80 |  |  | This column is the global comp metric attribute 2 |
| GBL_CMP_METRIC_ATTR_3 | VARCHAR2 | 80 |  |  | This column is the global comp metric attribute 3 |
| GBL_CMP_METRIC_ATTR_4 | VARCHAR2 | 80 |  |  | This column is the global comp metric attribute 4 |
| GBL_CMP_METRIC_ATTR_5 | VARCHAR2 | 80 |  |  | This column is the global comp metric attribute 5 |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_GBL_PRFL_METRC_CMP_B_N1 | Non Unique | FUSION_TS_TX_DATA | TYPE_OF_RECORD, CONTROL_KEY |
| HWR_GBL_PRFL_METRC_CMP_B_N2 | Non Unique | FUSION_TS_TX_DATA | METRIC_DATE |
| HWR_GBL_PRFL_METRC_CMP_B_N3 | Non Unique | FUSION_TS_TX_DATA | HWR_ORG_ID |
| HWR_GBL_PRFL_METRC_CMP_B_U1 | Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID, TYPE_OF_RECORD, CONTROL_KEY, METRIC_DATE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
