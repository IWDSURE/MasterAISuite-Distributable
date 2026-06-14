# HNS_PERSONS_

HNS PERSONS. This table stores Owner / Person related data. The column Type signifies type of activity (Incident, Investigation or Action).

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnspersons-29150.html#hnspersons-29150](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnspersons-29150.html#hnspersons-29150)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_PERSONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 |  | Task Assigned to the person/owner. |
| EMPLOYEE_ID | NUMBER |  | 18 |  | EMPLOYEE_ID column : Employee ID of the owner. |
| PERSON_ASSIGN_ID | NUMBER |  | 18 |  | PERSON_ASSIGN_ID column : Assignment ID of the person. |
| ROLE_CODE | VARCHAR2 | 30 |  |  | Role ID assigned to the person. |
| TARGET_COMPLETION_DATE | TIMESTAMP |  |  |  | Target completion date for the task assigned to the person. |
| ACTUAL_COMPLETION_DATE | TIMESTAMP |  |  |  | Actual completion date of the task  assigned to the person. |
| COMPLETED_FLAG | VARCHAR2 | 1 |  |  | Completed flag. Signifies whether the task is completed |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag. Signifies whether the task assigned is deleted |
| TASK_TYPE_CODE | VARCHAR2 | 30 |  |  | Task Type identifier. Lookup to the Task Type FND lookup. |
| PERSON_ID | NUMBER |  | 18 | Yes | Unique person identifier. This is the system generated primary key for HNS_PERSONS table. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RESULT_CODE | VARCHAR2 | 30 |  |  | Result Code Column : Incident Owner check result code. |
| ACTION_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Action Required Flag Column : Check box to confirm whether an action is required. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_PERSONSN1_ | Non Unique | Default | PERSON_ID, LAST_UPDATE_DATE |
| HNS_PERSONS_UK1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
