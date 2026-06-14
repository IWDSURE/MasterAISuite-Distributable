# CMP_TCS_PER_PERD_STMT

Table that stores the statement information for a person. This is a child of cmp_tcs_per_perd. 
A record is created for a employer for a person. If a person has more than one employer data or a person has any data at person level, the process automatically create a record for  All employer (null legal_entity_id).  If a person has only one employer (one_assignment_id)  then there will not be a all employer record ( al the information will be assign to the employer)

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdstmt-6342.html#cmptcsperperdstmt-6342](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdstmt-6342.html#cmptcsperperdstmt-6342)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_PER_PERD_STMT_PK | PER_PERD_STMT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_PERD_STMT_ID | NUMBER |  | 18 | Yes | PER_PERD_STMT_ID |
| STMT_AUDIT_DATE | DATE |  |  |  | STMT_AUDIT_DATE |
| STMT_VIEWED_DATE | TIMESTAMP |  |  |  | STMT_VIEWED_DATE |
| LOCAL_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Local Currency Code |
| STMT_AUDITED_BY | VARCHAR2 | 200 |  |  | STMT_AUDITED_BY |
| PER_PERD_ID | NUMBER |  | 18 | Yes | PER_PERD_ID |
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| PRIME_ASSIGNMENT_ID | NUMBER |  | 18 |  | PRIME_ASSIGNMENT_ID |
| PRIME_ASSIGNMENT_DATE | DATE |  |  |  | PRIME_ASSIGNMENT_DATE |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| WORKER_NUMBER | VARCHAR2 | 30 |  |  | WORKER_NUMBER |
| SALARY_AMOUNT | NUMBER |  |  |  | SALARY_AMOUNT |
| SALARY_CURRENCY | VARCHAR2 | 30 |  |  | SALARY_CURRENCY |
| SALARY_PERIOD_CODE | VARCHAR2 | 30 |  |  | SALARY_PERIOD_CODE |
| HIRE_DATE | DATE |  |  |  | HIRE_DATE |
| XML_LOB_STMT | CLOB |  |  |  | XML_LOB_STMT |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| HIDE_SUMMARY_FLAG | VARCHAR2 | 1 |  |  | HIDE_SUMMARY_FLAG |
| DSP_DETAIL_JOB_FLAG | VARCHAR2 | 1 |  |  | DSP_DETAIL_JOB_FLAG |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROCESS_REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the child job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| POSITION_ID | NUMBER |  | 18 |  | POSITION_ID |
| END_DATE | DATE |  |  |  | END_DATE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_PERD_STMT_N1 | Non Unique | Default | PERD_RUN_ID, PERSON_ID |
| CMP_TCS_PER_PERD_STMT_N2 | Non Unique | Default | PER_PERD_ID |
| CMP_TCS_PER_PERD_STMT_UK1 | Unique | Default | PER_PERD_STMT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
