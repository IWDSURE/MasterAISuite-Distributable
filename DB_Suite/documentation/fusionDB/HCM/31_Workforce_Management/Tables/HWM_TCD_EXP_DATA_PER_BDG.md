# HWM_TCD_EXP_DATA_PER_BDG

This table contains details for Time Clock Device export data for Person Badge Object

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataperbdg-21251.html#hwmtcdexpdataperbdg-21251](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataperbdg-21251.html#hwmtcdexpdataperbdg-21251)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCD_EXP_DATA_PER_BDG_PK | PER_BADGE_DATA_ID, PER_BADGE_DATA_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_BADGE_ID | VARCHAR2 | 256 |  |  | Person Badge  Id |
| TCD_EXP_DATA_ESS_PROCESS_ID | NUMBER |  | 18 |  | The process which generated the data. |
| STATUS | VARCHAR2 | 20 |  |  | Export or Collection Data Status |
| PER_BADGE_DATA_ID | NUMBER |  | 18 | Yes | Person Badge Data Id |
| PER_BADGE_DATA_VERSION | NUMBER |  | 9 | Yes | Person Badge Data Version |
| LATEST_VERSION | VARCHAR2 | 1 |  |  | LATEST_VERSION |
| REC_TYPE | VARCHAR2 | 10 |  |  | REC_TYPE |
| DELETE_FLAG | VARCHAR2 | 1 |  |  | Indicates soft delete of the row |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| DATE_FROM | TIMESTAMP |  |  |  | DATE_FROM |
| DATE_TO | TIMESTAMP |  |  |  | DATE_TO |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Person assignment Id |
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
| HWM_TCD_EXP_DATA_PER_BDG_N1 | Non Unique | Default | PERSON_BADGE_ID, PERSON_ID, LATEST_VERSION |
| HWM_TCD_EXP_DATA_PER_BDG_U2 | Unique | Default | PER_BADGE_DATA_ID, PER_BADGE_DATA_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
