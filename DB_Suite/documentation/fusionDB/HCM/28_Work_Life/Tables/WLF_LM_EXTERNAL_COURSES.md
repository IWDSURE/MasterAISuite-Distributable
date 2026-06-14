# WLF_LM_EXTERNAL_COURSES

Table to store external course content

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmexternalcourses-16845.html#wlflmexternalcourses-16845](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmexternalcourses-16845.html#wlflmexternalcourses-16845)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_EXTERNAL_COURSES_PK | EXTERNAL_COURSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTERNAL_COURSE_ID | NUMBER |  |  | Yes | Primary key |
| CONTENT_ID | NUMBER |  |  |  | Refer key |
| COURSE_ID | NUMBER |  |  |  | reference key |
| HASH_CODE | NUMBER |  |  | Yes | version change key |
| ABOUT_THE_COURSE | VARCHAR2 | 4000 |  |  | About the course |
| FAQ | VARCHAR2 | 4000 |  |  | faq about the course |
| COURSE_SYLLABUS | VARCHAR2 | 4000 |  |  | course syllabus |
| COURSE_FORMAT | VARCHAR2 | 4000 |  |  | course format |
| ESTIMATED_CLASS_WORKLOAD | VARCHAR2 | 4000 |  |  | estimated class workload for the course |
| ABOUT_THE_INSTRUCTOR | VARCHAR2 | 4000 |  |  | about the instructor of the course |
| RECOMMENDED_BACKGROUND | VARCHAR2 | 4000 |  |  | recommended background |
| LARGE_ICON | VARCHAR2 | 1000 |  |  | large icon |
| PHOTO_URL | VARCHAR2 | 1000 |  |  | photo url |
| THUMBNAIL_URL | VARCHAR2 | 1000 |  |  | thumbnail url |
| PREVIEW_URL | VARCHAR2 | 1000 |  |  | preview  url |
| VIDEO_PREVIEW_URL | VARCHAR2 | 1000 |  |  | video preview url |
| SMALL_ICON_URL | VARCHAR2 | 1000 |  |  | small icon url |
| SMALL_ICON_HOVER_URL | VARCHAR2 | 1000 |  |  | small icon hover url |
| UNIVERSITY_LOGO | VARCHAR2 | 1000 |  |  | university logo |
| UNIVERSITY_LOGO_ST | VARCHAR2 | 1000 |  |  | university logo st |
| AVAILABLE_LANGUAGES | VARCHAR2 | 1000 |  |  | available languages |
| HOME_PAGE | VARCHAR2 | 1000 |  |  | home page |
| BANNER_URL | VARCHAR2 | 1000 |  |  | banner url |
| PROJECT_NAME | VARCHAR2 | 1000 |  |  | project name |
| INSTRUCTOR | VARCHAR2 | 1000 |  |  | instructor |
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
| WLF_LM_EXTERNAL_COURSES_U1 | Unique | Default | EXTERNAL_COURSE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
