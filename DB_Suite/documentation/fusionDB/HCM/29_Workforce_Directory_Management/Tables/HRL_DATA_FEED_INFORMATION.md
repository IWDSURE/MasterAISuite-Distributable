# HRL_DATA_FEED_INFORMATION

This table stores the Spotlight data feed information.

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedinformation-19677.html#hrldatafeedinformation-19677](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedinformation-19677.html#hrldatafeedinformation-19677)

## Primary Key

| Name | Columns |
|------|----------|
| HRL_DATA_FEED_INFORMATION_PK | DF_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DF_INFO_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a data feed information. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| DF_SETTING_ID | NUMBER |  | 18 | Yes | Identifier of data feed setting.Foreign key to HRL_DATA_FEED_SETTINGS_B. |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifier of person. Foreign key to PER_PERSONS. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Identifier of assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |
| PK1_NUM_VALUE | NUMBER |  | 18 |  | First nuemeric primary key of the feed type. |
| PK2_NUM_VALUE | NUMBER |  | 18 |  | Second nuemeric primary key of the feed information category. |
| PK3_NUM_VALUE | NUMBER |  | 18 |  | Third numeric primary key of the feed information category. |
| PK1_CHAR_VALUE | VARCHAR2 | 150 |  |  | First  char primary key of the feed information category. |
| PK2_CHAR_VALUE | VARCHAR2 | 150 |  |  | second char primary key of the feed feed information category. |
| DF_INFORMATION_CATEGORY | VARCHAR2 | 80 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| DF_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION1 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION2 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION3 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION4 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION5 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION6 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION7 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION8 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION9 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION10 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DF_INFORMATION_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRL_DATA_FEED_INFORMATION_N1 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID, ASSIGNMENT_ID, DF_INFORMATION_CATEGORY |
| HRL_DATA_FEED_INFORMATION_PK | Unique | FUSION_TS_TX_IDX | DF_INFO_ID |

---

[← Back to Index](../29_Workforce_Directory_Management_Tables_Index.md)
