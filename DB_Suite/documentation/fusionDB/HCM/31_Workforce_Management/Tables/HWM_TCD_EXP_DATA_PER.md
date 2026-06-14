# HWM_TCD_EXP_DATA_PER

This table contains details for Time Clock Device export data for Person Object

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataper-25476.html#hwmtcdexpdataper-25476](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataper-25476.html#hwmtcdexpdataper-25476)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCD_EXP_DATA_PER_PK | PERSON_DATA_ID, PERSON_DATA_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_DATA_ID | NUMBER |  | 18 | Yes | System generated number to uniquely represent the person data record |
| TCD_EXP_DATA_ESS_PROCESS_ID | NUMBER |  | 18 |  | The process which generated the data. |
| STATUS | VARCHAR2 | 20 |  |  | Export or Collection Data Status |
| PERSON_DATA_VERSION | NUMBER |  | 9 | Yes | Version of the person data record |
| PERSON_ID | NUMBER |  | 18 | Yes | Person id |
| PERSON_NAME_ID | NUMBER |  | 18 |  | PERSON_NAME_ID |
| NAME_EFFECTIVE_START_DATE | DATE |  |  |  | NAME_EFFECTIVE_START_DATE |
| NAME_EFFECTIVE_END_DATE | DATE |  |  |  | NAME_EFFECTIVE_END_DATE |
| DELETE_FLAG | VARCHAR2 | 1 |  |  | Used for soft delete of the row |
| FIRST_NAME | VARCHAR2 | 150 |  |  | Person first name |
| LAST_NAME | VARCHAR2 | 150 |  |  | Person last name |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | Person number |
| PERSON_BADGE_ID | VARCHAR2 | 30 |  |  | Person badge id |
| REC_TYPE | VARCHAR2 | 10 |  |  | The type of the record like created, modified, deleted |
| LATEST_VERSION | VARCHAR2 | 1 |  |  | Latest version of the person data record |
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
| HWM_TCD_EXP_DATA_PER_N1 | Non Unique | Default | PERSON_ID, LATEST_VERSION, SETUP_PROFILE_ID |
| HWM_TCD_EXP_DATA_PER_U1 | Unique | Default | PERSON_DATA_ID, PERSON_DATA_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
