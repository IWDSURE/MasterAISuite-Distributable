# ANC_PER_PLAN_ENROLLMENT_

This table holds information of  the person absence plan enrollments.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperplanenrollment-16839.html#ancperplanenrollment-16839](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperplanenrollment-16839.html#ancperplanenrollment-16839)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_PLAN_ENROLLMENT_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PER_PLAN_ENRT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_PLAN_ENRT_ID | NUMBER |  | 18 | Yes | PER_PLAN_ENRT_ID |
| WORK_TERM_ASG_ID | NUMBER |  | 18 |  | WORK_TERM_ASG_ID |
| LAST_ACCRUAL_RUN | DATE |  |  |  | LAST_ACCRUAL_RUN |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| PRD_OF_SVC_ID | NUMBER |  | 18 |  | PRD_OF_SVC_ID |
| PER_EVENT_ID | NUMBER |  | 18 |  | PER_EVENT_ID |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| ENRT_ST_DT | DATE |  |  |  | ENRT_ST_DT |
| ENRT_END_DT | DATE |  |  |  | ENRT_END_DT |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| WAIT_PERIOD_DUR_UOM | VARCHAR2 | 30 |  |  | Waiting period duration unit of measure |
| WAIT_PERIOD_DUR_UNITS | NUMBER |  |  |  | Waiting period duration units |
| STATUS | VARCHAR2 | 30 |  |  | Plan enrollment status |
| OPERATION_TYPE | VARCHAR2 | 30 |  |  | OPERATION_TYPE |
| CEILING_AMT | NUMBER |  |  |  | Override donation ceiling amount |
| RECIPIENT_ALIAS | VARCHAR2 | 240 |  |  | Alias |
| SOURCE_ENRT_ID | NUMBER |  | 18 |  | Source accrual plan enrollment identifier |
| PAYROLL_MAPPING_ID | NUMBER |  | 18 |  | payroll mapping id |
| PAYROLL_STATUS | VARCHAR2 | 32 |  |  | payroll transfer/integration status |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_PLAN_ENROLLMENT_N1_ | Non Unique | DEFAULT | PER_PLAN_ENRT_ID |
| ANC_PER_PLAN_ENROLLMENT_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PER_PLAN_ENRT_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
