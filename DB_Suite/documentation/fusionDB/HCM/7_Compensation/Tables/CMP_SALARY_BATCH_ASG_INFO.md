# CMP_SALARY_BATCH_ASG_INFO

Contains the details of the each assignment picked up by the salary batch process based on the criteria used while submitting the batch job.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybatchasginfo-28570.html#cmpsalarybatchasginfo-28570](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybatchasginfo-28570.html#cmpsalarybatchasginfo-28570)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_BATCH_ASG_INFO_PK | ASSIGNMENT_ID, SALARY_ASG_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| SALARY_ASG_INFO_ID | NUMBER |  | 18 | Yes | SALARY_ASG_INFO_ID |
| BATCH_INFO_ID | NUMBER |  | 18 | Yes | BATCH_INFO_ID |
| PROCESS_MODE_CODE | VARCHAR2 | 30 |  | Yes | PROCESS_MODE_CODE |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_TYPE | VARCHAR2 | 20 |  |  | ASSIGNMENT_TYPE |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| POSTED_FLAG | VARCHAR2 | 30 |  |  | POSTED_FLAG |
| ROLLBACK_FLAG | VARCHAR2 | 30 |  |  | ROLLBACK_FLAG |
| PROCESSED_FLAG | VARCHAR2 | 30 |  |  | PROCESSED_FLAG |
| ERRORED_FLAG | VARCHAR2 | 30 |  |  | ERRORED_FLAG |
| POSTING_APPROVED | VARCHAR2 | 30 |  |  | POSTING_APPROVED |
| POSTING_REJECTED | VARCHAR2 | 30 |  |  | POSTING_REJECTED |
| ASSIGNMENT_OVN | NUMBER |  | 9 |  | ASSIGNMENT_OVN |
| BATCH_ERROR_ID | NUMBER |  | 18 |  | BATCH_ERROR_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_BATCH_ASG_INFO_N1 | Non Unique | Default | ASSIGNMENT_ID, PROCESS_MODE_CODE |
| CMP_SALARY_BATCH_ASG_INFO_U1 | Unique | Default | ASSIGNMENT_ID, SALARY_ASG_INFO_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
