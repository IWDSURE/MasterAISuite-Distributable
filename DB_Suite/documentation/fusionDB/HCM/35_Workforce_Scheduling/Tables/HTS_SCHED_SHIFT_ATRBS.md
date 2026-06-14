# HTS_SCHED_SHIFT_ATRBS

Table to store schedule shift attributes

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_INTERFACE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedshiftatrbs-28470.html#htsschedshiftatrbs-28470](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedshiftatrbs-28470.html#htsschedshiftatrbs-28470)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_SHIFT_ATRBS_PK | SCHED_SHIFT_ATRB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_SHIFT_ATRB_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| SCHED_REQUEST_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the request as specified by the exporter |
| SCHED_EVENT_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the schedule event as specified by the exporter |
| SCHED_SHIFT_EVENT_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the schedule shift event as specified by the exporter |
| SCHED_SHIFT_ATRB_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the schedule shift attribute as specified by the exporter |
| SCHED_SHIFT_EVENT_ID | NUMBER |  | 18 |  | SCHED_SHIFT_EVENT_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 240 |  |  | Name of the attribute |
| ATTRIBUTE_VALUE | VARCHAR2 | 150 |  |  | Value of the attribute. Stored as a string to cover all alphanumeric values |
| STATUS_IMP | NUMBER |  | 2 |  | Status for the import phase |
| STATUS_INT | NUMBER |  | 2 |  | Status for the internalization phase |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_SHIFT_ATRBS_N1 | Non Unique | FUSION_TS_INTERFACE | SCHED_SHIFT_EVENT_ID |
| HTS_SCHED_SHIFT_ATRBS_N2 | Non Unique | FUSION_TS_INTERFACE | SCHED_SHIFT_ATRB_NUMBER, SCHED_SHIFT_EVENT_NUMBER, SCHED_EVENT_NUMBER, SCHED_REQUEST_NUMBER |
| HTS_SCHED_SHIFT_ATRBS_PK | Unique | FUSION_TS_INTERFACE | SCHED_SHIFT_ATRB_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
