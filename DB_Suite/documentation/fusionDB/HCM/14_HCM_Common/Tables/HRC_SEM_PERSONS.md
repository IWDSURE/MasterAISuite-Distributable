# HRC_SEM_PERSONS

This table contains the attributes of a person.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersons-14669.html#hrcsempersons-14669](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersons-14669.html#hrcsempersons-14669)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_PERSONS_PK | PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | This is the primary key of the person table |  |
| URI | VARCHAR2 | 1024 |  | Yes | This contains the unique URI for the person. |  |
| IS_INTERNAL | VARCHAR2 | 4 |  |  | Indicates if a person is internal or external.  Value is 0 for external candidates and 1 for internal cadidates. |  |
| PREFIX | VARCHAR2 | 80 |  |  | This column contains teh prefix of the person. |  |
| FIRST_NAME | VARCHAR2 | 150 |  |  | This is the first name of the person |  |
| MIDDLE_NAME | VARCHAR2 | 80 |  |  | This is the middle name of the person |  |
| LAST_NAME | VARCHAR2 | 150 |  |  | This is the last name of the person. |  |
| FULL_NAME | VARCHAR2 | 2000 |  |  | This is the full name of the person (First + Middle + last) |  |
| SUFFIX | VARCHAR2 | 80 |  |  | This column contains teh suffix of the person. |  |
| WILLING_TO_TRAVEL | VARCHAR2 | 4 |  |  | This column indicates whether the person is willing to travel. |  |
| JOB_LEVEL | VARCHAR2 | 512 |  |  | This column indicates the job level of the person | Obsolete |
| JOB_SCHEDULE | VARCHAR2 | 512 |  |  | This column indicates the job schedule of the person. | Obsolete |
| EMPLOYEE_STATUS | VARCHAR2 | 128 |  |  | This column indicates the employee status of the person. | Obsolete |
| LOCATION_GEOGRAPHY_ID | VARCHAR2 | 80 |  |  | This contains the geography id for the location. | Obsolete |
| LOCATION_COUNTRY_ID | VARCHAR2 | 80 |  |  | This contains the country id for the location. |  |
| LOCATION_STATE_ID | VARCHAR2 | 80 |  |  | This contains the state id for the location. |  |
| LOCATION_CITY_ID | VARCHAR2 | 80 |  |  | This contains the city id for the location. |  |
| LOCATION_POSTAL_CODE | VARCHAR2 | 80 |  |  | This contains the postal code for the location. |  |
| LOCATION_LEAF_NAME | VARCHAR2 | 1024 |  |  | This contains the leaf name of the location. | Obsolete |
| LOCATION_FQN | VARCHAR2 | 4000 |  |  | This contains the fully qualified name of the location. |  |
| TOTAL_YEARS_EXPERIENCE | NUMBER |  |  |  | This column contains the total years of experience. |  |
| LOCATION_ADDRESS_LINE1 | VARCHAR2 | 128 |  |  | This contains the address line 1 of the location. |  |
| LOCATION_ADDRESS_LINE2 | VARCHAR2 | 128 |  |  | This contains the address line 2 of the location. |  |
| REHIRE_ELIGIBILITY | VARCHAR2 | 128 |  |  | Whether the employee is recommended for rehire (can have 3 values) |  |
| LOCATION_LATITUDE | NUMBER |  |  |  | This contains the latitude of the location. |  |
| LOCATION_LONGITUDE | NUMBER |  |  |  | This contains the longitude of the location. |  |
| STATUS | NUMBER |  | 8 |  | This column contains the status of the indexing event. |  |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is error in the indexing event. |  |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message of the indexing event. |  |
| INDEXING_EVENT_ID | NUMBER |  | 18 |  | This column contains the indexing event id. | Obsolete |
| BATCH_ID | NUMBER |  | 18 |  | This column contains the batch id. |  |
| OPT_IN | VARCHAR2 | 4 |  |  | True if candidate has opted-in for marketing emails |  |
| UNSUBSCRIBED | VARCHAR2 | 4 |  |  | True if candidate has unsubscribed from marketing emails |  |
| REFERRED | VARCHAR2 | 4 |  |  | True if candidate was referred to any job |  |
| ENDORSED | VARCHAR2 | 4 |  |  | True if candidate was endorsed for any job |  |
| PROSPECT | VARCHAR2 | 4 |  |  | True if candidate is a prospect for any open job |  |
| SOURCE | VARCHAR2 | 512 |  |  | Name of the source that resulted in this candidate |  |
| MEDIUM | VARCHAR2 | 512 |  |  | Name of the medium that resulted in this candidate |  |
| WILLING_TO_RELOCATE | VARCHAR2 | 4 |  |  | True if candidate is willing to relocate |  |
| PROFILE_LAST_UPDATED | TIMESTAMP |  |  |  | Last time this candidate profile was updated |  |
| LAST_INTERACTION_DATE | TIMESTAMP |  |  |  | Last time this candidate had an interaction |  |
| LAST_CAMPAIGN_DATE | TIMESTAMP |  |  |  | Last time this candidate was sent a campaign |  |
| ACTIVE_CANDIDATE | VARCHAR2 | 4 |  |  | True if candidate has an acive application on any open job |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_SEM_PERSONS_N1 | Non Unique | FUSION_TS_TX_DATA | INDEXING_EVENT_ID | Obsolete |
| HRC_SEM_PERSONS_N2 | Non Unique | FUSION_TS_TX_DATA | IS_INTERNAL |  |
| HRC_SEM_PERSONS_N3 | Non Unique | FUSION_TS_TX_DATA | LOCATION_COUNTRY_ID | Obsolete |
| HRC_SEM_PERSONS_N4 | Non Unique | FUSION_TS_TX_DATA | LOCATION_STATE_ID |  |
| HRC_SEM_PERSONS_N5 | Non Unique | FUSION_TS_TX_DATA | LOCATION_CITY_ID |  |
| HRC_SEM_PERSONS_N6 | Non Unique | FUSION_TS_TX_DATA | LOCATION_FQN |  |
| HRC_SEM_PERSONS_N7 | Non Unique | FUSION_TS_TX_DATA | FULL_NAME |  |
| HRC_SEM_PERSONS_N8 | Non Unique | Default | BATCH_ID |  |
| HRC_SEM_PERSONS_N9 | Non Unique | Default | LAST_UPDATE_DATE |  |
| HRC_SEM_PERSONS_U1 | Unique | FUSION_TS_TX_DATA | PERSON_ID |  |
| HRC_SEM_PERSONS_U2 | Unique | FUSION_TS_TX_DATA | URI |  |
| HRC_SEM_PERSONS_U3 | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, PERSON_ID | Obsolete |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
