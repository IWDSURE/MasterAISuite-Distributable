# HRC_SEM_WORK_EXPERIENCES

This table contains information about work experience of a person.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemworkexperiences-14543.html#hrcsemworkexperiences-14543](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemworkexperiences-14543.html#hrcsemworkexperiences-14543)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_WORK_EXPERIENCES_PK | WORK_EXPERIENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_EXPERIENCE_ID | NUMBER |  | 18 | Yes | This is the primary key of the table. |
| PERSON_ID | NUMBER |  | 18 | Yes | This is the foreign key to person table. |
| JOB_TITLE | VARCHAR2 | 512 |  |  | This is the job function description of the person. |
| EMPLOYER_NAME | VARCHAR2 | 1024 |  |  | This is the employer name of the person. |
| DEPARTMENT | VARCHAR2 | 512 |  |  | This is the department of the job. |
| START_DATE | TIMESTAMP |  |  |  | This column describes the start date of the work experience. |
| END_DATE | TIMESTAMP |  |  |  | This column describes the end date of the work experience. |
| YEARS_EXPERIENCE | NUMBER |  |  |  | This indicates the cumulative years of experience. |
| CURRENT_POSITION | VARCHAR2 | 4 |  |  | This column indicates if still at the current job. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_SEM_WORK_EXPERIENCES_U1 | Unique | FUSION_TS_TX_DATA | WORK_EXPERIENCE_ID |  |
| HRC_SEM_WORK_EXPERIENCE_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID |  |
| HRC_SEM_WORK_EXPERIENCE_N2 | Non Unique | FUSION_TS_TX_DATA | JOB_TITLE |  |
| HRC_SEM_WORK_EXPERIENCE_N3 | Non Unique | FUSION_TS_TX_DATA | EMPLOYER_NAME |  |
| HRC_SEM_WORK_EXPERIENCE_N4 | Non Unique | FUSION_TS_TX_DATA | YEARS_EXPERIENCE |  |
| HRC_SEM_WORK_EXPERIENCE_N5 | Non Unique | FUSION_TS_TX_DATA | DEPARTMENT | Obsolete |
| HRC_SEM_WORK_EXPERIENCE_N6 | Non Unique | FUSION_TS_TX_DATA | START_DATE | Obsolete |
| HRC_SEM_WORK_EXPERIENCE_N7 | Non Unique | FUSION_TS_TX_DATA | END_DATE | Obsolete |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
