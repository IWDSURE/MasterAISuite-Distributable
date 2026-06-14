# HWR_PER_PROFILE_B

The person profile table is used to store a profile of a social media account of a person.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprofileb-11328.html#hwrperprofileb-11328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprofileb-11328.html#hwrperprofileb-11328)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_PROFILE_B_PK | SOURCE_ID, PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the person profile tables. It is used by the source to identify the profile. |  |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id for the social data source. | Active |
| PROFILE_REPO | NUMBER |  | 18 |  | The unique Id for writing to repo. |  |
| FIRST_NAME | VARCHAR2 | 500 |  |  | This is the first name of the person. |  |
| MIDDLE_NAME | VARCHAR2 | 500 |  |  | This is the middle name of the person. |  |
| LAST_NAME | VARCHAR2 | 500 |  |  | This is the last name of the person. |  |
| ALIAS | VARCHAR2 | 500 |  |  | This is an identifier by which a person is known as. |  |
| GENDER_CODE | VARCHAR2 | 80 |  | Yes | A string code for gender: MALE, FEMALE or NA (not available). |  |
| EMAIL | VARCHAR2 | 800 |  |  | The email address of the person. |  |
| YEARS_OF_EXP | NUMBER |  |  |  | This is the number of years of work experience of the person. | Obsolete |
| INFLUENCE_SCORE | NUMBER |  |  |  | This is a value which indicates a person's social influence. | Obsolete |
| IS_SELECTED_FLAG | VARCHAR2 | 4 |  | Yes | A flag to indicate the selected person: Y for yes; N for no. | Obsolete |
| IS_ACTIVE_FLAG | VARCHAR2 | 4 |  |  | A flag to indicate whether the profile is active or not. Y for yes; N for no. |  |
| SOCIAL_COMPLIANCE_CODE | VARCHAR2 | 80 |  |  | The code for social compliance. | Obsolete |
| RESUME_URL | VARCHAR2 | 4000 |  |  | The URL to the person's resume. | Active |
| IMAGE_URL | VARCHAR2 | 4000 |  |  | The URL to the person's photo image. | Active |
| LIKED_BY | VARCHAR2 | 4000 |  |  | This is a list of other persons that have made a positive acknowledgment about this person. | Obsolete |
| ABOUT_ME | VARCHAR2 | 4000 |  |  | The profile summary written by the person. |  |
| ASSOCIATIONS | VARCHAR2 | 4000 |  |  | The list of associations for the profile. |  |
| CURRENT_STATUS | VARCHAR2 | 1000 |  |  | The current status of the profile. |  |
| DNA_CHECKSUM | VARCHAR2 | 100 |  |  | The DNA checksum of the profile. |  |
| GEEKCODE | VARCHAR2 | 100 |  |  | The geek code information of the profile. |  |
| HEADLINE | VARCHAR2 | 1000 |  |  | The headline information of the profile. |  |
| HONORS | VARCHAR2 | 4000 |  |  | The list of honors for the profile. |  |
| INDUSTRY | VARCHAR2 | 4000 |  |  | The industry information of the profile. |  |
| INTERESTS | VARCHAR2 | 4000 |  |  | The list of interests for the profile. |  |
| LANGUAGES | VARCHAR2 | 4000 |  |  | The list of languages for the profile. |  |
| MYERS_BRIGG | VARCHAR2 | 100 |  |  | The Myers-Brigg value for the profile. |  |
| NICKNAME | VARCHAR2 | 500 |  |  | The optional nickname of the person. |  |
| PERSONAL_URL | VARCHAR2 | 4000 |  |  | The personal URL of the profile |  |
| PLAN | VARCHAR2 | 4000 |  |  | The plan information of the profile. |  |
| SKILLS | VARCHAR2 | 4000 |  |  | The list of skills for the profile. |  |
| SPECIALTIES | VARCHAR2 | 4000 |  |  | The list of specialties for the profile. |  |
| TITLE | VARCHAR2 | 100 |  |  | The title used with the name of the person. |  |
| PROFILE_TYPE | VARCHAR2 | 100 |  |  | The profile type of the profile. |  |
| URL | VARCHAR2 | 4000 |  |  | The URL for accessing this profile. |  |
| USER_ID | NUMBER |  | 18 |  | This is the numeric user ID identifying the user. |  |
| USERNAME | VARCHAR2 | 100 |  |  | This is the login name of the user. |  |
| USER_GUID | VARCHAR2 | 64 |  |  | This is the GUID identifying the user. |  |
| USER_DISTINGUISHED_NAME | VARCHAR2 | 4000 |  |  | This is the distinguished name of the user. |  |
| MULTITENANCY_USERNAME | VARCHAR2 | 255 |  |  | This is the multitenancy username of the user. |  |
| CAREER_STATEMENT | VARCHAR2 | 4000 |  |  | This is the career statement of the user. |  |
| JOB_NAME | VARCHAR2 | 500 |  |  | This is the job name of the user profile. |  |
| COMPANY_NAME | VARCHAR2 | 500 |  |  | This is the company name of the user profile. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_PER_PROFILE_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, PRFL_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
