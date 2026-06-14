# HTS_SCHED_UNITS

Table containing a unique or distinct list of departments, locations, or other possible scheduling units in the future, and that defines the group to be staffed as part of the schedule generation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedunits-24506.html#htsschedunits-24506](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedunits-24506.html#htsschedunits-24506)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_UNITS_PK | SCHED_UNIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_UNIT_ID | NUMBER |  | 18 | Yes | Primary key identifiying the publish event record by a system generated ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_UNIT_CODE | VARCHAR2 | 30 |  | Yes | SCHED_UNIT_CODE |
| MEMBER_TYPE | VARCHAR2 | 30 |  | Yes | MEMBER_TYPE |
| MEMBER_ID | NUMBER |  | 18 |  | MEMBER_ID |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TIMEZONE_CODE | VARCHAR2 | 100 |  |  | Time Zone Code |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_UNITS_PK | Unique | FUSION_TS_TX_IDX | SCHED_UNIT_ID |
| HTS_SCHED_UNITS_U1 | Unique | HTS_SCHED_UNITS_U1 | SCHED_UNIT_CODE |
| HTS_SCHED_UNITS_U2 | Unique | HTS_SCHED_UNITS_U2 | MEMBER_TYPE, MEMBER_ID, LOCATION_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
