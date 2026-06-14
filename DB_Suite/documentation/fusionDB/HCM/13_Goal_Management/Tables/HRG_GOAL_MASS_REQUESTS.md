# HRG_GOAL_MASS_REQUESTS

Stores the details of "Goal plan generation" or "Goal mass assignment" request submitted by HR or Administrator.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalmassrequests-25393.html#hrggoalmassrequests-25393](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalmassrequests-25393.html#hrggoalmassrequests-25393)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_MASS_REQUESTS_PK | MASS_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_REQUEST_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry |
| EXCLUDE_WORKERS_NOT_IN_GP_FLAG | VARCHAR2 | 30 |  |  | Exclude workers who are not in the goal plan. |
| ACTION_TYPE | VARCHAR2 | 30 |  |  | Stores mass action type - share or assign action |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | The review period id of the goal plan. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| REQUEST_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Type of request. Possible values are "Goal Plan Generation" and "Goal Mass Assignment" |
| GOAL_PLAN_ID | NUMBER |  | 18 |  | Id of the Goal Plan that is to be assigned through goal plan generation process. |
| GOAL_PLAN_SET_ID | NUMBER |  | 18 |  | Id of the Goal Plan Set that is to be assigned through goal plan set generation process. |
| REQ_SUBMITTED_BY_PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F, which holds ID of person who submits the request. |
| REQ_ON_BEHALF_OF_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F, which holds the requester's ID. |
| REQUEST_SUBMISSION_DATE | TIMESTAMP |  |  | Yes | Date of request submission |
| REQUEST_SOURCE_CODE | VARCHAR2 | 30 |  |  | To store the source of the request submission like Manager flow, Admin flow etc |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MASS_REQUEST_NAME | VARCHAR2 | 200 |  |  | The name of the mass request. |
| PARENT_ID | NUMBER |  | 18 |  | The parent mass request Id. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_MASS_REQUESTS_PK | Unique | Default | MASS_REQUEST_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
