# HTS_SCHED_FULL_VALIDATIONS

This table embodies the schedule validation execution and acts as a parent/root for the KPIs and schedule violation detailed information.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedfullvalidations-28630.html#htsschedfullvalidations-28630](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedfullvalidations-28630.html#htsschedfullvalidations-28630)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_FULL_VALIDATIONS_PK | SCHED_FULL_VALIDATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_FULL_VALIDATION_ID | NUMBER |  | 18 | Yes | The ID of the schedule validation execution. |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | The ID of the schedule the validation was run on. |
| PERIOD_START_DATE | DATE |  |  | Yes | The start date of the schedule period. |
| PERIOD_END_DATE | DATE |  |  | Yes | The end date of the schedule period. |
| SCHEDULE_UNIT_ID | NUMBER |  | 18 | Yes | The ID of the schedule unit associated with the validated schedule. |
| ORIGIN_LOOKUP_TYPE | VARCHAR2 | 30 |  | Yes | The lookup type denoting the validation origin enumeration. |
| ORIGIN_LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | The lookup code denoting the validation origin enumeration value. |
| VALIDATION_INSTANT | TIMESTAMP |  |  | Yes | The moment the validation was executed. |
| JOB_REQUEST_ID | NUMBER |  | 18 |  | The identifier of the ESS full schedule validation job associated with the run information. |
| VALIDATION_PROCESS_ID | NUMBER |  | 18 |  | The identifier of the top level logical process embodying the full validation. |
| LAST_VALIDATION_FLAG | VARCHAR2 | 1 |  | Yes | A flag indicating if the full validation is the last one or not. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | EnterpriseId |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_FULL_VALIDATIONS_N1 | Non Unique | Default | SCHEDULE_ID |
| HTS_SCHED_FULL_VALIDATIONS_N2 | Non Unique | Default | PERIOD_START_DATE, SCHEDULE_UNIT_ID |
| HTS_SCHED_FULL_VALIDATIONS_PK | Unique | Default | SCHED_FULL_VALIDATION_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
