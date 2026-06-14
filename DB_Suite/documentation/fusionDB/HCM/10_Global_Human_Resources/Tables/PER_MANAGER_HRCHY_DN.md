# PER_MANAGER_HRCHY_DN

This table stores the flattened manager hierarchy details. The denormalized details are derived from the supervisors tables and stored in this table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchydn-5738.html#permanagerhrchydn-5738](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchydn-5738.html#permanagerhrchydn-5738)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| IMMEDIATE_REPORTEE_ASG_ID | NUMBER |  | 18 |  | IMMEDIATE_REPORTEE_ASG_ID column is for internal use in PL/SQL procedure calls. It will not be exposed in the view or entity objects. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERSONS table. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_ASSIGNMENTS_M table. |
| PRIMARY_ASSIGNMENT_FLAG | VARCHAR2 | 30 |  |  | Identifies whether the assignment is the primary |
| MANAGER_ID | NUMBER |  | 18 |  | Foreign Key to Per Persons. Identifies the Person record |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foregin Key to Per Assignments. Identifies the manager's assignment |
| MANAGER_LEVEL | NUMBER |  | 5 |  | Not supported |
| PRIMARY_MANAGER_FLAG | VARCHAR2 | 30 |  |  | Set to Y if manager type = LINE_MANAGER. Automatically generated |
| MANAGER_TYPE | VARCHAR2 | 30 |  |  | Determines the type of manager: line manager, project manager, etc |
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
| PER_MANAGER_HRCHY_DN_N1 | Non Unique | Default | PERSON_ID, ASSIGNMENT_ID, EFFECTIVE_END_DATE, MANAGER_TYPE, MANAGER_ID |
| PER_MANAGER_HRCHY_DN_N2 | Non Unique | Default | MANAGER_ID, MANAGER_ASSIGNMENT_ID |
| PER_MANAGER_HRCHY_DN_N3 | Non Unique | Default | ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_MANAGER_HRCHY_DN_N4 | Non Unique | Default | MANAGER_ASSIGNMENT_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, MANAGER_TYPE, MANAGER_LEVEL |
| PER_MANAGER_HRCHY_DN_N5 | Non Unique | Default | MANAGER_ID, MANAGER_LEVEL, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, MANAGER_TYPE, ASSIGNMENT_ID, BUSINESS_GROUP_ID |
| PER_MANAGER_HRCHY_DN_N6 | Non Unique | Default | PERSON_ID, MANAGER_ASSIGNMENT_ID |
| PER_MANAGER_HRCHY_DN_N7 | Non Unique | Default | MANAGER_ASSIGNMENT_ID, MANAGER_ID, MANAGER_LEVEL, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, MANAGER_TYPE, BUSINESS_GROUP_ID, ASSIGNMENT_ID, PERSON_ID |
| PER_MANAGER_HRCHY_DN_N8 | Non Unique | Default | ASSIGNMENT_ID, PERSON_ID, MANAGER_LEVEL, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, MANAGER_TYPE, BUSINESS_GROUP_ID, MANAGER_ID, MANAGER_ASSIGNMENT_ID |
| PER_MANAGER_HRCHY_DN_U1 | Unique | Default | MANAGER_ASSIGNMENT_ID, ASSIGNMENT_ID, PERSON_ID, MANAGER_ID, MANAGER_LEVEL, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, MANAGER_TYPE, BUSINESS_GROUP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
