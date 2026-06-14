# HWR_QRTZ_JOB_LISTENERS

This is the GRC table for QRTZ_JOB_LISTENERS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzjoblisteners-21394.html#hwrqrtzjoblisteners-21394](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzjoblisteners-21394.html#hwrqrtzjoblisteners-21394)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_JOB_LISTENERS_PK | JOB_NAME, JOB_GROUP, JOB_LISTENER |

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| JOB_NAME | VARCHAR2 | 256 | Yes | This is the column JOB_NAME on table HWR_QRTZ_JOB_LISTENERS. | Active |
| JOB_GROUP | VARCHAR2 | 80 | Yes | This is the column JOB_GROUP on table HWR_QRTZ_JOB_LISTENERS. | Active |
| JOB_LISTENER | VARCHAR2 | 80 | Yes | This is the column JOB_LISTENER on table HWR_QRTZ_JOB_LISTENERS. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_JOB_LISTENERS_U1 | Unique | FUSION_TS_TX_DATA | JOB_NAME, JOB_GROUP, JOB_LISTENER | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
