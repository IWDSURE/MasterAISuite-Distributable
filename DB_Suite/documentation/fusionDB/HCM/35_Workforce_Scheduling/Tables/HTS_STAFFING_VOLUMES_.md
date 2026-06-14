# HTS_STAFFING_VOLUMES_

Staffing volume items planned to repeat each day inside some date range.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffingvolumes-19213.html#htsstaffingvolumes-19213](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffingvolumes-19213.html#htsstaffingvolumes-19213)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFFING_VOLUMES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, STAFFING_VOLUME_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAFFING_VOLUME_ID | NUMBER |  | 18 | Yes | System generated ID identifying the volume |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| STAFFING_VOLUME_CODE | VARCHAR2 | 30 |  |  | User Key |
| SCHED_UNIT_ID | NUMBER |  | 18 |  | Foreign key to table HTS_SCHED_UNITS |
| VOLUME_TYPE | VARCHAR2 | 30 |  |  | One of the values of ORA_HTS_WORKLOAD_TYPES lookup:

Baseline, Adjusted, Actual |
| START_DATE | DATE |  |  |  | Start of the date range for which the volume is defined |
| END_DATE | DATE |  |  |  | End of the date range for which the volume is defined |
| START_TIME_OFFSET | NUMBER |  | 9 |  | Start time of the volume saved as offset in minutes from the day start |
| END_TIME_OFFSET | NUMBER |  | 9 |  | End time of the volume saved as offset in minutes from the day start |
| VOLUME_VALUE | NUMBER |  | 18 |  | The volume value |
| VOLUME_INTENSITY_CODE | VARCHAR2 | 80 |  |  | Reference to a unique Volume Intensity Code |
| WEIGHTED_VOLUME_VALUE | NUMBER |  | 18 |  | Volume value weighted by the intensity factor |
| IMPORT_TAG | VARCHAR2 | 30 |  |  | Used if wanted to identify an import batch/file (for later deletion) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to support soft delete. Value 'Y' indicates that the record is deleted. Null or 'N' values indicate the record is not deleted. |
| SHIFT_TYPE_ID | VARCHAR2 | 18 |  |  | Indicates whether the shift is Regular or On-Call or any custom shift type |
| ORIG_SYSTEM_REF | VARCHAR2 | 100 |  |  | External source system for an imported staffing volume |
| SOURCE_SYSTEM_KEY | VARCHAR2 | 100 |  |  | External source system ID for the staffing plan |
| DISTRIBUTED_OVER_TIME | VARCHAR2 | 1 |  |  | True if the volumes proportionate to duration |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_STAFFING_VOLUMES_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, STAFFING_VOLUME_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
