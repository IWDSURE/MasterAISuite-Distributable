# HTS_WORK_PATTERN_BREAKS

Table to store the work pattern break information.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternbreaks-11603.html#htsworkpatternbreaks-11603](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternbreaks-11603.html#htsworkpatternbreaks-11603)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORK_PATTERN_BREAKS_PK | WORK_PATTERN_BREAK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_BREAK_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for a work pattern break. |
| WORK_PATTERN_BREAK_CODE | VARCHAR2 | 30 |  |  | Unique code entered when creating a work pattern break, in order to help user identify the work pattern break. |
| PARENT_RECORD_ID | NUMBER |  | 18 | Yes | Identifier of the work pattern shift or exception to which this break pertains. |
| PARENT_RECORD_TYPE | VARCHAR2 | 30 |  | Yes | Identifies if break is for a work pattern shift or exception. |
| WORK_PATTERN_TYPE_BREAK_ID | NUMBER |  | 18 |  | Identifier of the work pattern type break associated to this work pattern break. |
| BREAK_TYPE_CODE | VARCHAR2 | 30 |  |  | Identifies the break type. |
| BREAK_PAID_CODE | VARCHAR2 | 30 |  |  | Identifies whether the break is a paid or unpaid break. |
| START_TIME_OFFSET | NUMBER |  | 9 |  | Offset from midnight. Defines the start time of the work pattern break in minutes. |
| END_TIME_OFFSET | NUMBER |  | 9 |  | Offset from midnight. Defines the end time of the work pattern break in minutes. |
| DURATION | NUMBER |  | 9 | Yes | Duration of the break in minutes. |
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
| HTS_WORK_PATTERN_BREAKS_N1 | Non Unique | Default | PARENT_RECORD_ID, PARENT_RECORD_TYPE |
| HTS_WORK_PATTERN_BREAKS_U1 | Unique | Default | WORK_PATTERN_BREAK_ID |
| HTS_WORK_PATTERN_BREAKS_U2 | Unique | Default | WORK_PATTERN_BREAK_CODE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
