# HWR_QRTZ_CALENDARS

This is the GRC table for QRTZ_CALENDARS.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzcalendars-17955.html#hwrqrtzcalendars-17955](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrqrtzcalendars-17955.html#hwrqrtzcalendars-17955)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_QRTZ_CALENDARS_PK | CALENDAR_NAME |

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| CALENDAR_NAME | VARCHAR2 | 80 | Yes | This is the column CALENDAR_NAME on table HWR_QRTZ_CALENDARS. | Active |
| CALENDAR | BLOB |  | Yes | This is the column CALENDAR on table HWR_QRTZ_CALENDARS. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_QRTZ_CALENDARS_U1 | Unique | FUSION_TS_TX_DATA | CALENDAR_NAME | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
