# HTS_WORKLOAD_PLANS_

Workload demand items planned to repeat each day inside some date range.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkloadplans-3381.html#htsworkloadplans-3381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkloadplans-3381.html#htsworkloadplans-3381)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORKLOAD_PLANS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORKLOAD_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKLOAD_PLAN_ID | NUMBER |  | 18 | Yes | Primary key identifiying the publish event record by a system generated ID |
| WORKLOAD_MODE | VARCHAR2 | 1 |  |  | The import type will indicate either 'T' for time based imports or 'S' for shift based imports. |
| SHIFT_ID | NUMBER |  | 18 |  | Shift ID |
| WORKLOAD_PLAN_CODE | VARCHAR2 | 30 |  |  | Unique identifier for a record provided by the user |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to support soft delete. Value 'Y' indicates that the record is deleted. Null or 'N' values indicate the record is not deleted. |
| WORKLOAD_TYPE | VARCHAR2 | 30 |  |  | Workload import type |
| SKILL_ID | NUMBER |  | 18 |  | Skill ID |
| SHIFT_TYPE_ID | NUMBER |  | 18 |  | Indicates whether the shift is Regular or On-Call or any custom shift type |
| SCHED_UNIT_ID | NUMBER |  | 18 |  | Scheduling Unit ID |
| START_DATE | DATE |  |  |  | Start of the date range for which the window plan is defined |
| END_DATE | DATE |  |  |  | End of the date range for which the workload plan is defined |
| START_TIME_OFFSET | NUMBER |  | 9 |  | Start time of the workload plan saved as offset in minutes from the day start |
| END_TIME_OFFSET | NUMBER |  | 9 |  | End time of the workload plan saved as offset in minutes from the day start |
| INPUT_SOURCE | VARCHAR2 | 30 |  |  | Record source, either import or UI |
| WORKLOAD_VALUE | NUMBER |  | 18 |  | Workload value |
| WORKLOAD_UOM | VARCHAR2 | 30 |  |  | Unit of Measure for the Workload Vaue |
| ORIGIN_SYSTEM_REF | VARCHAR2 | 100 |  |  | External source system for an imported workload plan |
| SOURCE_SYSTEM_KEY | VARCHAR2 | 100 |  |  | External source system ID for the workload plan |
| WORKLOAD_IMPORT_TAG | VARCHAR2 | 30 |  |  | Optional tag to identify an imported set of records |
| MON_FLAG | VARCHAR2 | 1 |  |  | Monday is part of day of week for this workload |
| TUE_FLAG | VARCHAR2 | 1 |  |  | Tuesday is part of day of week for this workload |
| WED_FLAG | VARCHAR2 | 1 |  |  | Wednesday is part of day of week for this workload |
| THU_FLAG | VARCHAR2 | 1 |  |  | Thursday is part of day of week for this workload |
| FRI_FLAG | VARCHAR2 | 1 |  |  | Friday is part of day of week for this workload |
| SAT_FLAG | VARCHAR2 | 1 |  |  | Saturday is part of day of week for this workload |
| SUN_FLAG | VARCHAR2 | 1 |  |  | Sunday is part of day of week for this workload |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MOCK_DISCRIMINATOR | VARCHAR2 | 1 |  |  | MOCK_DISCRIMINATOR |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 80 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WORKLOAD_PLANSN1_ | Non Unique | Default | WORKLOAD_PLAN_ID |
| HTS_WORKLOAD_PLANS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORKLOAD_PLAN_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
