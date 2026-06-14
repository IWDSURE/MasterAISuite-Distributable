# HTS_SCHED_VIOLATIONS

This table denotes the schedule violation messages that were raised during schedule validation execution.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedviolations-7293.html#htsschedviolations-7293](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedviolations-7293.html#htsschedviolations-7293)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_VIOLATIONS_PK | SCHED_VIOLATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_VIOLATION_ID | NUMBER |  | 18 | Yes | The unique ID of the violation. |
| SCHED_FULL_VALIDATION_ID | NUMBER |  | 18 | Yes | The full validation this validation error is associated with. |
| VALIDATION_LOOKUP_TYPE | VARCHAR2 | 30 |  | Yes | The lookup type containing the code identifying the type of validation leading to raise the violation |
| VALIDATION_LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | The lookup code (combined with the lookup type above) identifying  the validation error type. |
| CONSTRAINT_ID | NUMBER |  | 18 |  | The ID of some object denoting the constraint that is violated. |
| CONSTRAINT_TYPE_CODE | VARCHAR2 | 30 |  |  | A code indicating what kind of constraint is identified by the field
CONSTRAINT_ID. |
| CONSTRAINT_SET_ID | NUMBER |  | 18 |  | The ID of some object acting as the constraint container. |
| SEVERITY_LOOKUP_TYPE | VARCHAR2 | 30 |  | Yes | The lookup type containing the severity codes. |
| SEVERITY_LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | The constraint violation severity code. |
| PERSON_ID | NUMBER |  | 18 |  | The identifier of the worker. It can be null when the validation violation does not concern a worker. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | The identifier of the involved assignment when the validation violation is related to the assignment. |
| SCOPE_CODE | VARCHAR2 | 30 |  | Yes | The scope of the validation/error. |
| SCOPE_START_DATE | DATE |  |  |  | Start date of the temporal range derived from the scope of the validation error. |
| SCOPE_END_DATE | DATE |  |  |  | End date of the temporal range derived from the scope of the validation error. |
| SCOPE_START_REF_DATE | DATE |  |  |  | The reference start date (accounting for day start time) of the temporal range derived from the scope of the validation error. |
| SCOPE_END_REF_DATE | DATE |  |  |  | The reference end date (accounting for day start time) of the temporal range derived from the scope of the validation error. |
| SKILL_ID | NUMBER |  | 18 |  | The identifier of the skill involved in the validation violation. |
| VIOLATION_MESSAGE_CODE | VARCHAR2 | 30 |  | Yes | The code identifying the validation violation message. |
| VIOLATION_MESSAGE | VARCHAR2 | 1000 |  | Yes | The error message formatted using the preferences of the user running the full schedule validation. |
| MESSAGE_LANGUAGE | VARCHAR2 | 30 |  | Yes | The language used to generate the "default" violation message. |
| RESOLVED | VARCHAR2 | 1 |  |  | Indicates whether a schedule validation violation has been resolved. |
| INCREMENTAL | VARCHAR2 | 1 |  |  | Indicates whether a violation was captured by an incremental validation execution (i.e., not through the initial full validation execution). |
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
| HTS_SCHED_VIOLATIONS_N1 | Non Unique | Default | SCHED_FULL_VALIDATION_ID |
| HTS_SCHED_VIOLATIONS_PK | Unique | Default | SCHED_VIOLATION_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
