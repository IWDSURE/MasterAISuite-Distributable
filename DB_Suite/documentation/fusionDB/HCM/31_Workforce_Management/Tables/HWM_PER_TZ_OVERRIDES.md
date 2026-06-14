# HWM_PER_TZ_OVERRIDES

This table is designed to store time zone overrides of a person against the primary assignment.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmpertzoverrides-23961.html#hwmpertzoverrides-23961](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmpertzoverrides-23961.html#hwmpertzoverrides-23961)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_per_tz_overrides_PK | PER_TZ_OVERRIDE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_TZ_OVERRIDE_ID | NUMBER |  | 18 | Yes | PER_TZ_OVERRIDE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| LOCAL_START_DATE | DATE |  |  | Yes | LOCAL_START_DATE |
| LOCAL_END_DATE | DATE |  |  | Yes | LOCAL_END_DATE |
| TIMEZONE_ID | VARCHAR2 | 50 |  | Yes | TIMEZONE_ID |
| UTC_START_TIME | TIMESTAMP |  |  | Yes | UTC_START_TIME |
| UTC_END_TIME | TIMESTAMP |  |  | Yes | UTC_END_TIME |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hwm_per_tz_overrides_U1 | Unique | Default | PER_TZ_OVERRIDE_ID |
| hwm_per_tz_overrides_U2 | Unique | Default | ASSIGNMENT_ID, LOCAL_START_DATE, LOCAL_END_DATE |
| hwm_per_tz_overrides_U3 | Unique | Default | ASSIGNMENT_ID, UTC_START_TIME, UTC_END_TIME |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
