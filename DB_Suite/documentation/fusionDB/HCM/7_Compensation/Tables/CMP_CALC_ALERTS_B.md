# CMP_CALC_ALERTS_B

Stores custom alerts for a plan

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcalcalertsb-13387.html#cmpcalcalertsb-13387](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcalcalertsb-13387.html#cmpcalcalertsb-13387)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CALC_ALERTS_B_PK | ALERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALERT_ID | NUMBER |  | 18 | Yes | ALERT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ALERT_KEY | NUMBER |  | 18 | Yes | ALERT_KEY |
| KEY_TYPE | VARCHAR2 | 30 |  | Yes | KEY_TYPE |
| ALERT_TYPE | VARCHAR2 | 30 |  |  | ALERT_TYPE |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | ENABLED_FLAG |
| QUICK_ALERT_FLAG | VARCHAR2 | 1 |  |  | QUICK_ALERT_FLAG |
| QUICK_ALERT_CODE | VARCHAR2 | 30 |  |  | QUICK_ALERT_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PARTI_PROCESS_ENA | VARCHAR2 | 1 |  |  | PARTI_PROCESS_ENA |
| REFRESH_PROCESS_ENA | VARCHAR2 | 1 |  |  | REFRESH_PROCESS_ENA |
| WRKSHT_SAVE_ENA | VARCHAR2 | 1 |  |  | WRKSHT_SAVE_ENA |
| WRKSHT_TAB_OUT_ENA | VARCHAR2 | 1 |  |  | WRKSHT_TAB_OUT_ENA |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CALC_ALERTS_B_N1 | Non Unique | Default | KEY_TYPE, ALERT_KEY, ALERT_TYPE |
| CMP_CALC_ALERTS_B_UK1 | Unique | Default | ALERT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
