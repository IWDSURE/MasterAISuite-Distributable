# HRC_SEM_EDUCATIONS

This table contains education information for the person.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemeducations-20414.html#hrcsemeducations-20414](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemeducations-20414.html#hrcsemeducations-20414)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_EDUCATIONS_PK | EDUCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| EDUCATION_ID | NUMBER |  | 18 | Yes | This is the primary key of table education. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | This is the foreign key to person table. |  |
| DEGREE_LEVEL | VARCHAR2 | 256 |  |  | This is the education level of the person. |  |
| FIELD_OF_STUDY | VARCHAR2 | 256 |  |  | This is the field study of the person. |  |
| INSTITUTION_NAME | VARCHAR2 | 240 |  |  | This column contains the institution name. |  |
| INSTITUTION_CITY | VARCHAR2 | 128 |  |  | This column contains the institution city. |  |
| INSTITUTION_STATE | VARCHAR2 | 128 |  |  | This column contains the institution state. |  |
| INSTITUTION_COUNTRY | VARCHAR2 | 128 |  |  | This column contains the instituion country. |  |
| SCHOOL | VARCHAR2 | 256 |  |  | This is the school of the person. | Obsolete |
| START_DATE | TIMESTAMP |  |  |  | This column describes the end date of the education. |  |
| END_DATE | TIMESTAMP |  |  |  | This column describes the end date of the education. |  |
| GRADUATED | VARCHAR2 | 4 |  |  | This column indicates if graduated. |  |
| CURRENT_EDUCATION | VARCHAR2 | 4 |  |  | This column indicates if education is current. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_EDUCATIONS_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID |
| HRC_SEM_EDUCATIONS_N2 | Non Unique | FUSION_TS_TX_DATA | INSTITUTION_NAME |
| HRC_SEM_EDUCATIONS_N3 | Non Unique | FUSION_TS_TX_DATA | DEGREE_LEVEL |
| HRC_SEM_EDUCATIONS_N4 | Non Unique | FUSION_TS_TX_DATA | FIELD_OF_STUDY |
| HRC_SEM_EDUCATIONS_U1 | Unique | FUSION_TS_TX_DATA | EDUCATION_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
