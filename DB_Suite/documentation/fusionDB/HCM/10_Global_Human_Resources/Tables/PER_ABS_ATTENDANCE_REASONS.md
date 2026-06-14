# PER_ABS_ATTENDANCE_REASONS

PER_ABS_ATTENDANCE_REASONS holds the list of absence reasons that may
apply to an absence or attendance type. Reasons are selected from the
list of values defined for the lookup ABSENCE_REASON.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsattendancereasons-11915.html#perabsattendancereasons-11915](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsattendancereasons-11915.html#perabsattendancereasons-11915)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ABS_ATTENDANCE_REASONS_PK | ABS_ATTENDANCE_REASON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ABS_ATTENDANCE_REASON_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ABSENCE_ATTENDANCE_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ABSENCE_ATTENDANCE_TYPES_B table. |
| NAME | VARCHAR2 | 30 |  | Yes | Denotes the name for Absence Attendance reason. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ABS_ATTEND_REASONS_PK | Unique | Default | ABS_ATTENDANCE_REASON_ID |
| PER_ABS_ATTEND_REASONS_U1 | Unique | Default | ABSENCE_ATTENDANCE_TYPE_ID, NAME, LEGISLATIVE_DATA_GROUP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
