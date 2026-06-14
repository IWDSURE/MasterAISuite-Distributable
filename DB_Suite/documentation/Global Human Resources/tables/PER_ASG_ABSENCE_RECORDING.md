# PER_ASG_ABSENCE_RECORDING

This table is stores the details of Absences recorded at the Assignment level. In case if an absence record created spans across multiple assignments, then the corresponding individual assignment level details are stored in this table. Actual Absence details can be found in the PER_ABSENCE_ATTENDANCES, but the impact of an Absence on an Assignment is stored in this table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgabsencerecording-3709.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgabsencerecording-3709.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASG_ABSENCE_RECORDING_PK | ASG_ABSENCE_RECORDING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASG_ABSENCE_RECORDING_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ABSENCE_ATTENDANCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ABSENCE_ATTENDANCES table. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ALL_ASSIGNMENTS_M table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS table. Identifies the person. |
| AUTHORISING_PERSON_ID | NUMBER |  | 18 |  | No longer used. |
| REPLACEMENT_PERSON_ID | NUMBER |  | 18 |  | ID of the person who is replacing the worker during the absence. Only HR administrator users can update this value while recording the absence. |
| ABSENCE_DAYS | NUMBER |  | 9 |  | Absence duration calculated in days. |
| ABSENCE_HOURS | NUMBER |  | 9 |  | Absence duration calculated in hours. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ASG_ABSENCE_RECORDING_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ASG_ABS_RECORDING_FK1 | Non Unique | Default | ABSENCE_ATTENDANCE_ID |
| PER_ASG_ABS_RECORDING_N1 | Non Unique | Default | PERSON_ID, ASSIGNMENT_ID |
| PER_ASG_ABS_RECORDING_N3 | Non Unique | Default | ASSIGNMENT_ID |
| PER_ASG_ABS_RECORDING_PK | Unique | Default | ASG_ABSENCE_RECORDING_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
