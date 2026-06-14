# CMP_TCS_PER_PERD_FEEDBACKS

This table stores value for Employees Fweedback for Statements

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdfeedbacks-5156.html#cmptcsperperdfeedbacks-5156](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdfeedbacks-5156.html#cmptcsperperdfeedbacks-5156)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_PERD_FEEDBACK_ID | NUMBER |  | 18 | Yes | Primary Key for person Feedback |
| PER_PERD_ID | NUMBER |  | 18 | Yes | PER_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| RATING_CODE | VARCHAR2 | 30 |  |  | RATING_CODE |
| FEEDBACK1 | VARCHAR2 | 1000 |  |  | Feedback Response 1 |
| FEEDBACK2 | VARCHAR2 | 1000 |  |  | Feedback Response 2 |
| FEEDBACK3 | VARCHAR2 | 1000 |  |  | Feedback Response 3 |
| FEEDBACK4 | VARCHAR2 | 1000 |  |  | Feedback Response 4 |
| FEEDBACK5 | VARCHAR2 | 1000 |  |  | Feedback Response 5 |
| CONFIRMED_FLAG | VARCHAR2 | 1 |  |  | Determines if the feedback is confirmed |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_FEEDBACKS_FK1 | Non Unique | Default | STMT_ID, STMT_PERD_ID, PERSON_ID |
| CMP_TCS_PER_FEEDBACKS_FK2 | Non Unique | Default | PER_PERD_ID |
| CMP_TCS_PER_FEEDBACKS_FK3 | Non Unique | Default | PERD_RUN_ID |
| CMP_TCS_PER_FEEDBACKS_FK4 | Non Unique | CMP_TCS_PER_FEEDBACKS_FK4 | RATING_CODE, STMT_PERD_ID, STMT_ID |
| CMP_TCS_PER_FEEDBACKS_UK1 | Unique | Default | PER_PERD_FEEDBACK_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
