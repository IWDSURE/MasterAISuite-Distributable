# PAY_GEOGRAPHY_INTERFACE

This interface table contains geography information from ORAMAST.txt file.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** INTERFACE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographyinterface-19059.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygeographyinterface-19059.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECORD_TYPE | NUMBER |  | 2 |  | For internal use only |
| LEGISLATION_CODE | VARCHAR2 | 2 |  |  | Code of the country to which the Geography belongs |
| AREA1 | NUMBER |  | 2 |  | State jurisdiction code |
| AREA2 | NUMBER |  | 3 |  | County jurisdiction code |
| AREA3 | NUMBER |  | 10 |  | City jurisdiction code |
| AREA4 | NUMBER |  | 5 |  | School District code |
| START_DATE | DATE |  |  |  | Start date from which this geography is valid for use. |
| END_DATE | DATE |  |  |  | Date from which this geography is no longer valid. |
| CREATION_VERSION | NUMBER |  | 5 |  | Column to record the file version of third party content provider in which this record was first introduced |
| LAST_UPDATION_VERSION | NUMBER |  | 5 |  | Column to record the file version of third party content provider in which this record was last updated |
| GEOGRAPHY_SHORT_NAME | VARCHAR2 | 2 |  |  | Abbreviation for country or state based on whether this record is for a country or state |
| GEOGRAPHY_NAME | VARCHAR2 | 360 |  |  | Complete name of Geography |
| GEOGRAPHY_ID | NUMBER |  | 18 |  | Unique geography identifier for geographies |
| START_RANGE | VARCHAR2 | 10 |  |  | Column for recording the lowest value in the zip code range |
| END_RANGE | VARCHAR2 | 10 |  |  | Column for recording the highest value in the zip code range |
| STATUS | VARCHAR2 | 60 |  |  | Column to indicate whether this geography record is to be inserted or updated |
| IDENTIFIER_STATUS | VARCHAR2 | 60 |  |  | Column to indicate whether geocode and primary city geography identifier record is to be inserted or updated |
| GEO_DATA_PROVIDER | VARCHAR2 | 60 |  |  | Name of the data source provider |
| PROVIDER_GEO_ID | VARCHAR2 | 20 |  |  | Name of the provider ID |
| PARENT_PROVIDER_GEO_ID | VARCHAR2 | 20 |  |  | Name of the parent provider ID |
| EXTERNAL_IDENTIFIER | VARCHAR2 | 360 |  |  | Name of the EXTERNAL_IDENTIFIER |
| PRIMARY_FLAG | VARCHAR2 | 1 |  |  | Flag indicates whether the city and Township geography is primary geography |
| MULTIPLE_PARENT_FLAG | VARCHAR2 | 1 |  |  | Indicates whether this geography has multiple parents. |
| FILE_VERSION_NUMBER | NUMBER |  | 5 |  | File version of third party data source provider |
| FILE_VERSION_DATE | DATE |  |  |  | File Version Date of third party data source provider |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LANGUAGE_CODE | VARCHAR2 | 3 |  |  | Used to distinguish between English and French spellings for Canadian geographies.‘US’ and 'FRC' respectively indicate English and French  spellings of the geography. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_GEOGRAPHY_INTERFACE_U1 | Unique | Default | RECORD_TYPE, LEGISLATION_CODE, AREA1, AREA2, AREA3, AREA4, START_DATE, END_DATE, GEOGRAPHY_NAME, START_RANGE, PROVIDER_GEO_ID, PARENT_PROVIDER_GEO_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
