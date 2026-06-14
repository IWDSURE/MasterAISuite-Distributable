# HTS_STAFFING_VOLUMES

Staffing volume items planned to repeat each day inside some date range.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffingvolumes-14100.html#htsstaffingvolumes-14100](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffingvolumes-14100.html#htsstaffingvolumes-14100)

## Primary Key

| Name | Columns |
|------|----------|
| hts_staffing_volumes_PK | STAFFING_VOLUME_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAFFING_VOLUME_ID | NUMBER |  | 18 | Yes | System generated ID identifying the volume |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| STAFFING_VOLUME_CODE | VARCHAR2 | 30 |  | Yes | User Key |
| SCHED_UNIT_ID | NUMBER |  | 18 | Yes | Foreign key to table HTS_SCHED_UNITS |
| VOLUME_TYPE | VARCHAR2 | 30 |  | Yes | One of the values of ORA_HTS_WORKLOAD_TYPES lookup:

Baseline, Adjusted, Actual |
| START_DATE | DATE |  |  |  | Start of the date range for which the volume is defined |
| END_DATE | DATE |  |  |  | End of the date range for which the volume is defined |
| START_TIME_OFFSET | NUMBER |  | 9 |  | Start time of the volume saved as offset in minutes from the day start |
| END_TIME_OFFSET | NUMBER |  | 9 |  | End time of the volume saved as offset in minutes from the day start |
| VOLUME_VALUE | NUMBER |  | 18 |  | The volume value |
| VOLUME_INTENSITY_CODE | VARCHAR2 | 80 |  |  | Reference to a unique Volume Intensity Code |
| WEIGHTED_VOLUME_VALUE | NUMBER |  | 18 |  | Volume value weighted by the intensity factor |
| IMPORT_TAG | VARCHAR2 | 30 |  |  | Used if wanted to identify an import batch/file (for later deletion) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to support soft delete. Value 'Y' indicates that the record is deleted. Null or 'N' values indicate the record is not deleted. |
| SHIFT_TYPE_ID | VARCHAR2 | 18 |  |  | Indicates whether the shift is Regular or On-Call or any custom shift type |
| ORIG_SYSTEM_REF | VARCHAR2 | 100 |  |  | External source system for an imported staffing volume |
| SOURCE_SYSTEM_KEY | VARCHAR2 | 100 |  |  | External source system ID for the staffing plan |
| DISTRIBUTED_OVER_TIME | VARCHAR2 | 1 |  |  | True if the volumes proportionate to duration |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_STAFFING_VOLUMES_N1 | Non Unique | Default | STAFFING_VOLUME_CODE |
| HTS_STAFFING_VOLUMES_N2 | Non Unique | Default | SCHED_UNIT_ID, VOLUME_TYPE, START_DATE, END_DATE |
| HTS_STAFFING_VOLUMES_PK | Unique | Default | STAFFING_VOLUME_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
