# HWR_WLNS_USR_SUM

The wellness user summary table stores user metrics by summary date.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsusrsum-18462.html#hwrwlnsusrsum-18462](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsusrsum-18462.html#hwrwlnsusrsum-18462)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_USR_SUM_PK | USER_ID, SUMMARY_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the user wellness table. |
| SUMMARY_DATE | DATE |  |  | Yes | This is the date of the wellness user data summary. |
| STEPS | NUMBER |  |  |  | This is the total number of steps for the date. |
| CALORIES | NUMBER |  |  |  | This is the total number of calories for the date. |
| DISTANCE | NUMBER |  |  |  | This is the total distance for the date. |
| FAIRLY_ACTIVE_TIME | NUMBER |  |  |  | This is the total fairly active time for the date. |
| VERY_ACTIVE_TIME | NUMBER |  |  |  | This is the total very active time for the date. |
| ACTIVE_SCORE | NUMBER |  |  |  | This is the total active score for the date. |
| IS_SEDENTARY | VARCHAR2 | 4 |  |  | This is the sedentary flag for the date. |
| PROJECT_TYPE | VARCHAR2 | 500 |  |  | This is the project type for the date. |
| PERFORMANCE | NUMBER |  |  |  | This is the performance score for the date. |
| STRESS_SCORE | NUMBER |  |  |  | This is the stress score for the date. |
| SOURCE_ID | NUMBER |  | 18 |  | This is the source id of the wellness user data summary. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_USR_SUM_U1 | Unique | FUSION_TS_TX_DATA | USER_ID, SUMMARY_DATE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
