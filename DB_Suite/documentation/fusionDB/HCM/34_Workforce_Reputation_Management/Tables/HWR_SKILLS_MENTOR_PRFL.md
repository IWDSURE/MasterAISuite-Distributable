# HWR_SKILLS_MENTOR_PRFL

This table stores skills mentorship profiles information

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillsmentorprfl-31212.html#hwrskillsmentorprfl-31212](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillsmentorprfl-31212.html#hwrskillsmentorprfl-31212)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SKILLS_MENTOR_PRFL_PK | PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_ID | NUMBER |  | 18 | Yes | This is the person ID of the profile for which mentorship profile info is stored |
| CURRENT_ROLE | VARCHAR2 | 200 |  |  | This is current skill role for the profile |
| PROFILE_INTRODUCTION | VARCHAR2 | 4000 |  |  | This is the profile introduction |
| CAREER_PATH | VARCHAR2 | 600 |  |  | This is the journey details to current skill role |
| RECOMMENDATIONS | VARCHAR2 | 600 |  |  | This is the recommendations for mentees |
| MENTORSHIP_OPT_IN | VARCHAR2 | 5 |  | Yes | This is the flag to indicated if the person has opted in for mentorship |
| SMP_ATTR_1 | VARCHAR2 | 200 |  |  | SMP_ATTR_1: This is an extra column in case if needed |
| SMP_ATTR_2 | VARCHAR2 | 200 |  |  | SMP_ATTR_2: This is an extra column in case if needed |
| PHONE_NUMBER | VARCHAR2 | 60 |  |  | This column stores the phone number of the mentorship profile. |
| YEARS_OF_EXP | VARCHAR2 | 60 |  |  | This column stores the no. of years of experience of the mentorship profile. |
| OTHER_RELEVANT_EXP | VARCHAR2 | 4000 |  |  | This column stores other relevant experience and activities of the mentorship profile. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SKILLS_MENTOR_PRFL_U1 | Unique | Default | PROFILE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
