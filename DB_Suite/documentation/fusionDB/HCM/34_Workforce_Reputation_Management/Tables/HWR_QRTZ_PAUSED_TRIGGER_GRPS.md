# HWR_QRTZ_PAUSED_TRIGGER_GRPS

This is the GRC table for QRTZ_PAUSE_TGER_GRPS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzpausedtriggergrps-13409.html#hwrqrtzpausedtriggergrps-13409](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzpausedtriggergrps-13409.html#hwrqrtzpausedtriggergrps-13409)

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| TRIGGER_GROUP | VARCHAR2 | 80 | Yes | This is the column TRIGGER_GROUP on table HWR_QRTZ_PAUSED_TRIGGER_GRPS. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_PASD_TRGR_GRPS_U1 | Unique | FUSION_TS_TX_DATA | TRIGGER_GROUP | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
