# HWR_QRTZ_SCHEDULER_STATE

This is the GRC table for QRTZ_SCHEDULER_STATE.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzschedulerstate-21588.html#hwrqrtzschedulerstate-21588](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzschedulerstate-21588.html#hwrqrtzschedulerstate-21588)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_SCHEDULER_STATE_PK | INSTANCE_NAME |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INSTANCE_NAME | VARCHAR2 | 80 |  | Yes | This is the column INSTANCE_NAME on table HWR_QRTZ_SCHEDULER_STATE. | Active |
| LAST_CHECKIN_TIME | NUMBER |  | 13 | Yes | This is the column LAST_CHECKIN_TIME on table HWR_QRTZ_SCHEDULER_STATE. | Active |
| CHECKIN_INTERVAL | NUMBER |  | 13 | Yes | This is the column CHECKIN_INTERVAL on table HWR_QRTZ_SCHEDULER_STATE. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_SCHEDULER_STATE_U1 | Unique | FUSION_TS_TX_DATA | INSTANCE_NAME | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
