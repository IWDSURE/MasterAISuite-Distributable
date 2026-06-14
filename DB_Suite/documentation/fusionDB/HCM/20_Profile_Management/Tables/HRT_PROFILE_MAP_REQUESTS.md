# HRT_PROFILE_MAP_REQUESTS

Profile Upgrade Mapping Request table stores the upgrade run request data.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemaprequests-20709.html#hrtprofilemaprequests-20709](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilemaprequests-20709.html#hrtprofilemaprequests-20709)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFLE_MAP_REQUESTS_PK | MAPPING_REQUEST_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_REQUEST_ID | NUMBER |  | 18 | Yes | MAPPING_REQUEST_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| INSTANCE_ID | NUMBER |  | 18 | Yes | INSTANCE_ID |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| END_TIME | TIMESTAMP |  |  |  | END_TIME |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| ACTION | VARCHAR2 | 30 |  |  | ACTION |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFLE_MAP_REQUESTS_U1 | Unique | Default | MAPPING_REQUEST_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
