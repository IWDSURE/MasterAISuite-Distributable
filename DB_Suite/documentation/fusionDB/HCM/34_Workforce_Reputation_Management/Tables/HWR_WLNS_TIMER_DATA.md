# HWR_WLNS_TIMER_DATA

This table holds the wellness timer data

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstimerdata-12754.html#hwrwlnstimerdata-12754](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstimerdata-12754.html#hwrwlnstimerdata-12754)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_TIMER_DATA_PK | USER_ID, START_TIME |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ID | VARCHAR2 | 64 |  | Yes | This column contains the user id |
| ACTIVITY_TYPE | VARCHAR2 | 100 |  |  | Used to store the Activity Type related to timer activities. |
| START_TIME | TIMESTAMP |  |  | Yes | This column holds the start time of the timer |
| END_TIME | TIMESTAMP |  |  |  | This column holds the end time of the timer |
| ELAPSED_TIME | NUMBER |  | 18 |  | This column stores the elapsed time between Start and Pause event |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_TIMER_DATA_U1 | Unique | FUSION_TS_TX_DATA | USER_ID, START_TIME |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
