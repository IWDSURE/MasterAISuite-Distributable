# ANC_PER_ABS_PLAN_ENTRIES

This table holds information of  the person absence plan entries.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsplanentries-7981.html#ancperabsplanentries-7981](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsplanentries-7981.html#ancperabsplanentries-7981)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_PLAN_ENTRIES_PK | PER_ABS_PLAN_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_PLAN_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABS_PLAN_ENTRY_ID |
| PER_ABS_PLN_SUMM_ENTRY_ID | NUMBER |  | 18 |  | Plan summary entry id |
| START_DATETIME | TIMESTAMP |  |  |  | StartDateTime - Denotes Payment Date or Earned Date |
| END_DATETIME | TIMESTAMP |  |  |  | EndDateTime |
| FLSA_DATE | TIMESTAMP |  |  |  | Denotes FLSA Date or Overtime date |
| TM_REC_ID | NUMBER |  | 18 |  | TM_REC_ID |
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABS_TYPE_ENTRY_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ABSENCE_PLAN_ID | NUMBER |  | 18 | Yes | ABSENCE_PLAN_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| START_TIME | VARCHAR2 | 30 |  |  | START_TIME |
| END_TIME | VARCHAR2 | 30 |  |  | END_TIME |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| SCHEDULED_UNITS | NUMBER |  |  |  | SCHEDULED_UNITS |
| ABS_UNITS | NUMBER |  |  | Yes | ABS_UNITS |
| ABSENCE_PAY_FACTOR | NUMBER |  |  | Yes | ABSENCE_PAY_FACTOR |
| RATE_DEFINITION_ID | NUMBER |  |  |  | RATE_DEFINITION_ID |
| HEADER_ID | NUMBER |  |  |  | HEADER_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 |  | References ANC_PERSON_ABS_ENTRIES.PER_ABSENCE_ENTRY_ID |
| QUALIFICATION_DATE | DATE |  |  |  | Qualification date |
| ENTITLEMENT_DATE | DATE |  |  |  | Entitlement date |
| PER_ACCRUAL_ENTRY_DTL_ID | NUMBER |  | 18 |  | PER_ACCRUAL_ENTRY_DTL_ID |
| PAY_FACTOR_WITHOUT_OVERRIDE | NUMBER |  |  |  | PAY_FACTOR_WITHOUT_OVERRIDE |
| AMOUNT | NUMBER |  |  |  | To store payment amount at assignment level corresponding to case breakdown  -UK loc |
| PER_CASE_BREAKDOWN_ID | NUMBER |  | 18 |  | To map assignment level breakdown corresponding to case breakdown |
| CASE_ID | NUMBER |  | 18 |  | CASE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_PLAN_ENTRIES_N1 | Non Unique | Default | PER_ABS_TYPE_ENTRY_ID |
| ANC_PER_ABS_PLAN_ENTRIES_N2 | Non Unique | Default | ASSIGNMENT_ID, ABSENCE_PLAN_ID |
| ANC_PER_ABS_PLAN_ENTRIES_N3 | Non Unique | Default | PERSON_ID, ABSENCE_PLAN_ID |
| ANC_PER_ABS_PLAN_ENTRIES_N4 | Non Unique | Default | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_PLAN_ENTRIES_N5 | Non Unique | Default | PER_ABS_PLN_SUMM_ENTRY_ID |
| ANC_PER_ABS_PLAN_ENTRIES_N6 | Non Unique | Default | PER_ACCRUAL_ENTRY_DTL_ID |
| ANC_PER_ABS_PLAN_ENTRIES_N7 | Non Unique | Default | CASE_ID |
| ANC_PER_ABS_PLAN_ENTRIES_U1 | Unique | FUSION_TS_TX_DATA | PER_ABS_PLAN_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
