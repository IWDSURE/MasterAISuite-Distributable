# HTS_CUSTOM_SHIFT_TYPES_B

Table to store Shift related data.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscustomshifttypesb-9069.html#htscustomshifttypesb-9069](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscustomshifttypesb-9069.html#htscustomshifttypesb-9069)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_CUSTOM_SHIFT_TYPES_B_PK | SHIFT_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHIFT_TYPE_ID | NUMBER |  |  | Yes | Shift identifier to uniquely identify a shift |
| START_TIME_MS_NUM | NUMBER |  | 18 |  | Start Time for shift detail in milliseconds from midnight. |
| END_TIME_MS_NUM | NUMBER |  | 18 |  | End Time for shift in milliseconds from mignight |
| DURATION_MS_NUM | NUMBER |  | 18 |  | Duration for shift detail in milliseconds from start time. |
| DURATION_UOM_CODE | VARCHAR2 | 30 |  |  | Unit of measure in which duration is entered for a Shift. |
| SHIFT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | A Shift can have following types - Time, Duration and Elapsed. Time shifts are used to track fixed work timings. They have a specific start time and end time. Duration shifts are used when the resource does not have a fixed start time and end time but rather works for certain number of hours, is off for some hours, again works for some number of hours and so on. Elapsed shifts are used when a resource can work a set number of hours anytime during the day. |
| SHORT_TXT | VARCHAR2 | 3 |  |  | Short Code can be used to display a Shift when visualizing a Schedule. Since this is a three letter code it takes less space than the Name. |
| CATEGORY_CODE | VARCHAR2 | 30 |  |  | Category can be used to group Shifts. |
| GLOBAL_FLAG | VARCHAR2 | 1 |  |  | GLOBAL_FLAG |
| AVAILABILITY_CODE | VARCHAR2 | 30 |  |  | Period Type defines whether the resource is working (Work Period) or not working (Off Period) during the Shift. |
| SHIFT_DTL_TYPE_CODE | VARCHAR2 | 30 |  |  | Shift Slices divide the Shift into further intervals. Slice types can be Punch (having fixed start and end times) and Flex (having flexible start and end times). |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | This column is to support soft delete. Possible values 'Y' or 'N'. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SHIFT_SHORT_NAME | VARCHAR2 | 5 |  |  | SHIFT_SHORT_NAME |
| SHIFT_COLOUR | VARCHAR2 | 20 |  |  | SHIFT_COLOUR |
| START_EARLY_GRACE | NUMBER |  | 18 |  | Clock integration Start Early grace period for violation |
| START_LATE_GRACE | NUMBER |  | 18 |  | Clock integration Start late grace period for violation |
| END_EARLY_GRACE | NUMBER |  | 18 |  | Clock integration End early grace period for violation |
| END_LATE_GRACE | NUMBER |  | 18 |  | Clock integration End late grace period for violation |
| TOLERANCE | NUMBER |  | 9 |  | Clock integration Threshold to ignore violation |
| START_EARLY_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration Start Early violation message |
| START_LATE_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration Start late violation message |
| END_EARLY_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration End early violation message |
| END_LATE_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration End late violation message |
| TIME_NOT_WORKED | NUMBER |  | 18 |  | TIME_NOT_WORKED |
| DAY_INDICATOR | VARCHAR2 | 32 |  |  | Day indicator for next day and previous day w.r.t ref date |
| SHIFT_CODE | VARCHAR2 | 64 |  |  | SHIFT_CODE |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_CUSTOM_SHIFT_TYPES_B_N20 | Non Unique | Default | SGUID |
| HTS_CUSTOM_SHIFT_TYPES_B_U1 | Unique | FUSION_TS_SEED | SHIFT_TYPE_ID, ORA_SEED_SET1 |
| HTS_CUSTOM_SHIFT_TYPES_B_U11 | Unique | FUSION_TS_SEED | SHIFT_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
