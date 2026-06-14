# HWR_WLNS_ASSESSMENT

This table will be used to store wellness assessments.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsassessment-14599.html#hwrwlnsassessment-14599](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsassessment-14599.html#hwrwlnsassessment-14599)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_ASSESSMENT_PK | USER_ID, QUESTIONNAIRE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ID | VARCHAR2 | 500 |  | Yes | This is the wellness user id. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the wellness active questionnaire id. |
| LAST_ASSESSMENT_DATE | TIMESTAMP |  |  | Yes | Corresponds to the ASSESSMENT_SCORE field value change. |
| ASSESSMENT_CALC_RULE_CODE | VARCHAR2 | 30 |  |  | This column stores the wellness questionnaire calculation rule for calculating overall score. |
| ASSESSMENT_SCORE | NUMBER |  | 20 |  | This column stores the wellness assessment score for the questionnaire of the wellness user. |
| ASSESSMENT_TOTAL_SCORE | NUMBER |  | 20 |  | This column stores the wellness questionnaire total score. |
| SCORED_FLAG | VARCHAR2 | 30 |  |  | Indicates questionnaire is a scored questionnaire. |
| WLNS_ASSESS_ATTR_1 | VARCHAR2 | 100 |  |  | WLNS_ASSESS_ATTR_1. This is the extra attribute in case if needed. |
| WLNS_ASSESS_ATTR_2 | VARCHAR2 | 100 |  |  | WLNS_ASSESS_ATTR_2. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_ASSESSMENT_U1 | Unique | Default | USER_ID, QUESTIONNAIRE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
