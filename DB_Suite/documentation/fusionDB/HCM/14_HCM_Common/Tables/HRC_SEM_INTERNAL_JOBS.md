# HRC_SEM_INTERNAL_JOBS

This table contains the internal job posting.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcseminternaljobs-31548.html#hrcseminternaljobs-31548](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcseminternaljobs-31548.html#hrcseminternaljobs-31548)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_INTERNAL_JOBS_PK | INTERNAL_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INTERNAL_JOB_ID | NUMBER |  | 18 | Yes | This column contains the primary key of the table. |  |
| URI | VARCHAR2 | 1024 |  | Yes | This column contains the URI of the internal job. |  |
| REQUISITION_ID | NUMBER |  |  | Yes | This column contains the requisition ID. |  |
| REQUISITION_NUMBER | VARCHAR2 | 240 |  | Yes | This column contains the requisition number. |  |
| REQUISITION_TITLE | VARCHAR2 | 240 |  |  | This column contains the requisition title. |  |
| JOB_FAMILY_NAME | VARCHAR2 | 240 |  |  | This column contains job family name. |  |
| JOB_FUNCTION_NAME | VARCHAR2 | 128 |  |  | This column contains job function name. |  |
| ORGANIZATION_NAME | VARCHAR2 | 240 |  |  | This column contains the organization name. |  |
| HIRING_MANAGER_NAME | VARCHAR2 | 2000 |  | Yes | This column contains the hiring manager name. |  |
| RECRUITER_NAME | VARCHAR2 | 2000 |  | Yes | This column contains the recruiter name. |  |
| RECRUITER_ID | VARCHAR2 | 128 |  | Yes | This column contains the recruiter id. |  |
| HIRING_MANAGER_ID | VARCHAR2 | 128 |  | Yes | This column contains the hiring manager id. |  |
| ORGANIZATION_ID | VARCHAR2 | 128 |  |  | This column contains organization id. |  |
| JOB_FAMILY_ID | VARCHAR2 | 128 |  |  | This column contains the job family id. |  |
| JOB_FUNCTION_ID | VARCHAR2 | 128 |  |  | This column contains the job function id. |  |
| POSTED_JOB_ID | VARCHAR2 | 128 |  | Yes | This column contains the posted job id. |  |
| SHORT_DESCRIPTION | VARCHAR2 | 1024 |  |  | This column contains the requisition short description. | Obsolete |
| LONG_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column contains the requisition long description. | Obsolete |
| SHORT_DESCRIPTION_CLOB | CLOB |  |  |  | This column contains the short description clob. |  |
| LONG_DESCRIPTION_CLOB | CLOB |  |  |  | This column contains the long description clob. |  |
| POSTING_DATE | TIMESTAMP |  |  | Yes | This column contains the job posting date. |  |
| JOB_SHIFT | VARCHAR2 | 128 |  |  | This column contains the job shift. |  |
| FULL_OR_PART_TIME | VARCHAR2 | 128 |  |  | This column indicates the job is full or part time. |  |
| TRAVEL_REQUIRED | VARCHAR2 | 4 |  |  | This column indicates if this job requires travel. |  |
| POSTING_INTERNAL_ONLY | VARCHAR2 | 4 |  | Yes | This column indicates if the job is posted internally only. |  |
| LOCATION_COUNTRY_ID | VARCHAR2 | 128 |  |  | This column contains the location country id. |  |
| LOCATION_STATE_ID | VARCHAR2 | 128 |  |  | This column contains geography ID of state. |  |
| LOCATION_CITY_ID | VARCHAR2 | 128 |  |  | This column contains geography id of city. |  |
| LOCATION_FQN | VARCHAR2 | 4000 |  |  | This column contains fully qualified name of the location. |  |
| LOCATION_LATITUDE | NUMBER |  |  |  | This contains the latitude of the location. |  |
| LOCATION_LONGITUDE | NUMBER |  |  |  | This column contains the longitude of the location. |  |
| STATUS | NUMBER |  | 8 |  | This column contains the status of the job. |  |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is an error for indexing. |  |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message for the indexing event. |  |
| INDEXING_EVENT_ID | NUMBER |  | 18 |  | This column contains the indexing event id. | Obsolete |
| BATCH_ID | NUMBER |  | 18 |  | This column contains the batch id. |  |
| EDUCATION_LEVEL_ID | VARCHAR2 | 128 |  |  | This column is the Education Level code |  |
| JOB_TYPE_ID | VARCHAR2 | 128 |  |  | This column is the Job type Lookup code |  |
| EXPIRY_DATE | TIMESTAMP |  |  |  | This column is the Job Expiry Date |  |
| MANAGEMENT_LEVEL_ID | VARCHAR2 | 128 |  |  | This column is the Management Level Lookup code |  |
| RECRUITING_TYPE | VARCHAR2 | 128 |  |  | This column is the Recruiting Type Lookup code |  |
| JOB_GRADE_CODE | VARCHAR2 | 128 |  |  | This column is the job grade code |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_SEM_INTERNAL_JOBS_N1 | Non Unique | FUSION_TS_TX_DATA | INDEXING_EVENT_ID | Obsolete |
| HRC_SEM_INTERNAL_JOBS_N2 | Non Unique | FUSION_TS_TX_DATA | REQUISITION_NUMBER |  |
| HRC_SEM_INTERNAL_JOBS_N3 | Non Unique | FUSION_TS_TX_DATA | HIRING_MANAGER_NAME |  |
| HRC_SEM_INTERNAL_JOBS_N4 | Non Unique | FUSION_TS_TX_DATA | RECRUITER_NAME |  |
| HRC_SEM_INTERNAL_JOBS_N5 | Non Unique | FUSION_TS_TX_DATA | POSTED_JOB_ID |  |
| HRC_SEM_INTERNAL_JOBS_N6 | Non Unique | FUSION_TS_TX_DATA | POSTING_DATE |  |
| HRC_SEM_INTERNAL_JOBS_N7 | Non Unique | FUSION_TS_TX_DATA | REQUISITION_ID |  |
| HRC_SEM_INTERNAL_JOBS_N8 | Non Unique | Default | BATCH_ID |  |
| HRC_SEM_INTERNAL_JOBS_N9 | Non Unique | Default | LAST_UPDATE_DATE |  |
| HRC_SEM_INTERNAL_JOBS_U1 | Unique | FUSION_TS_TX_DATA | INTERNAL_JOB_ID |  |
| HRC_SEM_INTERNAL_JOBS_U2 | Unique | FUSION_TS_TX_DATA | URI |  |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
