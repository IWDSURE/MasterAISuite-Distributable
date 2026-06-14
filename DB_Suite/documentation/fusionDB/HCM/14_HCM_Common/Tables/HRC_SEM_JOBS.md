# HRC_SEM_JOBS

This table contains information about the job.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemjobs-15047.html#hrcsemjobs-15047](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemjobs-15047.html#hrcsemjobs-15047)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_JOBS_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | This is the primary column of job table. |  |
| URI | VARCHAR2 | 1024 |  | Yes | This is the uri of the job from an employer. |  |
| REQUISITION_ID | NUMBER |  |  | Yes | This is the requisition ID of the job. |  |
| REQUISITION_TITLE | VARCHAR2 | 240 |  |  | This column contains the requisition title. |  |
| REQUISITION_NUMBER | VARCHAR2 | 240 |  |  | This column is the Requisition Number ( Can be alphanumeric ) |  |
| TITLE | VARCHAR2 | 80 |  |  | This column describes the title of the job. | Obsolete |
| JOB_FAMILY_NAME | VARCHAR2 | 240 |  |  | This column contains the job family name. |  |
| JOB_FUNCTION_NAME | VARCHAR2 | 128 |  |  | This column contains the job function name. |  |
| JOB_FAMILY_ID | VARCHAR2 | 128 |  |  | This column contains the job family ID. |  |
| JOB_FUNCTION_ID | VARCHAR2 | 128 |  |  | This column contains the job function id. |  |
| POSTED_JOB_ID | VARCHAR2 | 128 |  | Yes | This column contains the posted job id. |  |
| ORGANIZATION_ID | VARCHAR2 | 128 |  |  | This column contains organization id |  |
| SHORT_DESCRIPTION | VARCHAR2 | 1024 |  |  | This columns contains the short description. | Obsolete |
| LONG_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column contains long description. | Obsolete |
| SHORT_DESCRIPTION_CLOB | CLOB |  |  |  | This column contains the short description clob. |  |
| LONG_DESCRIPTION_CLOB | CLOB |  |  |  | This column contains the long description clob. |  |
| POSTED_DATE | TIMESTAMP |  |  | Yes | This is the posted date of the job. |  |
| TRAVEL_REQUIRED | VARCHAR2 | 4 |  |  | This column indicates if this job requires travel. |  |
| INTERNAL_DETAILS | CLOB |  |  |  | This column describes the internal details of the job. | Obsolete |
| EXTERNAL_DETAILS | CLOB |  |  |  | This column describes the external details of the job. | Obsolete |
| INTERNAL_SNIPPET | VARCHAR2 | 4000 |  |  | This column describes the internal snippet of the job. | Obsolete |
| EXTERNAL_SNIPPET | VARCHAR2 | 4000 |  |  | This column describes the external snippet of the job. | Obsolete |
| FAMILY | VARCHAR2 | 512 |  |  | This column describes the family of the job. | Obsolete |
| CATEGORY_ID | VARCHAR2 | 80 |  |  | This is the job category ID of the job. | Obsolete |
| DEPARTMENT | VARCHAR2 | 512 |  |  | This is the department where the job belongs to. | Obsolete |
| DEPARTMENT_DESCRIPTION | VARCHAR2 | 4000 |  |  | This column describes the description of the job. | Obsolete |
| LOCATION_GEOGRAPHY_ID | VARCHAR2 | 80 |  |  | This contains the geography id of the location. | Obsolete |
| LOCATION_COUNTRY_ID | VARCHAR2 | 80 |  |  | This contains the country id of the location. |  |
| LOCATION_STATE_ID | VARCHAR2 | 80 |  |  | This contains the state id of the location. |  |
| LOCATION_CITY_ID | VARCHAR2 | 80 |  |  | This contains the city id of the location. |  |
| LOCATION_POSTAL_CODE | VARCHAR2 | 80 |  |  | This contains the postal code of the location. | Obsolete |
| LOCATION_LEAF_NAME | VARCHAR2 | 1024 |  |  | This contains the leaf name of the location. | Obsolete |
| LOCATION_FQN | VARCHAR2 | 4000 |  |  | This contains the fully qualified name of the location. |  |
| LOCATION_LATITUDE | NUMBER |  |  |  | This contains the latitude of the location. |  |
| LOCATION_LONGITUDE | NUMBER |  |  |  | This contains the longitude of the location. |  |
| LOCATION_ADDRESS_LINE1 | VARCHAR2 | 128 |  |  | This contains the address line 1 of the location. | Obsolete |
| LOCATION_ADDRESS_LINE2 | VARCHAR2 | 128 |  |  | This contains the address line 2 of the location. | Obsolete |
| STATUS | NUMBER |  | 8 |  | This column contains the status of the indexing event. |  |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is an error in the indexing event. |  |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message of the indexing event. |  |
| INDEXING_EVENT_ID | NUMBER |  | 18 |  | This column contains the indexing event id. | Obsolete |
| BATCH_ID | NUMBER |  | 18 |  | This column contains the batch id. |  |
| JOB_SHIFT_ID | VARCHAR2 | 128 |  |  | This column is the Job shift Lookup code |  |
| FULL_OR_PART_TIME_ID | VARCHAR2 | 128 |  |  | This column is the Full/part time look up code |  |
| EDUCATION_LEVEL_ID | VARCHAR2 | 128 |  |  | This column is the Education Level code |  |
| JOB_TYPE_ID | VARCHAR2 | 128 |  |  | This column is the Job type Lookup code |  |
| EXPIRY_DATE | TIMESTAMP |  |  |  | This column is the Job Expiry Date |  |
| MANAGEMENT_LEVEL_ID | VARCHAR2 | 128 |  |  | This column is the Management Level Lookup code |  |
| RECRUITING_TYPE | VARCHAR2 | 128 |  |  | This column is the Recruiting Type Lookup code |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_SEM_JOBS_N1 | Non Unique | FUSION_TS_TX_DATA | INDEXING_EVENT_ID | Obsolete |
| HRC_SEM_JOBS_N10 | Non Unique | FUSION_TS_TX_DATA | LOCATION_CITY_ID | Obsolete |
| HRC_SEM_JOBS_N11 | Non Unique | FUSION_TS_TX_DATA | POSTED_JOB_ID |  |
| HRC_SEM_JOBS_N12 | Non Unique | Default | BATCH_ID |  |
| HRC_SEM_JOBS_N13 | Non Unique | Default | LAST_UPDATE_DATE |  |
| HRC_SEM_JOBS_N2 | Non Unique | FUSION_TS_TX_DATA | FAMILY | Obsolete |
| HRC_SEM_JOBS_N3 | Non Unique | FUSION_TS_TX_DATA | LOCATION_FQN | Obsolete |
| HRC_SEM_JOBS_N4 | Non Unique | FUSION_TS_TX_DATA | REQUISITION_ID |  |
| HRC_SEM_JOBS_N5 | Non Unique | FUSION_TS_TX_DATA | POSTED_DATE |  |
| HRC_SEM_JOBS_N6 | Non Unique | FUSION_TS_TX_DATA | CATEGORY_ID | Obsolete |
| HRC_SEM_JOBS_N7 | Non Unique | FUSION_TS_TX_DATA | DEPARTMENT | Obsolete |
| HRC_SEM_JOBS_N8 | Non Unique | FUSION_TS_TX_DATA | LOCATION_COUNTRY_ID | Obsolete |
| HRC_SEM_JOBS_N9 | Non Unique | FUSION_TS_TX_DATA | LOCATION_STATE_ID | Obsolete |
| HRC_SEM_JOBS_U1 | Unique | FUSION_TS_TX_DATA | JOB_ID |  |
| HRC_SEM_JOBS_U2 | Unique | FUSION_TS_TX_DATA | URI |  |
| HRC_SEM_JOBS_U3 | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, JOB_ID | Obsolete |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
