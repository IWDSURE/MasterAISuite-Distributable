# CMP_SALARY_EXPORT

Salary Export table holds details of salary data bases on the parameters the user entered on the salary export page.  The data is stored here for use when exporting to excel.  After a set time the data will be purged.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalaryexport-21515.html#cmpsalaryexport-21515](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalaryexport-21515.html#cmpsalaryexport-21515)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_EXPORT_PK | SALARY_EXPORT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SALARY_EXPORT_ID | NUMBER |  | 18 | Yes | Table key |
| BATCH_ID | NUMBER |  | 18 | Yes | Batch id of the run |
| BATCH_CREATION_DATE | DATE |  |  | Yes | Batch Creattion Date |
| SALARY_ID | NUMBER |  | 18 | Yes | Salary Id |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment Id |
| ASSIGNMENT_NUMBER | VARCHAR2 | 50 |  |  | Assignment Number |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| WORKER_NUMBER | VARCHAR2 | 30 |  |  | Worker Number |
| PERSON_ID | NUMBER |  | 18 |  | Person Id |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | Person Number |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Business Unit Id |
| BUSINESS_UNIT_NAME | VARCHAR2 | 300 |  |  | Business Unit Name |
| SALARY_AMOUNT | NUMBER |  |  |  | Salary Amount |
| ANNUALIZED_SALARY | NUMBER |  |  |  | Annualized Salary |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | Code |
| SALARY_START_DATE | DATE |  |  |  | Sal Change Date |
| SALARY_END_DATE | DATE |  |  |  | Sal End date |
| FTE | NUMBER |  |  |  | Fte |
| REVIEW_DATE | DATE |  |  |  | Review Date |
| LATEST_HIRE_DATE | DATE |  |  |  | Hire date |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | Sal basis id |
| SALARY_BASIS_CODE | VARCHAR2 | 30 |  |  | Sal basis code |
| RATE_MIN | NUMBER |  |  |  | Min rate |
| RATE_MID | NUMBER |  |  |  | Mid rate |
| RATE_MAX | NUMBER |  |  |  | Max Rate |
| RATE_ANNUALIZATION_FACTOR | NUMBER |  |  |  | Rate Ann factor |
| SALARY_ANNUALIZATION_FACTOR | NUMBER |  |  |  | Sal Ann factor |
| SALARY_BASIS_NAME | VARCHAR2 | 300 |  |  | Sal Basis name |
| SALARY_BASIS_FREQUENCY | VARCHAR2 | 80 |  |  | Frequency |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Entity Id |
| LEGAL_EMPLOYER | VARCHAR2 | 300 |  |  | Employer |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Dept Id |
| DEPARTMENT_NAME | VARCHAR2 | 300 |  |  | Dept. name |
| POSITION_ID | NUMBER |  | 18 |  | Position Id |
| POSITION_NAME | VARCHAR2 | 300 |  |  | Position Name |
| POSITION_CODE | VARCHAR2 | 30 |  |  | Position Code |
| EMP_NAME | VARCHAR2 | 300 |  |  | Employee Name |
| MGR_NAME | VARCHAR2 | 300 |  |  | Manager Name |
| JOB_ID | NUMBER |  | 18 |  | Job Id |
| JOB_CODE | VARCHAR2 | 30 |  |  | Job Code |
| JOB_NAME | VARCHAR2 | 300 |  |  | Job Name |
| JOB_FAMILY_NAME | VARCHAR2 | 300 |  |  | Job Family Name |
| GRADE_ID | NUMBER |  | 18 |  | Grade Id |
| GRADE_CODE | VARCHAR2 | 30 |  |  | Grade Code |
| GRADE_NAME | VARCHAR2 | 300 |  |  | Grade Name |
| LOCATION_ID | NUMBER |  | 18 |  | Location Id |
| LOCATION_NAME | VARCHAR2 | 240 |  |  | Location Name |
| ZONE_TYPE_ID | NUMBER |  |  |  | Zone Type Id |
| ZONE_TYPE_NAME | VARCHAR2 | 4000 |  |  | Zone Type Name |
| ZONE_ID | NUMBER |  |  |  | Zone Id |
| ZONE_NAME | VARCHAR2 | 4000 |  |  | Zone Name |
| EXCHANGE_RATE | NUMBER |  |  |  | Exchange Rate |
| RANGE_POSITION | NUMBER |  |  |  | Range Pos |
| COMPA_RATIO | NUMBER |  |  |  | Compa ratio |
| QUARTILE | VARCHAR2 | 30 |  |  | Quartile |
| EMAIL_ADDRESS | VARCHAR2 | 150 |  |  | Email |
| EMPLOYMENT_CATEGORY | VARCHAR2 | 80 |  |  | Emp Cat |
| ACTION_ID | NUMBER |  | 18 |  | Action Id |
| ACTION_REASON_ID | NUMBER |  | 18 |  | Action Reason Id |
| ASSIGNMENT_STATUS | VARCHAR2 | 80 |  |  | Assgn Status |
| ASSIGNMENT_STATUS_TYPE | VARCHAR2 | 30 |  |  | Assng Status Type |
| YEARS_IN_GRADE | NUMBER |  | 18 |  | years in grade |
| SALARY_COMPONENT1_ID | NUMBER |  | 18 |  | Sal Comp 1 |
| COMPONENT1_NAME | VARCHAR2 | 300 |  |  | comp 1 name |
| COMPONENT1_AMOUNT | NUMBER |  |  |  | comp 1 amount |
| COMPONENT1_REASON_CODE | VARCHAR2 | 30 |  |  | comp 1 reason code |
| SALARY_COMPONENT2_ID | NUMBER |  | 18 |  | comp 2 |
| COMPONENT2_NAME | VARCHAR2 | 300 |  |  | comp 2 name |
| COMPONENT2_AMOUNT | NUMBER |  |  |  | comp 2 amount |
| COMPONENT2_REASON_CODE | VARCHAR2 | 30 |  |  | comp 2 reason |
| SALARY_COMPONENT3_ID | NUMBER |  | 18 |  | comp 3 id |
| COMPONENT3_NAME | VARCHAR2 | 300 |  |  | comp 3 name |
| COMPONENT3_AMOUNT | NUMBER |  |  |  | comp 3 amount |
| COMPONENT3_REASON_CODE | VARCHAR2 | 30 |  |  | comp 3 reason |
| SALARY_COMPONENT4_ID | NUMBER |  | 18 |  | comp 4 id |
| COMPONENT4_NAME | VARCHAR2 | 300 |  |  | comp 4 name |
| COMPONENT4_AMOUNT | NUMBER |  |  |  | comp 4 amount |
| COMPONENT4_REASON_CODE | VARCHAR2 | 30 |  |  | comp 4 reason |
| SALARY_COMPONENT5_ID | NUMBER |  | 18 |  | comp 5 id |
| COMPONENT5_NAME | VARCHAR2 | 300 |  |  | comp 5 name |
| COMPONENT5_AMOUNT | NUMBER |  |  |  | comp 5 amount |
| COMPONENT5_REASON_CODE | VARCHAR2 | 30 |  |  | comp 5 reason |
| COMPONENTS_ENABLED | VARCHAR2 | 5 |  |  | enabled |
| READ_ONLY_FORMAT | VARCHAR2 | 5 |  |  | read only |
| IMPORT_ENABLED | VARCHAR2 | 5 |  |  | import enabled |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element Type |
| PRIMARY_EMAIL_ID | NUMBER |  | 18 |  | Email Id |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Job Family Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_EXPORT_N1 | Non Unique | Default | BATCH_CREATION_DATE |
| CMP_SALARY_EXPORT_N2 | Non Unique | Default | SALARY_ID, BATCH_ID, ASSIGNMENT_ID |
| CMP_SALARY_EXPORT_PK1 | Unique | Default | SALARY_EXPORT_ID, BATCH_ID |
| CMP_SALARY_EXPORT_U2 | Unique | Default | BATCH_ID, SALARY_EXPORT_ID, SALARY_START_DATE |
| CMP_SALARY_EXPORT_U3 | Unique | Default | SALARY_EXPORT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
