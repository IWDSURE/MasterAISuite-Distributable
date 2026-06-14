# ANC_PER_COVR_SUB_BAL

Table to capture multicarry over values

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpercovrsubbal-26032.html#ancpercovrsubbal-26032](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpercovrsubbal-26032.html#ancpercovrsubbal-26032)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_COVR_SUB_BAL_PK | ANC_PER_COVR_SUB_BAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANC_PER_COVR_SUB_BAL_ID | NUMBER |  | 18 | Yes | Primary Key |
| PER_ACRL_ENTRY_DTL_ID | NUMBER |  | 18 |  | Foreign key of accrual entry details ID |
| PERSON_ID | NUMBER |  | 18 | Yes | Person ID |
| PROCD_DATE | DATE |  |  | Yes | Date of entry created |
| PER_PLAN_ENRT_ID | NUMBER |  | 18 | Yes | Plan enrollment ID |
| TYPE | VARCHAR2 | 30 |  | Yes | COVR/COVR_ADJ/PREVCOVR type |
| COVR_PLAN_TERM | VARCHAR2 | 10 |  | Yes | COVR or adjust year of entry |
| EXPIRATION_DATE | DATE |  |  | Yes | Expiration date of the type |
| ORIGINAL_COVR_VALUE | NUMBER |  |  | Yes | Total value |
| REMAINING_COVR_VALUE | NUMBER |  |  |  | Total REMAINING from the bucket. Based on accrual run and the transaction, REMAINING column will be updated. |
| PARENT_REF_ID | NUMBER |  | 18 |  | Parent Covr Ref Id FOR prevcovr record |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_COVR_SUB_BAL_N1 | Non Unique | Default | PER_PLAN_ENRT_ID |
| ANC_PER_COVR_SUB_BAL_U1 | Unique | Default | ANC_PER_COVR_SUB_BAL_ID |
| ANC_PER_COVR_SUB_BAL_U2 | Unique | Default | PER_ACRL_ENTRY_DTL_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
