# CMP_BATCH_ERRORS

This table will have all the errors for an assignment when salary batch process runs for calculating rate values. Errors can be logged in processing, posting or when doing a rollback.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbatcherrors-14014.html#cmpbatcherrors-14014](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbatcherrors-14014.html#cmpbatcherrors-14014)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_BATCH_ERRORS_PK | BATCH_ERROR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ERROR_ID | NUMBER |  | 18 | Yes | BATCH_ERROR_ID |
| BATCH_REQUEST_ID | NUMBER |  | 18 |  | BATCH_REQUEST_ID |
| BATCH_NAME | VARCHAR2 | 80 |  |  | BATCH_NAME |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| ASSIGNMENT_TYPE | VARCHAR2 | 30 |  |  | ASSIGNMENT_TYPE |
| ERROR_SOURCE_TABLE | VARCHAR2 | 150 |  |  | ERROR_SOURCE_TABLE |
| ERROR_ORIGINATING_PROCESS | VARCHAR2 | 80 |  | Yes | ERROR_ORIGINATING_PROCESS |
| ERROR_TYPE | VARCHAR2 | 30 |  |  | ERROR_TYPE |
| ERROR_MESSAGE_ID | NUMBER |  | 18 |  | ERROR_MESSAGE_ID |
| ERROR_MESSAGE_TEXT | VARCHAR2 | 500 |  |  | ERROR_MESSAGE_TEXT |
| ERROR_STACK | CLOB |  |  |  | ERROR_STACK |
| SALARY_ASG_INFO_ID | NUMBER |  | 18 |  | SALARY_ASG_INFO_ID |
| SALARY_BATCH_INFO_ID | NUMBER |  | 18 |  | SALARY_BATCH_INFO_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_BATCH_ERRORS_N1 | Non Unique | Default | ASSIGNMENT_ID, ERROR_ORIGINATING_PROCESS, ERROR_TYPE |
| CMP_BATCH_ERRORS_N2 | Non Unique | Default | PERSON_ID, ERROR_ORIGINATING_PROCESS, ERROR_TYPE |
| CMP_BATCH_ERRORS_N3 | Non Unique | Default | ERROR_SOURCE_TABLE, ERROR_TYPE |
| CMP_BATCH_ERRORS_N4 | Non Unique | Default | BATCH_NAME |
| CMP_BATCH_ERRORS_U1 | Unique | Default | BATCH_ERROR_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
