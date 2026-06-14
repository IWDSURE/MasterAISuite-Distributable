# HRD_CAREER_AMB_ELIG_PROCESS_TL

This table will store translatable Ui field values for creating Career Ambassadors sign-up eligibility process like process name and description

## Details

**Schema:** FUSION

**Object owner:** HRD

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdcareerambeligprocesstl-29166.html#hrdcareerambeligprocesstl-29166](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdcareerambeligprocesstl-29166.html#hrdcareerambeligprocesstl-29166)

## Primary Key

| Name | Columns |
|------|----------|
| HRD_CAREER_AMB_ELIG_PR_TL_PK | CAREER_AMB_ELIG_PROCESS_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAREER_AMB_ELIG_PROCESS_ID | NUMBER |  | 18 | Yes | Foreign key to Career Ambassadors sign up eligibility process base table |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  | Yes | Translated Career Ambassadors sign up eligibility process name |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Translated Description |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRD_CAREER_AMB_ELIG_PR_TL_N1 | Non Unique | Default | NAME |
| HRD_CAREER_AMB_ELIG_PR_TL_PK | Unique | Default | CAREER_AMB_ELIG_PROCESS_ID, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../5_Career_Development_Tables_Index.md)
