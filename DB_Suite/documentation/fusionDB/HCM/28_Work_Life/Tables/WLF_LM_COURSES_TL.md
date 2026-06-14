# WLF_LM_COURSES_TL

This table is used for Activity Version language translations.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcoursestl-8103.html#wlflmcoursestl-8103](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcoursestl-8103.html#wlflmcoursestl-8103)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_COURSES_TL_PK | COURSE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COURSE_ID | NUMBER |  | 18 | Yes | COURSE_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 80 |  | Yes | VERSION_NAME |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | DESCRIPTION |
| INTENDED_AUDIENCE | VARCHAR2 | 4000 |  |  | INTENDED_AUDIENCE |
| OBJECTIVES | VARCHAR2 | 4000 |  |  | OBJECTIVES |
| KEYWORDS | VARCHAR2 | 2000 |  |  | KEYWORDS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_COURSES_TL_N1 | Non Unique | Default | LANGUAGE, NAME |
| WLF_LM_COURSES_TL_N2 | Non Unique | Default | UPPER("KEYWORDS") |
| WLF_LM_COURSES_TL_N3 | Non Unique | Default | UPPER("NAME") |
| WLF_LM_COURSES_TL_U1 | Unique | Default | COURSE_ID, LANGUAGE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
