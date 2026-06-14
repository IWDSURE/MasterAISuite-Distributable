# ANC_PER_ACCRUAL_ENTRIES

This table holds information of  the person accruals balances.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperaccrualentries-5111.html#ancperaccrualentries-5111](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperaccrualentries-5111.html#ancperaccrualentries-5111)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ACCRUAL_ENTRIES_PK | PER_ACCRUAL_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ACCRUAL_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ACCRUAL_ENTRY_ID |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | ESS_REQUEST_ID |
| FIRST_LAST_PRD_IN_PL_TERM | VARCHAR2 | 20 |  |  | FIRST OR LAST PERIOD IN PLAN TERM |
| WORK_TERM_ASG_ID | NUMBER |  | 18 |  | WORK_TERM_ASG_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ACCRUAL_PERIOD | DATE |  |  | Yes | ACCRUAL_PERIOD |
| PRD_OF_SVC_ID | NUMBER |  | 18 | Yes | PRD_OF_SVC_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |
| BEGIN_BAL | NUMBER |  |  | Yes | BEGIN_BAL |
| ACCRUED | NUMBER |  |  | Yes | ACCRUED |
| USED | NUMBER |  |  | Yes | USED |
| END_BAL | NUMBER |  |  | Yes | END_BAL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identier |
| PER_PLAN_ENRT_ID | NUMBER |  | 18 |  | Person plan enrollment identifier |
| RPT_PERIOD_ID | NUMBER |  | 18 |  | Store the PAYROLL_ID from PAY_TIME_PERIODS table Or REPEATING_TM_PERIOD_ID from HWM_RP_TM_RESOLVED table |
| PAYROLL_MAPPING_ID | NUMBER |  | 18 |  | payroll mapping id |
| PAYROLL_STATUS | VARCHAR2 | 32 |  |  | Payroll transfer/integration status |
| RATE_DEFINITION_ID | NUMBER |  | 18 |  | To store payroll rate definition id. Default value will be -1 |
| STATUS | VARCHAR2 | 30 |  |  | To indicate the status (active or inactive) of accrual entry. Default value will be 'A' |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ACCRUAL_ENTRIES_N1 | Non Unique | Default | WORK_TERM_ASG_ID, PLAN_ID, ACCRUAL_PERIOD |
| ANC_PER_ACCRUAL_ENTRIES_N2 | Non Unique | Default | PERSON_ID, PLAN_ID, ACCRUAL_PERIOD |
| ANC_PER_ACCRUAL_ENTRIES_N3 | Non Unique | Default | PERSON_EVENT_ID |
| ANC_PER_ACCRUAL_ENTRIES_N4 | Non Unique | Default | PER_PLAN_ENRT_ID |
| ANC_PER_ACCRUAL_ENTRIES_U1 | Unique | FUSION_TS_TX_DATA | PER_ACCRUAL_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
