# HWR_VLTR_PROJECT_TL

This table stores project translation information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrprojecttl-5471.html#hwrvltrprojecttl-5471](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrprojecttl-5471.html#hwrvltrprojecttl-5471)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_PROJECT_TL_PK | PROJECT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |
| PROJECT_NAME | VARCHAR2 | 100 |  |  | PROJECT_NAME |
| PROJECT_DESCRIPTION | VARCHAR2 | 4000 |  |  | PROJECT_DESCRIPTION |
| FOCUS_AREA | VARCHAR2 | 100 |  |  | FOCUS_AREA |
| PARTICIPANT_SKILL_REQUIREMENTS | VARCHAR2 | 4000 |  |  | PARTICIPANT_SKILL_REQUIREMENTS |
| ITEMS_TO_BE_BROUGHT | VARCHAR2 | 4000 |  |  | ITEMS_TO_BE_BROUGHT |
| ITEMS_TO_BE_SUPPLIED | VARCHAR2 | 4000 |  |  | ITEMS_TO_BE_SUPPLIED |
| PARTICIPANT_BENEFITS | VARCHAR2 | 4000 |  |  | PARTICIPANT_BENEFITS |
| OTHER_PARTICIPANT_BENEFITS | VARCHAR2 | 4000 |  |  | OTHER_PARTICIPANT_BENEFITS |
| CONTACT_FIRST_NAME | VARCHAR2 | 100 |  |  | CONTACT_FIRST_NAME |
| CONTACT_LAST_NAME | VARCHAR2 | 100 |  |  | CONTACT_LAST_NAME |
| CONTACT_ADDRESS_TYPE | VARCHAR2 | 100 |  |  | CONTACT_ADDRESS_TYPE |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CONTACT_TITLE | VARCHAR2 | 100 |  |  | CONTACT_TITLE |
| ADDITIONAL_PROJECT_DETAILS | VARCHAR2 | 4000 |  |  | ADDITIONAL_PROJECT_DETAILS |
| DIRECTIONS_TO_WORK_SITE | VARCHAR2 | 4000 |  |  | DIRECTIONS_TO_WORK_SITE |
| COUNTRY | VARCHAR2 | 60 |  |  | COUNTRY |
| CITY | VARCHAR2 | 50 |  |  | CITY |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_PROJECT_TL_U2 | Unique | FUSION_TS_TX_IDX | PROJECT_ID, LANGUAGE |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
