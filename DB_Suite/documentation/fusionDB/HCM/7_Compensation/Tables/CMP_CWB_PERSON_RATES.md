# CMP_CWB_PERSON_RATES

All worksheet amount rates used in awarding compensation. It holds information  about eligible or ineligible employees depending on setup, for example, for eligible employees eligibility is "Y". It also holds all worksheet rate values, for example, for worksheet amount rate it has worksheet amount minimum value, maximum value, increment value and worksheet value.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersonrates-21086.html#cmpcwbpersonrates-21086](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersonrates-21086.html#cmpcwbpersonrates-21086)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PERSON_RATES_PK | PERSON_EVENT_ID, COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| COMPONENT_ID | NUMBER |  | 18 | Yes | COMPONENT_ID |  |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |  |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |  |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID | Active |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID | Active |
| ELIG_FLAG | VARCHAR2 | 1 |  |  | ELIG_FLAG | Active |
| INELIG_REASON_CODE | VARCHAR2 | 30 |  |  | INELIG_REASON_CODE |  |
| CURRENCY | VARCHAR2 | 30 |  |  | CURRENCY | Active |
| WS_VAL | NUMBER |  |  |  | WS_VAL | Active |
| WS_MIN_VAL | NUMBER |  |  |  | WS_MIN_VAL |  |
| WS_MAX_VAL | NUMBER |  |  |  | WS_MAX_VAL |  |
| ELIG_SAL_VAL | NUMBER |  |  |  | ELIG_SAL_VAL | Active |
| MISC1_VAL | NUMBER |  |  |  | MISC1_VAL | Active |
| MISC2_VAL | NUMBER |  |  |  | MISC2_VAL | Active |
| MISC3_VAL | NUMBER |  |  |  | MISC3_VAL | Active |
| MISC4_VAL | NUMBER |  |  |  | MISC4_VAL | Active |
| MISC5_VAL | NUMBER |  |  |  | MISC5_VAL | Active |
| MISC6_VAL | NUMBER |  |  |  | MISC6_VAL | Active |
| REC_VAL | NUMBER |  |  |  | REC_VAL | Active |
| REC_MIN_VAL | NUMBER |  |  |  | REC_MIN_VAL |  |
| REC_MAX_VAL | NUMBER |  |  |  | REC_MAX_VAL |  |
| EMP_BDGT_VAL | NUMBER |  |  |  | EMP_BDGT_VAL |  |
| EMP_BDGT_MIN_VAL | NUMBER |  |  |  | EMP_BDGT_MIN_VAL |  |
| EMP_BDGT_MAX_VAL | NUMBER |  |  |  | EMP_BDGT_MAX_VAL |  |
| PRIOR_WS_VAL | NUMBER |  |  |  | PRIOR_WS_VAL |  |
| PRIOR_WS_VAL_DATE | DATE |  |  |  | PRIOR_WS_VAL_DATE |  |
| PRIOR_ELIG_SAL_VAL | NUMBER |  |  |  | PRIOR_ELIG_SAL_VAL |  |
| COMP_POSTED_DATE | DATE |  |  |  | COMP_POSTED_DATE |  |
| COMP_POSTING_DATE | DATE |  |  |  | COMP_POSTING_DATE | Active |
| ELIG_OVERRIDE_DATE | DATE |  |  |  | ELIG_OVERRIDE_DATE |  |
| ELIG_OVERRIDE_PERSON_ID | NUMBER |  | 18 |  | ELIG_OVERRIDE_PERSON_ID |  |
| WS_VAL_ORIG_UPD_BY | NUMBER |  | 18 |  | WS_VAL_ORIG_UPD_BY |  |
| WS_VAL_LAST_UPD_DATE | DATE |  |  |  | WS_VAL_LAST_UPD_DATE | Active |
| WS_VAL_LAST_UPD_BY | NUMBER |  | 18 |  | WS_VAL_LAST_UPD_BY | Active |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | ELIGIBILITY_PROFILE_ID |  |
| ELIGIBILITY_PROFILE_REQ_FLAG | VARCHAR2 | 1 |  |  | ELIGIBILITY_PROFILE_REQ_FLAG |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PERSON_RATES_N1 | Non Unique | Default | PERIOD_ID, COMPONENT_ID |
| CMP_CWB_PERSON_RATES_N2 | Non Unique | Default | PLAN_ID, COMPONENT_ID |
| CMP_CWB_PERSON_RATES_N4 | Non Unique | Default | ASSIGNMENT_ID, PLAN_ID, PERIOD_ID, COMPONENT_ID |
| CMP_CWB_PERSON_RATES_PK | Unique | Default | PERSON_EVENT_ID, COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
