# HWR_MENTOR_PRFL_LANGUAGE

This table stores mentor language and proficiency information.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmentorprfllanguage-13657.html#hwrmentorprfllanguage-13657](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmentorprfllanguage-13657.html#hwrmentorprfllanguage-13657)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_MENTOR_PRFL_LANGUAGE_PK | PERSON_ID, LANGUAGE_CODE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | This is the person ID of the profile for language info is stored |
| LANGUAGE_CODE | VARCHAR2 | 64 |  | Yes | This columns stores language code. |
| READING_PROFICIENCY | VARCHAR2 | 64 |  |  | This column stores the reading proficiency. |
| WRITING_PROFICIENCY | VARCHAR2 | 64 |  |  | This column stores the writing proficiency. |
| SPEAKING_PROFICIENCY | VARCHAR2 | 64 |  |  | This column stores the speaking proficiency. |
| AOE_ATTR_1 | VARCHAR2 | 200 |  |  | MPL_ATTR_1: This is an extra column in case if needed |
| MPL_ATTR_2 | VARCHAR2 | 200 |  |  | MPL_ATTR_2: This is an extra column in case if needed |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_MENTOR_PRFL_LANGUAGE_U1 | Unique | Default | PERSON_ID, LANGUAGE_CODE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
