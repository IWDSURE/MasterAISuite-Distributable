# CMP_CWB_FEEDBACK

Stores feedback provided by managers for a compensation plan period including product rating and answers to questions.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbfeedback-22659.html#cmpcwbfeedback-22659](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbfeedback-22659.html#cmpcwbfeedback-22659)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_FEEDBACK_PK | FEEDBACK_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_RESPONSE_ID | NUMBER |  | 18 | Yes | FEEDBACK_RESPONSE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| FEEDBACK_ID | NUMBER |  | 18 | Yes | FEEDBACK_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| FEEDBACK_DATE | DATE |  |  | Yes | FEEDBACK_DATE |
| FEEDBACK_RATING | VARCHAR2 | 30 |  |  | FEEDBACK_RATING |
| FEEDBACK_ANSWER1 | VARCHAR2 | 1000 |  |  | FEEDBACK_ANSWER1 |
| FEEDBACK_ANSWER2 | VARCHAR2 | 1000 |  |  | FEEDBACK_ANSWER2 |
| FEEDBACK_ANSWER3 | VARCHAR2 | 1000 |  |  | FEEDBACK_ANSWER3 |
| FEEDBACK_ANSWER4 | VARCHAR2 | 1000 |  |  | FEEDBACK_ANSWER4 |
| FEEDBACK_ANSWER5 | VARCHAR2 | 1000 |  |  | FEEDBACK_ANSWER5 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_FEEDBACK_N1 | Non Unique | Default | FEEDBACK_ID |
| CMP_CWB_FEEDBACK_N2 | Non Unique | Default | PERSON_EVENT_ID |
| CMP_CWB_FEEDBACK_N3 | Non Unique | Default | PERIOD_ID, PLAN_ID |
| CMP_CWB_FEEDBACK_PK | Unique | Default | FEEDBACK_RESPONSE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
