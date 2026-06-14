# IRC_TN_JOBS_B

Table for storing Jobs pulled from multiple customers.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobsb-28381.html#irctnjobsb-28381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobsb-28381.html#irctnjobsb-28381)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOBS_B_PK | TN_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | To store the subscriber id. Foreign Key to IRC_TN_SUBSCRIBERS. |
| STATUS | VARCHAR2 | 30 |  | Yes | Stores the  Posting Status on TN (ORA_TN_POSTED/ORA_TN_UNPOSTED) |
| FA_RECRUITING_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the type of Recruiting as a lookup code. The corresponding lookup type is ORA_IRC_RECRUITING_TYPE. |
| FA_REQUISITION_ID | NUMBER |  | 18 | Yes | Stores the REQUISITION_ID from IRC_REQUISITIONS_B table |
| FA_REQUISITION_NUMBER | VARCHAR2 | 240 |  | Yes | Stores the REQUISITION_NUMBER from IRC_REQUISITIONS_B table |
| FA_REQ_LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Stores the REQ_LAST_MODIFIED_DATE from IRC_REQUISITIONS_B table |
| FA_JOB_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the job type code from IRC_REQUISITIONS_B.JOB_TYPE_CODE. The corresponding lookup type is ORA_IRC_JOB_TYPE. |
| FA_JOB_SHIFT_CODE | VARCHAR2 | 30 |  |  | Stores the job shift code from IRC_REQUISITIONS_B.JOB_SHIFT_CODE. The corresponding lookup type is ORA_IRC_JOB_SHIFT |
| FA_EXT_CONTACT_NAME | VARCHAR2 | 240 |  |  | Stores the External Contact name from IRC_REQUISITIONS_B table. |
| FA_EXT_CONTACT_EMAIL | VARCHAR2 | 240 |  |  | Stores the External Contact email from IRC_REQUISITIONS_B table. |
| JOB_NUMBER | NUMBER |  | 18 |  | Stores the Sequence Number for the JOB from IRC_TN_JOB_NUMBER_S. |
| WORK_START_DATE | TIMESTAMP |  |  |  | Stores Expected Start Date from IRC_REQUISITIONS_B table. |
| WORK_END_DATE | TIMESTAMP |  |  |  | Stores Expected End Date from IRC_REQUISITIONS_B table. |
| MIN_SALARY | NUMBER |  |  |  | Stores the minimum salary for this Requisition from IRC_REQUISITIONS_B.MIN_SALARY table. |
| MAX_SALARY | NUMBER |  |  |  | Stores the maximum salary for this Requisition from IRC_REQUISITIONS_B.MAX_SALARY table |
| SALARY_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Stores the salary currency code for this Requisition from  IRC_REQUISITIONS_B.SALARY_CURRENCY_CODE table. |
| STANDARD_WORKING_HOURS | NUMBER |  | 22 |  | Stores the Number of standard working hours from HR_ALL_POSITIONS_F.STANDARD_WORKING_HOURS and IRC_REQUISITIONS_B.POSITION_ID table. |
| NAT_TRAVEL_REQUIRED_FLAG | VARCHAR2 | 30 |  |  | Stores domestic travel required flag from  HRT_WORK_PREFERENCE_ITEMS_V.NAT_TRAVEL_REQUIRED_FLAG and IRC_REQUISITIONS_B.PROFILE_ID table. |
| INTL_TRAVEL_REQUIRED_FLAG | VARCHAR2 | 30 |  |  | Stores International travel required flag from  HRT_WORK_PREFERENCE_ITEMS_V.INTL_TRAVEL_REQUIRED_FLAG and IRC_REQUISITIONS_B.PROFILE_ID table. |
| HOT_JOB_FLAG | VARCHAR2 | 1 |  | Yes | Stores whether this Requisition should be considerate as a Hot Job or not from IRC_REQUISITIONS_B.HOT_JOB_FLAG table. |
| NUMBER_TO_HIRE | NUMBER |  | 9 |  | Stores the number of people to hire for this job. |
| UNLIMITED_HIRE_FLAG | VARCHAR2 | 1 |  |  | Stores whether this job can hire unlimited number of people. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of the Object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOBS_B_FK1 | Non Unique | Default | SUBSCRIBER_ID |
| IRC_TN_JOBS_B_PK | Unique | Default | TN_JOB_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
