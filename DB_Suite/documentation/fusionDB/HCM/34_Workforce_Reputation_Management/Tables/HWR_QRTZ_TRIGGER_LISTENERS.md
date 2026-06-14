# HWR_QRTZ_TRIGGER_LISTENERS

This is the GRC table for QRTZ_TRIGGER_LISTENERS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtztriggerlisteners-27872.html#hwrqrtztriggerlisteners-27872](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtztriggerlisteners-27872.html#hwrqrtztriggerlisteners-27872)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_TRIGGER_LISTENERS_PK | TRIGGER_NAME, TRIGGER_GROUP, TRIGGER_LISTENER |

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| TRIGGER_NAME | VARCHAR2 | 256 | Yes | This is the column TRIGGER_NAME on table HWR_QRTZ_TRIGGER_LISTENERS. | Active |
| TRIGGER_GROUP | VARCHAR2 | 80 | Yes | This is the column TRIGGER_GROUP on table HWR_QRTZ_TRIGGER_LISTENERS. | Active |
| TRIGGER_LISTENER | VARCHAR2 | 80 | Yes | This is the column TRIGGER_LISTENER on table HWR_QRTZ_TRIGGER_LISTENERS. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_TRIGGER_LISTENERS_U1 | Unique | FUSION_TS_TX_DATA | TRIGGER_NAME, TRIGGER_GROUP, TRIGGER_LISTENER | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
