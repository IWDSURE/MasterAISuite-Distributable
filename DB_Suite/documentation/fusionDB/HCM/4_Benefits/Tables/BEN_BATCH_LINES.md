# BEN_BATCH_LINES

BEN_BATCH_LINES contains information, related to processing benefits data .

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchlines-14756.html#benbatchlines-14756](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchlines-14756.html#benbatchlines-14756)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_LINES_PK | BATCH_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_LINE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BATCH_HEADER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_BATCH_HEADER. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business group. |
| STATUS | VARCHAR2 | 250 |  |  | Line status. |
| ERROR_MESSAGE | VARCHAR2 | 2000 |  |  | Error message. |
| ENROLLMENT_TYPE | VARCHAR2 | 250 |  | Yes | Enrollment type. |
| PRTT_PERSON_NUM | VARCHAR2 | 30 |  |  | Participant person number. |
| PGM_NAME | VARCHAR2 | 240 |  |  | Program name. |
| PL_NAME | VARCHAR2 | 240 |  |  | Plan name. |
| DEENROLL_PL_NAME | VARCHAR2 | 240 |  |  | De-enroll plan. |
| OPT_NAME | VARCHAR2 | 240 |  |  | Option name. |
| DEENROLL_OPT_NAME | VARCHAR2 | 240 |  |  | De-enroll option. |
| LER_NAME | VARCHAR2 | 240 |  | Yes | Life event name. |
| LF_EVT_OCRD_DT | DATE |  |  | Yes | Life event occured date. |
| EFFECTIVE_DATE | DATE |  |  | Yes | Effective date. |
| CREATE_PTNL_FLAG | VARCHAR2 | 10 |  |  | Create potential flag. |
| PRTT_LAST_NAME | VARCHAR2 | 150 |  | Yes | Participant last name. |
| PRTT_FIRST_NAME | VARCHAR2 | 150 |  | Yes | Participant first name. |
| DPNT_LAST_NAME | VARCHAR2 | 150 |  |  | Dependent last name. |
| DPNT_FIRST_NAME | VARCHAR2 | 150 |  |  | Dependent first name. |
| BNF_LAST_NAME | VARCHAR2 | 150 |  |  | Beneficiary last name. |
| BNF_FIRST_NAME | VARCHAR2 | 150 |  |  | Beneficiary first name. |
| BENEFIT_RELATION | VARCHAR2 | 240 |  | Yes | Benefit relation name. |
| RATE_VALUE | NUMBER |  | 18 |  | Rate value. |
| BNFT_VALUE | NUMBER |  | 18 |  | Coverage amount. |
| DEENROLL_BNFT_VALUE | NUMBER |  | 18 |  | De-enroll coverage amount. |
| BNF_AMOUNT | NUMBER |  |  |  | Beneficiary amount. |
| BNF_PCT | NUMBER |  | 18 |  | Beneficiary percentage. |
| PRTT_CVG_START_DT | DATE |  |  |  | Participant coverage start date. |
| PRTT_ORIG_ENRT_DT | DATE |  |  |  | Participant original enrollment date. |
| DPNT_CVG_START_DT | DATE |  |  |  | Dependent coverage start date. |
| BNF_START_DT | DATE |  |  |  | Beneficiary start date. |
| CLOSE_LER_FLAG | VARCHAR2 | 10 |  |  | Close life event flag. |
| CLOSE_LER_EFFECTIVE_DATE | DATE |  |  |  | Close life event effective date. |
| BBL_TXT_VAL_1 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_2 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_3 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_4 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_5 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_6 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_7 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_8 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_9 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_TXT_VAL_10 | VARCHAR2 | 240 |  |  | Additional batch lines text information. |
| BBL_NUM_VAL_1 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_2 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_3 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_4 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_5 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_6 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_7 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_8 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_9 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_NUM_VAL_10 | NUMBER |  | 18 |  | Additional batch lines numeric information. |
| BBL_DT_VAL_1 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_2 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_3 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_4 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_5 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_6 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_7 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_8 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_9 | DATE |  |  |  | Additional batch lines date information. |
| BBL_DT_VAL_10 | DATE |  |  |  | Additional batch lines date information. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BATCH_LINES_N1 | Non Unique | FUSION_TS_TX_IDX | BATCH_HEADER_ID |
| BEN_BATCH_LINES_N2 | Non Unique | FUSION_TS_TX_IDX | PRTT_PERSON_NUM, LF_EVT_OCRD_DT |
| BEN_BATCH_LINES_PK | Unique | FUSION_TS_TX_IDX | BATCH_LINE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
