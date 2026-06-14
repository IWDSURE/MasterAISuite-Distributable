# CMP_CWB_SUMMARY

Stores summarized information about the different rates used in the plan period. This information is used in self-service pages for reporting purposes. For example, total salary, total supplemental earnings, etc. It also holds summarized information of budget pools.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsummary-26023.html#cmpcwbsummary-26023](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsummary-26023.html#cmpcwbsummary-26023)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_SUMMARY_PK | SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SUMMARY_ID | NUMBER |  | 18 | Yes | SUMMARY_ID | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |  |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |  |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |  |
| COMPONENT_ID | NUMBER |  | 18 | Yes | COMPONENT_ID |  |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID | Active |
| POOL_ID | NUMBER |  | 18 |  | POOL_ID |  |
| STATUS | VARCHAR2 | 30 |  |  | STATUS | Active |
| TOTAL_COUNT_DIRECT | NUMBER |  | 18 |  | TOTAL_COUNT_DIRECT |  |
| TOTAL_COUNT_ALL | NUMBER |  | 18 |  | TOTAL_COUNT_ALL |  |
| ELIG_COUNT_DIRECT | NUMBER |  | 18 |  | ELIG_COUNT_DIRECT | Active |
| ELIG_COUNT_ALL | NUMBER |  | 18 |  | ELIG_COUNT_ALL | Active |
| EMP_RECV_COUNT_DIRECT | NUMBER |  | 18 |  | EMP_RECV_COUNT_DIRECT | Active |
| EMP_RECV_COUNT_ALL | NUMBER |  | 18 |  | EMP_RECV_COUNT_ALL | Active |
| ELIG_SAL_VAL_DIRECT | NUMBER |  |  |  | ELIG_SAL_VAL_DIRECT | Active |
| ELIG_SAL_VAL_ALL | NUMBER |  |  |  | ELIG_SAL_VAL_ALL | Active |
| WS_VAL_DIRECT | NUMBER |  |  |  | WS_VAL_DIRECT | Active |
| WS_VAL_ALL | NUMBER |  |  |  | WS_VAL_ALL | Active |
| WS_BDGT_VAL_DIRECT | NUMBER |  |  |  | WS_BDGT_VAL_DIRECT | Active |
| WS_BDGT_VAL_ALL | NUMBER |  |  |  | WS_BDGT_VAL_ALL | Active |
| WS_BDGT_ISS_VAL_DIRECT | NUMBER |  |  |  | WS_BDGT_ISS_VAL_DIRECT | Active |
| WS_BDGT_ISS_VAL_ALL | NUMBER |  |  |  | WS_BDGT_ISS_VAL_ALL | Active |
| EMP_BDGT_VAL_DIRECT | NUMBER |  |  |  | EMP_BDGT_VAL_DIRECT |  |
| EMP_BDGT_VAL_ALL | NUMBER |  |  |  | EMP_BDGT_VAL_ALL |  |
| BDGT_VAL_DIRECT | NUMBER |  |  |  | BDGT_VAL_DIRECT | Active |
| BDGT_ISS_VAL_DIRECT | NUMBER |  |  |  | BDGT_ISS_VAL_DIRECT | Active |
| REC_VAL_DIRECT | NUMBER |  |  |  | REC_VAL_DIRECT | Active |
| REC_VAL_ALL | NUMBER |  |  |  | REC_VAL_ALL | Active |
| REC_MN_VAL_DIRECT | NUMBER |  |  |  | REC_MN_VAL_DIRECT | Active |
| REC_MN_VAL_ALL | NUMBER |  |  |  | REC_MN_VAL_ALL | Active |
| REC_MX_VAL_DIRECT | NUMBER |  |  |  | REC_MX_VAL_DIRECT | Active |
| REC_MX_VAL_ALL | NUMBER |  |  |  | REC_MX_VAL_ALL | Active |
| MISC1_VAL_DIRECT | NUMBER |  |  |  | MISC1_VAL_DIRECT | Active |
| MISC1_VAL_ALL | NUMBER |  |  |  | MISC1_VAL_ALL | Active |
| MISC2_VAL_DIRECT | NUMBER |  |  |  | MISC2_VAL_DIRECT | Active |
| MISC2_VAL_ALL | NUMBER |  |  |  | MISC2_VAL_ALL | Active |
| MISC3_VAL_DIRECT | NUMBER |  |  |  | MISC3_VAL_DIRECT | Active |
| MISC3_VAL_ALL | NUMBER |  |  |  | MISC3_VAL_ALL | Active |
| MISC4_VAL_DIRECT | NUMBER |  |  |  | MISC4_VAL_DIRECT | Active |
| MISC4_VAL_ALL | NUMBER |  |  |  | MISC4_VAL_ALL | Active |
| MISC5_VAL_DIRECT | NUMBER |  |  |  | MISC5_VAL_DIRECT | Active |
| MISC5_VAL_ALL | NUMBER |  |  |  | MISC5_VAL_ALL | Active |
| MISC6_VAL_DIRECT | NUMBER |  |  |  | MISC6_VAL_DIRECT | Active |
| MISC6_VAL_ALL | NUMBER |  |  |  | MISC6_VAL_ALL | Active |
| TOTAL_RANKED | NUMBER |  | 18 |  | TOTAL_RANKED |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_SUMMARY_N1 | Non Unique | Default | PERSON_EVENT_ID, COMPONENT_ID, POOL_ID |
| CMP_CWB_SUMMARY_N2 | Non Unique | Default | PERSON_ID |
| CMP_CWB_SUMMARY_N3 | Non Unique | Default | PERIOD_ID, PLAN_ID, STATUS |
| CMP_CWB_SUMMARY_PK | Unique | Default | SUMMARY_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
