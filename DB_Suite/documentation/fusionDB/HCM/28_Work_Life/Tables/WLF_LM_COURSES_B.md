# WLF_LM_COURSES_B

A course is the highest level of learning that can be prescribed to a learner.It also contains the objectives and competencies a learner will achieve by completing any class that belongs underneath. It is an object in the catalog, and resid

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcoursesb-16672.html#wlflmcoursesb-16672](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcoursesb-16672.html#wlflmcoursesb-16672)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_COURSES_PK | COURSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COURSE_ID | NUMBER |  | 18 | Yes | COURSE_ID |
| EFFORT_TEXT | VARCHAR2 | 30 |  |  | EFFORT_TEXT |
| DURATION_TEXT | VARCHAR2 | 30 |  |  | DURATION_TEXT |
| TRIAL_VIDEO_CONTENT_ID | NUMBER |  | 18 | Yes | TRIAL_VIDEO_CONTENT_ID |
| COURSE_NUMBER | VARCHAR2 | 30 |  |  | COURSE_NUMBER |
| DEVELOPER_ORGANIZATION_ID | NUMBER |  | 18 | Yes | DEVELOPER_ORGANIZATION_ID |
| CONTROLLING_PERSON_ID | NUMBER |  | 18 |  | CONTROLLING_PERSON_ID |
| VENDOR_ID | NUMBER |  | 18 |  | VENDOR_ID |
| ACTUAL_COST | NUMBER |  |  |  | ACTUAL_COST |
| BUDGET_COST | NUMBER |  |  |  | BUDGET_COST |
| BUDGET_CURRENCY_CODE | VARCHAR2 | 30 |  |  | BUDGET_CURRENCY_CODE |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| DURATION | NUMBER |  | 9 |  | DURATION |
| DURATION_UNITS | VARCHAR2 | 30 |  |  | DURATION_UNITS |
| END_DATE | DATE |  |  |  | END_DATE |
| EXPENSES_ALLOWED | VARCHAR2 | 30 |  |  | EXPENSES_ALLOWED |
| INTENDED_AUDIENCE | VARCHAR2 | 4000 |  |  | INTENDED_AUDIENCE |
| LANGUAGE_ID | NUMBER |  | 18 |  | LANGUAGE_ID |
| MAXIMUM_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_ATTENDEES |
| MAXIMUM_INTERNAL_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_INTERNAL_ATTENDEES |
| MINIMUM_ATTENDEES | NUMBER |  | 9 |  | MINIMUM_ATTENDEES |
| OBJECTIVES | VARCHAR2 | 4000 |  |  | OBJECTIVES |
| PROFESSIONAL_CREDIT_TYPE | VARCHAR2 | 30 |  |  | PROFESSIONAL_CREDIT_TYPE |
| PROFESSIONAL_CREDITS | NUMBER |  |  |  | PROFESSIONAL_CREDITS |
| START_DATE | DATE |  |  |  | START_DATE |
| SUCCESS_CRITERIA | VARCHAR2 | 30 |  |  | SUCCESS_CRITERIA |
| THUMBNAIL_ID | NUMBER |  | 18 |  | THUMBNAIL_ID |
| USER_STATUS | VARCHAR2 | 30 |  |  | USER_STATUS |
| INVENTORY_ITEM_ID | NUMBER |  | 18 |  | INVENTORY_ITEM_ID |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |
| RCO_ID | NUMBER |  | 18 |  | RCO_ID |
| VERSION_CODE | VARCHAR2 | 30 |  |  | VERSION_CODE |
| DATA_SOURCE | VARCHAR2 | 30 |  |  | DATA_SOURCE |
| COMPETENCY_UPDATE_LEVEL | VARCHAR2 | 30 |  |  | COMPETENCY_UPDATE_LEVEL |
| ERES_ENABLED | VARCHAR2 | 30 |  |  | ERES_ENABLED |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CRS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| CRS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER1 |
| CRS_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER2 |
| CRS_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER3 |
| CRS_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER4 |
| CRS_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER5 |
| CRS_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER6 |
| CRS_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER7 |
| CRS_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER8 |
| CRS_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER9 |
| CRS_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER10 |
| CRS_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER11 |
| CRS_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER12 |
| CRS_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER13 |
| CRS_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER14 |
| CRS_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER15 |
| CRS_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER16 |
| CRS_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER17 |
| CRS_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER18 |
| CRS_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER19 |
| CRS_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER20 |
| CRS_ATTRIBUTE_DATE1 | DATE |  |  |  | CRS_ATTRIBUTE_DATE1 |
| CRS_ATTRIBUTE_DATE2 | DATE |  |  |  | CRS_ATTRIBUTE_DATE2 |
| CRS_ATTRIBUTE_DATE3 | DATE |  |  |  | CRS_ATTRIBUTE_DATE3 |
| CRS_ATTRIBUTE_DATE4 | DATE |  |  |  | CRS_ATTRIBUTE_DATE4 |
| CRS_ATTRIBUTE_DATE5 | DATE |  |  |  | CRS_ATTRIBUTE_DATE5 |
| CRS_ATTRIBUTE_DATE6 | DATE |  |  |  | CRS_ATTRIBUTE_DATE6 |
| CRS_ATTRIBUTE_DATE7 | DATE |  |  |  | CRS_ATTRIBUTE_DATE7 |
| CRS_ATTRIBUTE_DATE8 | DATE |  |  |  | CRS_ATTRIBUTE_DATE8 |
| CRS_ATTRIBUTE_DATE9 | DATE |  |  |  | CRS_ATTRIBUTE_DATE9 |
| CRS_ATTRIBUTE_DATE10 | DATE |  |  |  | CRS_ATTRIBUTE_DATE10 |
| CRS_ATTRIBUTE_DATE11 | DATE |  |  |  | CRS_ATTRIBUTE_DATE11 |
| CRS_ATTRIBUTE_DATE12 | DATE |  |  |  | CRS_ATTRIBUTE_DATE12 |
| CRS_ATTRIBUTE_DATE13 | DATE |  |  |  | CRS_ATTRIBUTE_DATE13 |
| CRS_ATTRIBUTE_DATE14 | DATE |  |  |  | CRS_ATTRIBUTE_DATE14 |
| CRS_ATTRIBUTE_DATE15 | DATE |  |  |  | CRS_ATTRIBUTE_DATE15 |
| CONTENT_ID | NUMBER |  | 18 |  | CONTENT_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_COURSES_N50 | Non Unique | Default | CONTROLLING_PERSON_ID |
| WLF_LM_COURSES_N51 | Non Unique | Default | VENDOR_ID |
| WLF_LM_COURSES_N56 | Non Unique | Default | VERSION_CODE |
| WLF_LM_COURSES_U1 | Unique | Default | COURSE_ID |
| WLF_LM_COURSES_U2 | Unique | Default | RCO_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
