# ANC_PER_BEN_ELCTD_DISB

CYCLICAL ACCRUAL PLAN BALANCE DISBURSEMENTS

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperbenelctddisb-14208.html#ancperbenelctddisb-14208](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperbenelctddisb-14208.html#ancperbenelctddisb-14208)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_BEN_ELCTD_DISB_PK | ANC_PER_BEN_ELCTD_DISB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANC_PER_BEN_ELCTD_DISB_ID | NUMBER |  | 18 | Yes | ANC_PER_BEN_ELCTD_DISB_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ABSENCE_PLAN_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| ELECTION_DT | DATE |  |  | Yes | ELECTION_DT |
| ELECTED_AMT | NUMBER |  |  | Yes | ELECTION_AMT |
| PAYMENT_DT | DATE |  |  | Yes | PAYMENT_DT |
| BNFT_PL_ID | NUMBER |  | 18 | Yes | BNFT_PL_ID |
| BNFT_ENRT_RSLT_ID | NUMBER |  | 18 | Yes | BNFT_ENRT_RSLT_ID |
| BNFT_PER_IN_LER_ID | NUMBER |  | 18 | Yes | BNFT_PER_IN_LER_ID |
| BNFT_LF_EVT_DT | DATE |  |  | Yes | BNFT_LF_EVT_DT |
| OPERATION | VARCHAR2 | 30 |  | Yes | OPERATION |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PROCESSED_FLAG | VARCHAR2 | 1 |  |  | PROCESSED_FLAG |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_BEN_ELCTD_DISB_N1 | Non Unique | Default | PERSON_ID |
| ANC_PER_BEN_ELCTD_DISB_N2 | Non Unique | Default | ASSIGNMENT_ID |
| ANC_PER_BEN_ELCTD_DISB_U1 | Unique | Default | ANC_PER_BEN_ELCTD_DISB_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
