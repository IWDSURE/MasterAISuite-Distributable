# WLF_LM_LEARNING_PATHS_B

Table to store learning path objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmlearningpathsb-25555.html#wlflmlearningpathsb-25555](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmlearningpathsb-25555.html#wlflmlearningpathsb-25555)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_LEARNING_PATHS_B_PK | LEARNING_PATH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARNING_PATH_ID | NUMBER |  | 18 | Yes | LEARNING_PATH_ID |
| TRIAL_VIDEO_CONTENT_ID | NUMBER |  | 18 |  | TRIAL_VIDEO_CONTENT_ID |
| LEARNING_PATH_NUMBER | VARCHAR2 | 30 |  |  | LEARNING_PATH_NUMBER |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| DURATION_UNITS | VARCHAR2 | 30 |  |  | DURATION_UNITS |
| DUE_IN_DAYS | NUMBER |  |  |  | DUE_IN_DAYS |
| DUEDATE_IN_NUM_YRS | NUMBER |  |  |  | DUEDATE_IN_NUM_YRS |
| DUE_DATE | DATE |  |  |  | DUE_DATE |
| CERTIFICATION_FLAG | VARCHAR2 | 30 |  |  | CERTIFICATION_FLAG |
| VALIDITY_PERIOD | NUMBER |  |  |  | VALIDITY_PERIOD |
| RENEWABLE_FLAG | VARCHAR2 | 30 |  |  | RENEWABLE_FLAG |
| RENEWAL_PERIOD | NUMBER |  |  |  | RENEWAL_PERIOD |
| NOTIFY_DAYS_BEFORE_TARGET | NUMBER |  | 10 |  | NOTIFY_DAYS_BEFORE_TARGET |
| PATH_SOURCE_CODE | VARCHAR2 | 30 |  |  | PATH_SOURCE_CODE |
| SOURCE_FUNCTION_CODE | VARCHAR2 | 30 |  |  | SOURCE_FUNCTION_CODE |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| PUBLIC_FLAG | VARCHAR2 | 30 |  |  | PUBLIC_FLAG |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| THUMBNAIL_ID | NUMBER |  | 18 |  | THUMBNAIL_ID |
| CONTACT_ID | NUMBER |  | 18 |  | CONTACT_ID |
| DISPLAY_TO_LEARNER_FLAG | VARCHAR2 | 30 |  |  | DISPLAY_TO_LEARNER_FLAG |
| COMPETENCY_UPDATE_LEVEL | VARCHAR2 | 30 |  |  | COMPETENCY_UPDATE_LEVEL |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| INITIAL_COMPLETION_DATE | DATE |  |  |  | INITIAL_COMPLETION_DATE |
| INITIAL_COMPLETION_DURATION | NUMBER |  |  |  | INITIAL_COMPLETION_DURATION |
| INITIAL_COMPL_DURATION_UNITS | VARCHAR2 | 30 |  |  | INITIAL_COMPL_DURATION_UNITS |
| RENEWAL_DURATION | NUMBER |  |  |  | RENEWAL_DURATION |
| RENEWAL_DURATION_UNITS | VARCHAR2 | 30 |  |  | RENEWAL_DURATION_UNITS |
| NOTIFY_DAYS_BEFORE_EXPIRE | NUMBER |  |  |  | NOTIFY_DAYS_BEFORE_EXPIRE |
| VALIDITY_DURATION | NUMBER |  |  |  | VALIDITY_DURATION |
| VALIDITY_DURATION_UNITS | VARCHAR2 | 30 |  |  | VALIDITY_DURATION_UNITS |
| VALIDITY_START_TYPE | VARCHAR2 | 30 |  |  | VALIDITY_START_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LPA_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| LPA_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LPA_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| LPA_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flex field. |
| CONTENT_ID | NUMBER |  | 18 |  | CONTENT_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_LEARNING_PATHS_B_N1 | Non Unique | Default | CONTACT_ID |
| WLF_LM_LEARNING_PATHS_B_PK | Unique | Default | LEARNING_PATH_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
