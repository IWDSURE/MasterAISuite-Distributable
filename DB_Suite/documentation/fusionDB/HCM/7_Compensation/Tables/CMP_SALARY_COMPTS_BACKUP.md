# CMP_SALARY_COMPTS_BACKUP

Temporary salary components backup table for future salary proposal during global transfer flow.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarycomptsbackup-16551.html#cmpsalarycomptsbackup-16551](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarycomptsbackup-16551.html#cmpsalarycomptsbackup-16551)

## Primary Key

| Name | Columns |
|------|----------|
| cmp_salary_compts_backup_PK | SALARY_COMPTS_BACKUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SALARY_BACKUP_ID | NUMBER |  | 18 |  | SALARY_BACKUP_ID |
| SALARY_COMPTS_BACKUP_ID | NUMBER |  | 18 | Yes | SALARY_COMPTS_BACKUP_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| SALARY_ID | NUMBER |  | 18 |  | SALARY_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| COMPONENT_REASON_CODE | VARCHAR2 | 30 |  |  | COMPONENT_REASON_CODE |
| CHANGE_AMOUNT | NUMBER |  |  |  | CHANGE_AMOUNT |
| CHANGE_PERCENT | NUMBER |  |  |  | CHANGE_PERCENT |
| PAY_RATE_DEFINITION_ID | NUMBER |  | 18 |  | PAY_RATE_DEFINITION_ID |
| RATE_AMOUNT | NUMBER |  |  |  | RATE_AMOUNT |
| RATE_PERCENTAGE | NUMBER |  |  |  | RATE_PERCENTAGE |
| BASIS_SIMPLE_COMPONENT_ID | NUMBER |  | 18 |  | BASIS_SIMPLE_COMPONENT_ID |
| SIMPLE_RATE_AMOUNT | NUMBER |  |  |  | SIMPLE_RATE_AMOUNT |
| SIMPLE_RATE_PERCENTAGE | NUMBER |  |  |  | SIMPLE_RATE_PERCENTAGE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_COMPTS_BACKUP_N1 | Non Unique | Default | SALARY_BACKUP_ID, ASSIGNMENT_ID |
| CMP_SALARY_COMPTS_BACKUP_U1 | Unique | Default | SALARY_COMPTS_BACKUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
