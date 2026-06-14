# HWR_WLNS_USER_

The wellness user table stores wellness user data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsuser-23306.html#hwrwlnsuser-23306](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsuser-23306.html#hwrwlnsuser-23306)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_USER_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| USER_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the wellness user table. |  |
| LAST_UPDATE_DATE_ERGONOMIC | TIMESTAMP |  |  |  | Corresponds to the ERGONOMIC_STATUS field value change |  |
| ERGONOMIC_STATUS | VARCHAR2 | 100 |  |  | This column contains the User's Ergonomic Status. |  |
| LAST_UPDATE_DATE_GUIDED | TIMESTAMP |  |  |  | Corresponds to the WELLBEING_LEVEL field value change |  |
| START_DATE | DATE |  |  |  | This is the start date of the wellness user. |  |
| BMI | NUMBER |  | 18 |  | This is the body mass index of the wellness user. |  |
| AGE | NUMBER |  | 18 |  | This is the age of the wellness user. | Obsolete |
| STATE | VARCHAR2 | 100 |  |  | This is the state in which the wellness user is located. | Obsolete |
| SALARY | NUMBER |  | 18 |  | This is the salary of the wellness user. | Obsolete |
| JOB_TITLE | VARCHAR2 | 500 |  |  | This is the job title of the wellness user. | Obsolete |
| ORGANIZATION | VARCHAR2 | 500 |  |  | This is the organization of the wellness user. | Obsolete |
| PROJECT_TYPE | VARCHAR2 | 500 |  |  | This is the project type of the wellness user. | Obsolete |
| GENDER | VARCHAR2 | 20 |  |  | This is the gender of the wellness user. | Obsolete |
| AVERAGE_STEPS | NUMBER |  | 18 |  | This is the average of steps per day of the wellness user. | Obsolete |
| PERCENT_SEDENTARY | NUMBER |  | 18 |  | This is the percent of sedentary days of the wellness user. | Obsolete |
| AVERAGE_SLEEP_TIME | NUMBER |  | 18 |  | This is the average sleep time of the wellness user. | Obsolete |
| AVERAGE_TIMES_AWAKE | NUMBER |  | 18 |  | This is the average number of times awakened from sleep of the wellness user. | Obsolete |
| AVERAGE_VERY_ACTIVE | NUMBER |  | 18 |  | This is the average very active time of the wellness user. | Obsolete |
| SOURCE_ID | NUMBER |  | 18 |  | This is the source id of  the wellness user table. | Obsolete |
| TRACKING_SERVICE_SOURCE_ID | NUMBER |  | 18 |  | This column contains the source id of user's tracking sercvice. |  |
| TRACKING_SOURCE_ADDED_DATE | TIMESTAMP |  |  |  | This column contains added date for Tracking source |  |
| HEIGHT | NUMBER |  |  |  | This column stores the height of the wellness user. |  |
| HEIGHT_UNIT | VARCHAR2 | 256 |  |  | This column stores the unit for user height information. |  |
| WEIGHT | NUMBER |  |  |  | This column stores the weight of the wellness user. |  |
| WEIGHT_UNIT | VARCHAR2 | 256 |  |  | This column stores the unit for user weight information. |  |
| WELLBEING_LEVEL | VARCHAR2 | 256 |  |  | This column stores the wellbeing status of the wellness user. |  |
| UNIT_SYSTEM | VARCHAR2 | 40 |  |  | This column stores the unit system selected by the user (Metric/Imperial) |  |
| ASSESSMENT_TYPE | VARCHAR2 | 100 |  |  | This column stores the last assessment type for well being . |  |
| WELLBEING_CALC_RULE_CODE | VARCHAR2 | 30 |  |  | This column stores the wellbeing questionnaire calculation rule for calculating overall score. |  |
| ERGONOMIC_CALC_RULE_CODE | VARCHAR2 | 30 |  |  | This column stores the ergonomic questionnaire calculation rule for calculating overall score. |  |
| WELLBEING_SCORE | NUMBER |  | 20 |  | This column stores the wellbeing assessment score of the wellness user. |  |
| ERGONOMIC_SCORE | NUMBER |  | 20 |  | This column contains the User's Ergonomic assessment score |  |
| WELLBEING_TOTAL_SCORE | NUMBER |  | 20 |  | This column stores the wellbeing assesment total score of the wellness user. |  |
| ERGONOMIC_TOTAL_SCORE | NUMBER |  | 20 |  | This column stores the ergonomic assessment total score. |  |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_USERN1_ | Non Unique | Default | USER_ID, LAST_UPDATE_DATE |
| HWR_WLNS_USER_U1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, USER_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
