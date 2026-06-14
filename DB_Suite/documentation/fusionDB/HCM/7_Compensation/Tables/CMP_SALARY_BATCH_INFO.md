# CMP_SALARY_BATCH_INFO

Contains the details of the salary batch rate process request details along with the parameters passed which be show in the batch results user interface.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybatchinfo-22228.html#cmpsalarybatchinfo-22228](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybatchinfo-22228.html#cmpsalarybatchinfo-22228)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_BATCH_INFO_PK | BATCH_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 80 |  |  | LEGISLATION_CODE |
| BATCH_INFO_ID | NUMBER |  | 18 | Yes | BATCH_INFO_ID |
| BATCH_NAME | VARCHAR2 | 80 |  | Yes | BATCH_NAME |
| PROCESS_REQUEST_ID | NUMBER |  | 18 | Yes | PROCESS_REQUEST_ID |
| PROCESS_START_DATE_TIME | TIMESTAMP |  |  |  | PROCESS_START_DATE_TIME |
| PROCESS_END_DATE_TIME | TIMESTAMP |  |  |  | PROCESS_END_DATE_TIME |
| PROCESS_SALARY_FLAG | VARCHAR2 | 30 |  |  | PROCESS_SALARY_FLAG |
| PROCESS_TOTAL_ASG | NUMBER |  | 10 |  | PROCESS_TOTAL_ASG |
| PROCESS_ERRORED_ASG | NUMBER |  | 10 |  | PROCESS_ERRORED_ASG |
| POSTED_REQUEST_ID | NUMBER |  | 18 |  | POSTED_REQUEST_ID |
| POSTED_START_DATE_TIME | TIMESTAMP |  |  |  | POSTED_START_DATE_TIME |
| POSTED_END_DATE_TIME | TIMESTAMP |  |  |  | POSTED_END_DATE_TIME |
| POSTED_SALARY_FLAG | VARCHAR2 | 30 |  |  | POSTED_SALARY_FLAG |
| POSTED_TOTAL_ASG | NUMBER |  | 10 |  | POSTED_TOTAL_ASG |
| POSTED_ERRORED_ASG | NUMBER |  | 10 |  | POSTED_ERRORED_ASG |
| ROLLBACK_REQUEST_ID | NUMBER |  | 18 |  | ROLLBACK_REQUEST_ID |
| ROLLBACK_START_DATE_TIME | TIMESTAMP |  |  |  | ROLLBACK_START_DATE_TIME |
| ROLLBACK_END_DATE_TIME | TIMESTAMP |  |  |  | ROLLBACK_END_DATE_TIME |
| ROLLBACK_SALARY_FLAG | VARCHAR2 | 30 |  |  | ROLLBACK_SALARY_FLAG |
| ROLLBACK_TOTAL_ASG | NUMBER |  | 10 |  | ROLLBACK_TOTAL_ASG |
| ROLLBACK_ERRORED_ASG | NUMBER |  | 10 |  | ROLLBACK_ERRORED_ASG |
| PROCESS_MODE_CODE | VARCHAR2 | 60 |  | Yes | PROCESS_MODE_CODE |
| INSERT_ZERO_ADJUSTMENT | VARCHAR2 | 30 |  |  | INSERT_ZERO_ADJUSTMENT |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| ACTION_REASON_ID | NUMBER |  | 18 |  | ACTION_REASON_ID |
| RANGE_START_DATE | DATE |  |  |  | RANGE_START_DATE |
| RANGE_END_DATE | DATE |  |  |  | RANGE_END_DATE |
| BEN_ACTION_ID | NUMBER |  | 18 |  | BEN_ACTION_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| WORK_LOCATION_ID | NUMBER |  | 18 |  | WORK_LOCATION_ID |
| DEPARTMENT_ID | NUMBER |  | 18 |  | DEPARTMENT_ID |
| PERSON_RULE_ID | NUMBER |  | 18 |  | PERSON_RULE_ID |
| RUN_TYPE | VARCHAR2 | 30 |  |  | RUN_TYPE |
| AUDIT_LOG | VARCHAR2 | 30 |  |  | AUDIT_LOG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_BATCH_INFO_N1 | Non Unique | Default | BATCH_NAME |
| CMP_SALARY_BATCH_INFO_N2 | Non Unique | Default | PROCESS_MODE_CODE |
| CMP_SALARY_BATCH_INFO_U1 | Unique | Default | BATCH_INFO_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
