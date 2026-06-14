# HWR_QRTZ_TRIGGERS

This is the GRC table for QRTZ_TRIGGERS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtztriggers-10556.html#hwrqrtztriggers-10556](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtztriggers-10556.html#hwrqrtztriggers-10556)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_TRIGGERS_PK | TRIGGER_NAME, TRIGGER_GROUP |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TRIGGER_NAME | VARCHAR2 | 256 |  | Yes | This is the column TRIGGER_NAME on table HWR_QRTZ_TRIGGERS. | Active |
| TRIGGER_GROUP | VARCHAR2 | 80 |  | Yes | This is the column TRIGGER_GROUP on table HWR_QRTZ_TRIGGERS. | Active |
| JOB_NAME | VARCHAR2 | 256 |  | Yes | This is the column JOB_NAME on table HWR_QRTZ_TRIGGERS. | Active |
| JOB_GROUP | VARCHAR2 | 80 |  | Yes | This is the column JOB_GROUP on table HWR_QRTZ_TRIGGERS. | Active |
| IS_VOLATILE | VARCHAR2 | 1 |  | Yes | This is the column IS_VOLATILE on table HWR_QRTZ_TRIGGERS. | Active |
| DESCRIPTION | VARCHAR2 | 120 |  |  | This is the column DESCRIPTION on table HWR_QRTZ_TRIGGERS. | Active |
| NEXT_FIRE_TIME | NUMBER |  | 13 |  | This is the column NEXT_FIRE_TIME on table HWR_QRTZ_TRIGGERS. | Active |
| PREV_FIRE_TIME | NUMBER |  | 13 |  | This is the column PREV_FIRE_TIME on table HWR_QRTZ_TRIGGERS. | Active |
| PRIORITY | NUMBER |  | 13 |  | This is the column PRIORITY on table HWR_QRTZ_TRIGGERS. | Active |
| TRIGGER_STATE | VARCHAR2 | 16 |  | Yes | This is the column TRIGGER_STATE on table HWR_QRTZ_TRIGGERS. | Active |
| TRIGGER_TYPE | VARCHAR2 | 8 |  | Yes | This is the column TRIGGER_TYPE on table HWR_QRTZ_TRIGGERS. | Active |
| START_TIME | NUMBER |  | 13 | Yes | This is the column START_TIME on table HWR_QRTZ_TRIGGERS. | Active |
| END_TIME | NUMBER |  | 13 |  | This is the column END_TIME on table HWR_QRTZ_TRIGGERS. | Active |
| CALENDAR_NAME | VARCHAR2 | 80 |  |  | This is the column CALENDAR_NAME on table HWR_QRTZ_TRIGGERS. | Active |
| MISFIRE_INSTR | NUMBER |  | 2 |  | This is the column MISFIRE_INSTR on table HWR_QRTZ_TRIGGERS. | Active |
| JOB_DATA | BLOB |  |  |  | This is the column JOB_DATA on table HWR_QRTZ_TRIGGERS. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_TRIGGERS_N1 | Non Unique | FUSION_TS_TX_DATA | IS_VOLATILE | Active |
| HWR_QRTZ_TRIGGERS_N2 | Non Unique | FUSION_TS_TX_DATA | NEXT_FIRE_TIME | Active |
| HWR_QRTZ_TRIGGERS_N3 | Non Unique | FUSION_TS_TX_DATA | TRIGGER_STATE | Active |
| HWR_QRTZ_TRIGGERS_N4 | Non Unique | FUSION_TS_TX_DATA | JOB_NAME, JOB_GROUP |  |
| HWR_QRTZ_TRIGGERS_U1 | Unique | FUSION_TS_TX_DATA | TRIGGER_NAME, TRIGGER_GROUP | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
