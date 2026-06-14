# HWR_VLTR_PROJECT_B

This table stores base  project information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrprojectb-28113.html#hwrvltrprojectb-28113](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrprojectb-28113.html#hwrvltrprojectb-28113)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_PROJECT_B_PK | PROJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of conversation. |
| ABSENCE_TYPE_ID | NUMBER |  | 18 |  | ABSENCE_TYPE_ID |
| ENROLLMENT_CHOICE | NUMBER |  | 1 |  | ENROLLMENT_CHOICE |
| LOGO_FILE_ID | NUMBER |  | 18 |  | LOGO_FILE_ID |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| PROJECT_ADDRESS_ID | NUMBER |  | 18 |  | PROJECT_ADDRESS_ID |
| CONTACT_LOCATION_ID | NUMBER |  | 18 |  | CONTACT_LOCATION_ID |
| IS_SAME_SCH_SELECTED_DAYS | NUMBER |  | 1 |  | IS_SAME_SCH_ALL_DAY |
| START_DATE | DATE |  |  |  | START_DATE |
| START_TIME | NUMBER |  | 18 |  | START_TIME |
| END_TIME | NUMBER |  | 18 |  | END_TIME |
| END_DATE | DATE |  |  |  | END_DATE |
| RECURRENCE_TYPE | VARCHAR2 | 20 |  |  | RECURRENCE_TYPE |
| RECURRENCE_COUNT | NUMBER |  | 2 |  | RECURRENCE_COUNT |
| RECURRENCE_GAP | NUMBER |  | 2 |  | RECURRENCE_GAP |
| DAYS_OF_WEEK | VARCHAR2 | 100 |  |  | SELECTED_DAYS |
| MON_START_TIME | NUMBER |  | 18 |  | MON_START_TIME |
| MON_END_TIME | NUMBER |  | 18 |  | MON_END_TIME |
| TUE_START_TIME | NUMBER |  | 18 |  | TUE_START_TIME |
| TUE_END_TIME | NUMBER |  | 18 |  | TUE_END_TIME |
| WED_START_TIME | NUMBER |  | 18 |  | WED_START_TIME |
| WED_END_TIME | NUMBER |  | 18 |  | WED_END_TIME |
| THU_START_TIME | NUMBER |  | 18 |  | THU_START_TIME |
| THU_END_TIME | NUMBER |  | 18 |  | THU_END_TIME |
| FRI_START_TIME | NUMBER |  | 18 |  | FRI_START_TIME |
| FRI_END_TIME | NUMBER |  | 18 |  | FRI_END_TIME |
| SAT_START_TIME | NUMBER |  | 18 |  | SAT_START_TIME |
| SAT_END_TIME | NUMBER |  | 18 |  | SAT_END_TIME |
| SUN_START_TIME | NUMBER |  | 18 |  | SUN_START_TIME |
| SUN_END_TIME | NUMBER |  | 18 |  | SUN_END_TIME |
| AREAS_OF_INTEREST | VARCHAR2 | 4000 |  |  | AREAS_OF_INTEREST |
| REGISTRATION_DEADLINE | CLOB |  |  |  | REGISTRATION_DEADLINE |
| REG_DEADLINE | DATE |  |  |  | REG_DEADLINE |
| PROJECT_INITIATIVE | VARCHAR2 | 100 |  |  | PROJECT_INITIATIVE |
| VOLUNTEER_JOB | VARCHAR2 | 4000 |  |  | VOLUNTEER_JOB |
| SHIFTS | VARCHAR2 | 4000 |  |  | SHIFTS |
| MINIMUM_PARTICIPANT_NUMBER | NUMBER |  | 18 |  | MINIMUM_PARTICIPANT_NUMBER |
| MAXIMUM_PARTICIPANT_NUMBER | NUMBER |  | 18 |  | MAXIMUM_PARTICIPANT_NUMBER |
| MAXIMUM_GUEST_NUMBER | NUMBER |  | 18 |  | MAXIMUM_GUEST_NUMBER |
| MINIMUM_AGE_REQUIREMENT | NUMBER |  | 18 |  | MINIMUM_AGE_REQUIREMENT |
| PROJECT_LEAD_ID | NUMBER |  | 18 |  | PROJECT_LEAD_ID |
| PROJECT_LEAD_PERSON_ID | NUMBER |  | 18 |  | PROJECT_LEAD_PERSON_ID |
| INVITE_PROJECT_LEADERS | VARCHAR2 | 4000 |  |  | INVITE_PROJECT_LEADERS |
| STATE | VARCHAR2 | 100 |  |  | STATUS |
| STATUS | VARCHAR2 | 100 |  |  | STATUS |
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | ORGANIZATION_ID |
| CONTACT_PHONE | VARCHAR2 | 100 |  |  | CONTACT_PHONE |
| CONTACT_FAX | VARCHAR2 | 100 |  |  | CONTACT_FAX |
| CONTACT_EMAIL | VARCHAR2 | 100 |  |  | CONTACT_EMAIL |
| WEBSITE | VARCHAR2 | 100 |  |  | WEBSITE |
| SUBMITTED_BY | VARCHAR2 | 64 |  |  | SUBMITTED_BY |
| PROJECT_START_DATE | TIMESTAMP |  |  |  | PROJECT_START_DATE |
| PROJECT_END_DATE | TIMESTAMP |  |  |  | PROJECT_END_DATE |
| LONGITUDE | NUMBER |  |  |  | Longitude |
| LATITUDE | NUMBER |  |  |  | LATITUDE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATOR_PERSON_ID | NUMBER |  | 18 |  | CREATOR_PERSON_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COUNTRY_CODE_NUMBER | VARCHAR2 | 30 |  |  | COUNTRY_CODE_NUMBER |
| START_DATE_LOC_ZONE | TIMESTAMP |  |  |  | START_DATE_LOC_ZONE |
| END_DATE_LOC_ZONE | TIMESTAMP |  |  |  | END_DATE_LOC_ZONE |
| CT_ACTIVITY_ID | VARCHAR2 | 20 |  |  | CT_ACTIVITY_ID |
| PROJECT_TYPE | NUMBER |  | 1 |  | PROJECT_TYPE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_PROJECT_B_U1 | Unique | FUSION_TS_TX_IDX | PROJECT_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
