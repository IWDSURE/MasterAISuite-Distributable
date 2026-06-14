# BEN_PRTL_MO_RT_PRTN_VAL_F

BEN_PRTL_MO_RT_PRTN_VAL_F identifies how to prorate rates , in those cases when a participant's enrollment coverage date falls within a month and the plan requires that  rates be prorated based upon the date during the month the participant's coverage started.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtlmortprtnvalf-19890.html#benprtlmortprtnvalf-19890](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtlmortprtnvalf-19890.html#benprtlmortprtnvalf-19890)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTL_MO_RT_PRTN_VAL_F_PK | PRTL_MO_RT_PRTN_VAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTL_MO_RT_PRTN_VAL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |
| TO_DY_MO_NUM | NUMBER |  | 18 |  | To day month number. |
| FROM_DY_MO_NUM | NUMBER |  | 18 |  | From day of the month. |
| PCT_VAL | NUMBER |  |  |  | Percent value. |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STRT_R_STP_CVG_CD | VARCHAR2 | 30 |  |  | Start or stop coverage code. |
| PRTL_MO_PRORTN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |
| CVG_AMT_CALC_MTHD_ID | NUMBER |  | 18 |  | Foreign key to BEN_CVG_AMT_CALC_MTHD_F. |
| NUM_DAYS_MONTH | NUMBER |  |  |  | Number of days in month applicable to proration. |
| PRORATE_BY_DAY_TO_MON_FLAG | VARCHAR2 | 30 |  | Yes | Method of proration based on percentage value, rule or day of month. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_P_MO_RT_PRTN_VAL_F_N1 | Non Unique | Default | ACTY_BASE_RT_ID |
| BEN_P_MO_RT_PRTN_VAL_F_N3 | Non Unique | Default | ACTL_PREM_ID |
| BEN_P_MO_RT_PRTN_VAL_F_N4 | Non Unique | Default | CVG_AMT_CALC_MTHD_ID |
| BEN_P_MO_RT_PRTN_VAL_F_PK | Unique | Default | PRTL_MO_RT_PRTN_VAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
