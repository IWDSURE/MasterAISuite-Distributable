# CMP_SALARY_BACKUP

Temporary salary backup table for future salary proposal during global transfer flow.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybackup-26553.html#cmpsalarybackup-26553](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybackup-26553.html#cmpsalarybackup-26553)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_BACKUP_PK | SALARY_BACKUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SALARY_BACKUP_ID | NUMBER |  | 18 | Yes | SALARY_BACKUP_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| SALARY_ID | NUMBER |  | 18 |  | SALARY_ID |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| ACTION_REASON_ID | NUMBER |  | 18 |  | ACTION_REASON_ID |
| DATE_FROM | DATE |  |  |  | DATE_FROM |
| DATE_TO | DATE |  |  |  | DATE_TO |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |
| COMPONENT_USAGE | VARCHAR2 | 30 |  |  | COMPONENT_USAGE |
| MULTIPLE_COMPONENTS | VARCHAR2 | 30 |  |  | MULTIPLE_COMPONENTS |
| SALARY_AMOUNT | NUMBER |  |  |  | SALARY_AMOUNT |
| CURRENCY_CODE | VARCHAR2 | 20 |  |  | CURRENCY_CODE |
| SALARY_FACTOR | NUMBER |  |  |  | SALARY_FACTOR |
| ANNUAL_FT_SALARY | NUMBER |  |  |  | ANNUAL_FT_SALARY |
| ANNUAL_SALARY | NUMBER |  |  |  | ANNUAL_SALARY |
| NEXT_SAL_REVIEW_DATE | DATE |  |  |  | NEXT_SAL_REVIEW_DATE |
| COPY_STATUS | VARCHAR2 | 30 |  |  | COPY_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_BACKUP_N1 | Non Unique | Default | ASSIGNMENT_ID, DATE_FROM |
| CMP_SALARY_BACKUP_N2 | Non Unique | Default | PERSON_ID, ASSIGNMENT_ID |
| CMP_SALARY_BACKUP_U1 | Unique | Default | SALARY_BACKUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
