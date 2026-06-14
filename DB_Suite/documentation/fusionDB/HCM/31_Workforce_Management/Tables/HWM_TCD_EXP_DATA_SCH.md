# HWM_TCD_EXP_DATA_SCH

This table contains details for Time Clock Device export data for Schedule

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdatasch-5810.html#hwmtcdexpdatasch-5810](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdatasch-5810.html#hwmtcdexpdatasch-5810)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCD_EXP_DATA_SCH_PK | SCHEDULE_DATA_ID, SCHEDULE_DATA_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_DATA_ID | NUMBER |  | 18 | Yes | System generated number to uniquely represent the schedule data record |
| TCD_EXP_DATA_ESS_PROCESS_ID | NUMBER |  | 18 |  | The process which generated the data. |
| STATUS | VARCHAR2 | 20 |  |  | Export or Collection Data Status |
| DELETE_FLAG | VARCHAR2 | 1 |  |  | Used for soft delete of the row |
| SCHEDULE_DATA_VERSION | NUMBER |  | 9 | Yes | Version of the schedule data record |
| PERSON_ID | NUMBER |  | 18 | Yes | Person id |
| SCH_REC_ID | NUMBER |  | 18 | Yes | Schedule record id |
| SCH_REC_VERSION | NUMBER |  | 9 | Yes | Schedule record version |
| SHIFT_ORIGIN | VARCHAR2 | 20 |  |  | Source of the shift. Values are like employment shedule, absences, holiday etc |
| LATEST_VERSION | VARCHAR2 | 1 |  |  | Latest version of the schedule data record |
| SHIFT_ID | NUMBER |  | 18 |  | SHIFT_ID |
| START_TIME | TIMESTAMP |  |  |  | Schedule shift start date and time |
| END_TIME | TIMESTAMP |  |  |  | Schedule shift end date and time |
| REC_TYPE | VARCHAR2 | 10 |  |  | The type of the record like created, modified, deleted |
| SETUP_PROFILE_ID | NUMBER |  | 18 |  | The setup profile id driving the export data collection. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCD_EXP_DATA_SCH_U1 | Unique | Default | SCHEDULE_DATA_ID, SCHEDULE_DATA_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
