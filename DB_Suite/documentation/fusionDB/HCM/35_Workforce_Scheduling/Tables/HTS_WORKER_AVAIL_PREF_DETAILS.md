# HTS_WORKER_AVAIL_PREF_DETAILS

Table to store the worker availability preference details.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkeravailprefdetails-30207.html#htsworkeravailprefdetails-30207](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkeravailprefdetails-30207.html#htsworkeravailprefdetails-30207)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORKER_AVAIL_PREF_DETA_PK | AVAILABILITY_PREF_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AVAILABILITY_PREF_DETAIL_ID | NUMBER |  | 18 | Yes | A unique system-generated identifier for worker availability preference detail. |
| AVAILABILITY_PREFERENCE_ID | NUMBER |  | 18 | Yes | Identifier of the availability preference to which the detail belongs. |
| START_TIME_OFFSET | NUMBER |  | 9 | Yes | Defines the start time of availability in offset from midnight in minutes. |
| END_TIME_OFFSET | NUMBER |  | 9 | Yes | Defines the end time of availability in offset from midnight in minutes. |
| REPEAT_DURATION_INDEX | NUMBER |  | 3 |  | Index of the repeat cycle to which the detail belongs. |
| DAY_INDEX | NUMBER |  | 2 |  | Day from the repeat duration index to which this detail belongs. |
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
| HTS_WORKER_AVAIL_PREF_DTLS_N2 | Non Unique | Default | AVAILABILITY_PREFERENCE_ID |
| HTS_WORKER_AVAIL_PREF_DTLS_U1 | Unique | Default | AVAILABILITY_PREF_DETAIL_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
