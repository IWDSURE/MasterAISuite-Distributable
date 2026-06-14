# ANC_PER_ACRL_ENTRY_DTLS_

This table holds information of  the person accrual entry details.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperacrlentrydtls-31499.html#ancperacrlentrydtls-31499](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperacrlentrydtls-31499.html#ancperacrlentrydtls-31499)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ACRL_ENTRY_DTLS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PER_ACCRUAL_ENTRY_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ACCRUAL_ENTRY_DTL_ID | NUMBER |  | 18 | Yes | PER_ACCRUAL_ENTRY_DTL_ID |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | ESS_REQUEST_ID |
| BEN_DISB_PROC_ERROR | VARCHAR2 | 1 |  |  | BEN_DISB_PROC_ERROR |
| ELECTION_DT | DATE |  |  |  | ELECTION_DT |
| REPROCESS_REQUIRED | VARCHAR2 | 1 |  |  | REPROCESS_REQUIRED |
| ELECTED_AMT | NUMBER |  |  |  | ELECTED_AMT |
| BEN_DISB_PROCESSED | VARCHAR2 | 1 |  |  | BEN_DISB_PROCESSED |
| BEN_DISB_FIXED | VARCHAR2 | 1 |  |  | BEN_DISB_FIXED |
| ANC_PER_BEN_ELCTD_DISB_ID | NUMBER |  | 18 |  | ANC_PER_BEN_ELCTD_DISB_ID |
| COVR_ENTRY_DTL_ID | NUMBER |  | 18 |  | Self reference accrualEntryDtlId with the corresponding COVR row. |
| PER_ACCRUAL_ENTRY_ID | NUMBER |  | 18 |  | PER_ACCRUAL_ENTRY_ID |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| VALUE | NUMBER |  |  |  | VALUE |
| TYPE | VARCHAR2 | 30 |  |  | TYPE |
| ADJUSTMENT_REASON | VARCHAR2 | 30 |  |  | ADJUSTMENT_REASON |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_ID | NUMBER |  | 18 |  | Person Identifier |
| PL_ID | NUMBER |  | 18 |  | PL_ID |
| PROCD_DATE | DATE |  |  |  | Processed date |
| PER_EVENT_ID | NUMBER |  | 18 |  | Person Event Id |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | Legal Employer |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment Identifier |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 |  | references ANC_PER_ABS_ENTRIES.PER_ABSENCE_ENTRY_ID |
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 |  | PER_ABS_TYPE_ENTRY_ID |
| PER_PLAN_ENRT_ID | NUMBER |  | 18 |  | PER_PLAN_ENRT_ID |
| WORK_TERM_ASG_ID | NUMBER |  | 18 |  | WORK_TERM_ASG_ID |
| VOIDED_ACRL | VARCHAR2 | 30 |  |  | VOIDED ACCRUALS |
| SOURCE | VARCHAR2 | 10 |  |  | SOURCE |
| VOIDED_BY | VARCHAR2 | 64 |  |  | VOIDED_BY |
| VOIDED_DATETIME | TIMESTAMP |  |  |  | VOIDED_DATETIME |
| TIME_CARD_ID | NUMBER |  | 18 |  | Compensatory time record from T&L when pushed from T&L |
| TIME_CARD_VERSION | NUMBER |  | 9 |  | comp time record version from T$L |
| EXP_DT | DATE |  |  |  | Expiration date of the compensatory time |
| ADJ_EXP_DT | DATE |  |  |  | Manually adjusted Expiration date |
| ADJ_EXP_DT_REASON_CD | VARCHAR2 | 30 |  |  | Adjustment expiration reason code |
| REFERENCE_DATE | DATE |  |  |  | Actual earned date passed from Time/External. If vesting rule configured on plan setup, this column will store the earned date. PROCD_DATE will store the vesting date. |
| COMP_ADJ_REASON_CD | VARCHAR2 | 2000 |  |  | Manual adjustment reason |
| REF_ID | NUMBER |  | 18 |  | reference for csh and transfer |
| EXP_DISB_PAY_PUSH | VARCHAR2 | 1 |  |  | Determine if expiration disbursement is pushed to payroll (Y is pushed to payroll) |
| LOADER_REF_ID | NUMBER |  | 18 |  | References to the accrual entry dtl id row populated from loader |
| RECIPIENT_PLAN_ENRT_ID | NUMBER |  | 18 |  | Recipient's Enrollment ID
Only Donor's record will store value in this column |
| ANC_PER_ACRL_ENTRY_DTLS_ALTCD | VARCHAR2 | 240 |  |  | Approval flow unique key |
| USER_MODE | VARCHAR2 | 10 |  |  | The role who submitted the approval request |
| APPROVAL_STATUS_CD | VARCHAR2 | 30 |  |  | Approval status code |
| APPROVAL_SUBMITTED_DATE | DATE |  |  |  | Approval submission date |
| PROC_STATUS_CD | VARCHAR2 | 30 |  |  | Processing result status code |
| PAYMENT_PERCENTAGE | NUMBER |  |  |  | Save payment percentage defined in plan setup or returned from fast formula |
| ARCL_ENTRY_DTL_REC_SOURCE | VARCHAR2 | 10 |  |  | Store the source info if it's coming from Mobile UX. |
| PAYROLL_MAPPING_ID | NUMBER |  | 18 |  | payroll mapping id |
| PAYROLL_STATUS | VARCHAR2 | 32 |  |  | payroll mapping integration status |
| DISB_FROM_COVR_FIRST | VARCHAR2 | 30 |  |  | Confirm if Disbursement is consume from availab
      le carryover first |
| RATE_DEFINITION_ID | NUMBER |  | 18 |  | To store payroll rate definition id. Default value will be -1 |
| STATUS | VARCHAR2 | 30 |  |  | To indicate the status (active or inactive) of accrual entry detail. Default value will be 'A' |
| PLAN_TERM | VARCHAR2 | 10 |  |  | PREVCOVER year of entry |
| DON_POOL_PLAN_ID | NUMBER |  | 18 |  | To store donation pool plan id. |
| DON_TYPE | VARCHAR2 | 30 |  |  | Donation Type. (Individual or Pool) |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ACRL_ENTRY_DTLS_N1_ | Non Unique | ANC_PER_ACRL_ENTRY_DTLS_N1_ | PER_ACCRUAL_ENTRY_DTL_ID |
| ANC_PER_ACRL_ENTRY_DTLS_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PER_ACCRUAL_ENTRY_DTL_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
