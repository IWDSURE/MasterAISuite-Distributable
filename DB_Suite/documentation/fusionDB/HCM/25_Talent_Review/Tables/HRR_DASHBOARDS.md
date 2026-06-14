# HRR_DASHBOARDS

Talent Review Dashboard transaction table

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrdashboards-29584.html#hrrdashboards-29584](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrdashboards-29584.html#hrrdashboards-29584)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_DASHBOARDS_PK | DASHBOARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DASHBOARD_ID | NUMBER |  | 18 | Yes | Unique identifier |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business group |
| MEETING_ID | NUMBER |  | 18 | Yes | Meeting |
| PERSON_ID | NUMBER |  | 18 | Yes | Person |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment |
| TALENT_SCORE_RT_LVL_ID | NUMBER |  | 18 |  | Talent score rating level |
| TALENT_SCOR_CALB_RT_LVL_ID | NUMBER |  | 18 |  | Talent Score Calibrated Rating Level Id |
| BU_LEADER_DIRECT_ID | NUMBER |  | 18 |  | Business unit leaders direct reports id |
| PERF_RT_LVL_ID | NUMBER |  | 18 |  | Performance rating level |
| PERF_CALIB_RT_LVL_ID | NUMBER |  | 18 |  | Calibrated performance rating level |
| POT_RT_LVL_ID | NUMBER |  | 18 |  | Potential rating level |
| POT_CALIB_RT_LVL_ID | NUMBER |  | 18 |  | Calibrated potential rating level |
| RISK_LOSS_RT_LVL_ID | NUMBER |  | 18 |  | Risk of loss rating level |
| RISK_LOSS_CALIB_RT_LVL_ID | NUMBER |  | 18 |  | Calibrated risk of loss rating level |
| IMPACT_LOSS_RT_LVL_ID | NUMBER |  | 18 |  | Impact of loss rating level |
| IMPACT_LOSS_CALB_RT_LVL_ID | NUMBER |  | 18 |  | Calibrated impact of loss rating level |
| MOBILITY_VALUE | VARCHAR2 | 30 |  |  | Mobility rating (no rating level) |
| MOBILITY_CALIB_VALUE | VARCHAR2 | 30 |  |  | Calibrated mobility rating |
| AGE_GROUP_VALUE | NUMBER |  | 18 |  | Age group |
| EXTN_METRIC_VALUE1 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE1 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE2 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE2 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE3 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE3 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE4 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE4 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE5 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE5 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE6 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE6 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE7 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE7 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE8 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE8 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE9 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE9 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| EXTN_METRIC_VALUE10 | NUMBER |  | 18 |  | Extensible rating level id field. |
| EXTN_METRIC_CALIB_VALUE10 | NUMBER |  | 18 |  | Extensible calibrated rating level id field. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_DASHBOARDS_FK1 | Non Unique | FUSION_TS_TX_DATA | MEETING_ID |
| HRR_DASHBOARDS_PK | Unique | FUSION_TS_TX_DATA | DASHBOARD_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
