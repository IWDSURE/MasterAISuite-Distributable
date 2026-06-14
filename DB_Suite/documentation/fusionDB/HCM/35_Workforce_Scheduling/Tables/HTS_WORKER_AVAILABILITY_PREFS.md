# HTS_WORKER_AVAILABILITY_PREFS

Table to store the worker availability preferences.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkeravailabilityprefs-6389.html#htsworkeravailabilityprefs-6389](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkeravailabilityprefs-6389.html#htsworkeravailabilityprefs-6389)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORKER_AVAILABILITY_PR_PK | AVAILABILITY_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| AVAILABILITY_PREFERENCE_ID | NUMBER |  | 18 | Yes | A unique system-generated identifier for worker availability preference. |  |
| AVAILABILITY_PREFERENCE_TYPE | VARCHAR2 | 30 |  | Yes | Type of worker availability. |  |
| REASON | VARCHAR2 | 30 |  |  | Reason corresponding to availability preference type | Obsolete |
| REASON_ID | NUMBER |  | 18 |  | Reason corresponding to availability preference type |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Unique identifier of the person to which the availability preference belongs. |  |
| START_DATE | DATE |  |  | Yes | Start date of the worker availability preference. |  |
| END_DATE | DATE |  |  | Yes | End date of the worker availability preference. |  |
| REPEAT_CYCLE | VARCHAR2 | 30 |  | Yes | Repeating cycle of worker availability preference. |  |
| REPEAT_DURATION | NUMBER |  | 3 |  | Defines the duration of repeat cycle. |  |
| COMMENTS | VARCHAR2 | 4000 |  |  | Comments given by the worker at the time of creating/updating preference. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise |  |
| ALL_DAY_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the Availability Preference covers the entire day. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WORKER_AVAIL_PREFS_N1 | Non Unique | Default | PERSON_ID, START_DATE, END_DATE |
| HTS_WORKER_AVAIL_PREFS_U1 | Unique | Default | AVAILABILITY_PREFERENCE_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
