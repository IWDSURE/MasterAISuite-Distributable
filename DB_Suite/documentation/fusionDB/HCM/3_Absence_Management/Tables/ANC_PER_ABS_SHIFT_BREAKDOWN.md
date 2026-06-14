# ANC_PER_ABS_SHIFT_BREAKDOWN

This table holds information of the shift breakdown for a person absence entry.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsshiftbreakdown-11709.html#ancperabsshiftbreakdown-11709](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsshiftbreakdown-11709.html#ancperabsshiftbreakdown-11709)

## Primary Key

| Name | Columns |
|------|----------|
| anc_per_abs_shift_breakdo_PK | PER_ABS_SHIFT_BREAKDOWN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_SHIFT_BREAKDOWN_ID | NUMBER |  | 18 | Yes | Key identifier for breakdown of shifts. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Identifier. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person identifier. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment identifier. |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | Person absence entry identifier. |
| ABSENCE_TYPE_ID | NUMBER |  | 18 | Yes | Absence type identifier. |
| UOM | VARCHAR2 | 30 |  | Yes | Unit of measure for duration. |
| START_DATETIME | TIMESTAMP |  |  | Yes | Start date and time of the shift entry. |
| END_DATETIME | TIMESTAMP |  |  | Yes | End date and time of the shift entry. |
| DURATION | NUMBER |  |  | Yes | Total duration for the shift entry. |
| DURATION_IN_MILLISECONDS | NUMBER |  |  |  | Total duration in milliseconds |
| SCHEDULE_TYPE | VARCHAR2 | 30 |  | Yes | This denotes time or elapsed schedule type. |
| WORK_SCHEDULE_SHIFT_START | TIMESTAMP |  |  |  | Shift start time as per the work schedule of the person. |
| WORK_SCHEDULE_SHIFT_END | TIMESTAMP |  |  |  | Shift end time as per the work schedule of the person. |
| WORK_SCHEDULE_DURATION | NUMBER |  |  |  | Duration of the shift as per the work schedule of the person. |
| TIME_CARD_BOUNDARY_SPLIT | VARCHAR2 | 1 |  |  | This column is to indicate if Shift breakdown was split due to Timecard boundaries |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_SHIFT_BRKDN_N1 | Non Unique | FUSION_TS_TX_IDX | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_SHIFT_BRKDN_U1 | Unique | Default | PER_ABS_SHIFT_BREAKDOWN_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
