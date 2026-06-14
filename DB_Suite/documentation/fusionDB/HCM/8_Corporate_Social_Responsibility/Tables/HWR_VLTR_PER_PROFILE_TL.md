# HWR_VLTR_PER_PROFILE_TL

The translation table for the volunteer translation table

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrperprofiletl-22467.html#hwrvltrperprofiletl-22467](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrperprofiletl-22467.html#hwrvltrperprofiletl-22467)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_PER_PROFILE_TL_PK | VOLUNTEER_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VOLUNTEER_ID | NUMBER |  | 18 | Yes | VOLUNTEER_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| FIRST_NAME | VARCHAR2 | 500 |  |  | This is the first name of the person. |
| MIDDLE_NAME | VARCHAR2 | 500 |  |  | This is the middle name of the person. |
| LAST_NAME | VARCHAR2 | 500 |  |  | This is the last name of the person. |
| ALIAS | VARCHAR2 | 500 |  |  | This is an identifier by which a person is known as. |
| GENDER_CODE | VARCHAR2 | 80 |  | Yes | A string code for gender: MALE, FEMALE or NA (not available). |
| EMAIL | VARCHAR2 | 800 |  |  | The email address of the person. |
| CURRENT_STATUS | VARCHAR2 | 1000 |  |  | The current status of the profile. |
| INTERESTS | VARCHAR2 | 4000 |  |  | The list of interests for the profile. |
| LANGUAGES | VARCHAR2 | 4000 |  |  | The list of languages for the profile. |
| SKILLS | VARCHAR2 | 4000 |  |  | The list of skills for the profile. |
| SPECIALTIES | VARCHAR2 | 4000 |  |  | The list of specialties for the profile. |
| TITLE | VARCHAR2 | 100 |  |  | TITLE |
| PROJECT_LEAD_INTEREST | VARCHAR2 | 4 |  |  | PROJECT_LEAD_INTEREST |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_PER_PROFILE_TL_U1 | Unique | FUSION_TS_TX_IDX | VOLUNTEER_ID, LANGUAGE |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
