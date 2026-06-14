# HWR_VLTR_VOL_JOB_B

this table stores job base information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvoljobb-16381.html#hwrvltrvoljobb-16381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvoljobb-16381.html#hwrvltrvoljobb-16381)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_VOL_JOB_B_PK | VOLUNTEER_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VOLUNTEER_JOB_ID | NUMBER |  | 18 | Yes | VOLUNTEER_JOB_ID |
| STATUS | NUMBER |  | 1 | Yes | STATUS |
| NOTIFY_VOLUNTEERS | NUMBER |  | 1 |  | NOTIFY_VOLUNTEERS |
| JOB_TYPE | VARCHAR2 | 100 |  |  | JOB_TYPE |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 20 |  | Yes | ENTITY_TYPE |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| START_TIME | NUMBER |  | 18 |  | START_TIME |
| END_TIME | NUMBER |  | 18 |  | END_TIME |
| IS_SAME_SCH_SELECTED_DAYS | NUMBER |  | 1 |  | IS_SAME_SCH_SELECTED_DAYS |
| MON_START_TIME | NUMBER |  | 18 |  | MON_START_TIME |
| MON_END_TIME | NUMBER |  | 18 |  | MON_END_TIME |
| TUE_START_TIME | NUMBER |  | 18 |  | TUE_START_TIME |
| TUE_END_TIME | NUMBER |  | 18 |  | TUE_END_TIME |
| WED_START_TIME | NUMBER |  | 18 |  | WED_START_TIME |
| WED_END_TIME | NUMBER |  | 18 |  | WED_END_TIME |
| THU_START_TIME | NUMBER |  | 18 |  | THUR_START_TIME |
| THU_END_TIME | NUMBER |  | 18 |  | THUR_END_TIME |
| FRI_START_TIME | NUMBER |  | 18 |  | FRI_START_TIME |
| FRI_END_TIME | NUMBER |  | 18 |  | FRI_END_TIME |
| SAT_START_TIME | NUMBER |  | 18 |  | SAT_START_TIME |
| SAT_END_TIME | NUMBER |  | 18 |  | SAT_END_TIME |
| SUN_START_TIME | NUMBER |  | 18 |  | SUN_START_TIME |
| SUN_END_TIME | NUMBER |  | 18 |  | SUN_END_TIME |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_VOL_JOB_B_N1 | Non Unique | FUSION_TS_TX_IDX | ENTITY_ID, ENTITY_TYPE |
| HWR_VLTR_VOL_JOB_B_U1 | Unique | FUSION_TS_TX_IDX | VOLUNTEER_JOB_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
