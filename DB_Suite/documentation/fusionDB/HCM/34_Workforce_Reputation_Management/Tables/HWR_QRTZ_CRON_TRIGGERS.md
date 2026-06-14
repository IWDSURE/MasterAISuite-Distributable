# HWR_QRTZ_CRON_TRIGGERS

This is the GRC table for QRTZ_CRON_TRIGGERS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzcrontriggers-16395.html#hwrqrtzcrontriggers-16395](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzcrontriggers-16395.html#hwrqrtzcrontriggers-16395)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_CRON_TRIGGERS_PK | TRIGGER_NAME, TRIGGER_GROUP |

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| TRIGGER_NAME | VARCHAR2 | 256 | Yes | This is the column TRIGGER_NAME on table HWR_QRTZ_CRON_TRIGGERS. | Active |
| TRIGGER_GROUP | VARCHAR2 | 80 | Yes | This is the column TRIGGER_GROUP on table HWR_QRTZ_CRON_TRIGGERS. | Active |
| CRON_EXPRESSION | VARCHAR2 | 80 | Yes | This is the column CRON_EXPRESSION on table HWR_QRTZ_CRON_TRIGGERS. | Active |
| TIME_ZONE_ID | VARCHAR2 | 80 |  | This is the column TIME_ZONE_ID on table HWR_QRTZ_CRON_TRIGGERS. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_CRON_TRIGGERS_U1 | Unique | FUSION_TS_TX_DATA | TRIGGER_NAME, TRIGGER_GROUP | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
