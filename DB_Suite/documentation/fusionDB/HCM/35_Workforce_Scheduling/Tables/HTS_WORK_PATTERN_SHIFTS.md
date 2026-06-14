# HTS_WORK_PATTERN_SHIFTS

Table to store the work pattern shift information.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternshifts-18385.html#htsworkpatternshifts-18385](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternshifts-18385.html#htsworkpatternshifts-18385)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORK_PATTERN_SHIFTS_PK | WORK_PATTERN_SHIFT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_SHIFT_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for a work pattern shift. |
| WORK_PATTERN_SHIFT_CODE | VARCHAR2 | 30 |  |  | Unique code entered when creating a work pattern shift, in order to help user identify the work pattern shift. |
| WORK_PATTERN_ID | NUMBER |  | 18 | Yes | Identifier of the work pattern to which this shift pertains. |
| DAY_INDEX | NUMBER |  | 9 | Yes | Day of the work pattern to which this shift is associated. |
| SHIFT_ID | NUMBER |  | 18 |  | Identifier of the shift from shifts library associated to the work pattern. |
| START_TIME_OFFSET | NUMBER |  | 9 |  | Offset from midnight. Defines the start time of the work pattern shift in minutes. |
| END_TIME_OFFSET | NUMBER |  | 9 |  | Offset from midnight. Defines the end time of the work pattern shift in minutes. |
| DURATION | NUMBER |  | 9 | Yes | Duration of the shift in minutes. |
| BREAK_DURATION | NUMBER |  | 9 |  | Unpaid break duration of the shift. |
| PAID_BREAK_DURATION | NUMBER |  | 9 |  | Paid break duration of the shift. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WORK_PATTERN_SHIFTS_N1 | Non Unique | Default | WORK_PATTERN_ID |
| HTS_WORK_PATTERN_SHIFTS_U1 | Unique | Default | WORK_PATTERN_SHIFT_ID |
| HTS_WORK_PATTERN_SHIFTS_U2 | Unique | Default | WORK_PATTERN_SHIFT_CODE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
