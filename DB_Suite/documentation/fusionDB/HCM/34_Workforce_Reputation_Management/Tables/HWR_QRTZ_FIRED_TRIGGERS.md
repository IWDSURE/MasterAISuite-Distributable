# HWR_QRTZ_FIRED_TRIGGERS

This is the GRC table for QRTZ_FIRED_TRIGGERS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzfiredtriggers-26504.html#hwrqrtzfiredtriggers-26504](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzfiredtriggers-26504.html#hwrqrtzfiredtriggers-26504)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_FIRED_TRIGGERS_PK | ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ENTRY_ID | VARCHAR2 | 95 |  | Yes | This is the column ENTRY_ID on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| TRIGGER_NAME | VARCHAR2 | 256 |  | Yes | This is the column TRIGGER_NAME on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| TRIGGER_GROUP | VARCHAR2 | 80 |  | Yes | This is the column TRIGGER_GROUP on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| IS_VOLATILE | VARCHAR2 | 1 |  | Yes | This is the column IS_VOLATILE on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| INSTANCE_NAME | VARCHAR2 | 80 |  | Yes | This is the column INSTANCE_NAME on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| FIRED_TIME | NUMBER |  | 13 | Yes | This is the column FIRED_TIME on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| PRIORITY | NUMBER |  | 13 | Yes | This is the column PRIORITY on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| STATE | VARCHAR2 | 16 |  | Yes | This is the column STATE on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| JOB_NAME | VARCHAR2 | 256 |  |  | This is the column JOB_NAME on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| JOB_GROUP | VARCHAR2 | 80 |  |  | This is the column JOB_GROUP on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| IS_STATEFUL | VARCHAR2 | 1 |  |  | This is the column IS_STATEFUL on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| REQUESTS_RECOVERY | VARCHAR2 | 1 |  |  | This is the column REQUESTS_RECOVERY on table HWR_QRTZ_FIRED_TRIGGERS. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_FIRED_TRIGGERS_N1 | Non Unique | FUSION_TS_TX_DATA | JOB_GROUP | Active |
| HWR_QRTZ_FIRED_TRIGGERS_N2 | Non Unique | FUSION_TS_TX_DATA | TRIGGER_NAME, TRIGGER_GROUP | Active |
| HWR_QRTZ_FIRED_TRIGGERS_N5 | Non Unique | FUSION_TS_TX_DATA | IS_VOLATILE | Active |
| HWR_QRTZ_FIRED_TRIGGERS_N6 | Non Unique | FUSION_TS_TX_DATA | REQUESTS_RECOVERY | Active |
| HWR_QRTZ_FIRED_TRIGGERS_N7 | Non Unique | FUSION_TS_TX_DATA | IS_STATEFUL | Active |
| HWR_QRTZ_FIRED_TRIGGERS_N8 | Non Unique | FUSION_TS_TX_DATA | JOB_NAME | Active |
| HWR_QRTZ_FIRED_TRIGGERS_N9 | Non Unique | FUSION_TS_TX_DATA | INSTANCE_NAME | Active |
| HWR_QRTZ_FIRED_TRIGGERS_U1 | Unique | FUSION_TS_TX_DATA | ENTRY_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
