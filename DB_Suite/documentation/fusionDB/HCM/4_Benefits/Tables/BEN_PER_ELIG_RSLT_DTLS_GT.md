# BEN_PER_ELIG_RSLT_DTLS_GT

ben_per_elig_rslt_track_dtls holds the eligibility criteria evaluation results for each criteria of the eligibility profile and or the eligibility objects

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpereligrsltdtlsgt-7133.html#benpereligrsltdtlsgt-7133](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpereligrsltdtlsgt-7133.html#benpereligrsltdtlsgt-7133)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_ELIG_RSLT_DTLS_GT_PK | PER_ELIG_RSLT_TRACK_DTLS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ELIG_RSLT_TRACK_DTLS_ID | NUMBER |  | 18 | Yes | Person Eligibility Result Tracking Details Identifier |
| PER_ELIG_RSLT_TRACK_ID | NUMBER |  | 18 | Yes | Person Eligibility Result Tracking Identifier |
| CRIT_TAB_SHORT_NAME | VARCHAR2 | 32 |  |  | Criteria Sub Category Name |
| CRIT_TAB_PK_ID | NUMBER |  | 18 | Yes | Criteria Sub Category primary key identifier |
| INELG_RSN_CD | VARCHAR2 | 30 |  |  | Ineligibility reason code |
| ELIG_FLAG | VARCHAR2 | 1 |  | Yes | Whether eligibile flag |
| TRAVERSED_FLAG | VARCHAR2 | 1 |  | Yes | whether traversed flag |
| CRITERIA_NAME | VARCHAR2 | 600 |  | Yes | Sub Category criteria Name |
| ORDER_NUMBER | NUMBER |  | 9 | Yes | Sequence number of the criteria row |
| ELIG_CAT_CODE | VARCHAR2 | 30 |  |  | Hierarchy eligibility category code |
| ELIG_SUB_CAT_CODE | VARCHAR2 | 30 |  |  | Hierarchy eligibility sub category code |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Person Assignment Identifier |
| ASSIGNMENT_NAME | VARCHAR2 | 240 |  |  | Person Assignment name |
| CRIT_TAB_PER_VALUE | VARCHAR2 | 600 |  |  | Eligibility evaluation Sub Category person value |
| ELIG_OBJ_ID | NUMBER |  | 18 |  | ELIG_OBJ_ID |
| ELIG_PRFL_ID | NUMBER |  | 18 |  | ELIG_PRFL_ID |
| CONFIG_ID1 | NUMBER |  | 18 |  | Configuration identifier |
| CONFIG_ID2 | NUMBER |  | 18 |  | Configuration identifier |
| CONFIG_ID3 | NUMBER |  | 18 |  | Configuration identifier |
| CONFIG_NUMBER1 | NUMBER |  | 18 |  | Configuration number |
| CONFIG_NUMBER2 | NUMBER |  | 18 |  | Configuration number |
| CONFIG_NUMBER3 | NUMBER |  | 18 |  | Configuration number |
| CONFIG_DATE1 | DATE |  |  |  | Configuration date |
| CONFIG_DATE2 | DATE |  |  |  | Configuration date |
| CONFIG_DATE3 | DATE |  |  |  | Configuration date |
| CONFIG_CHAR1 | VARCHAR2 | 240 |  |  | Configuration char column |
| CONFIG_CHAR2 | VARCHAR2 | 240 |  |  | Configuration char column |
| CONFIG_CHAR3 | VARCHAR2 | 240 |  |  | Configuration char column |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CRIT_TAB_GROUP_ID | NUMBER |  | 18 |  | ID for criteria group |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| PER_ELIG_RSLT_DTLS_GT_PK | Unique | PER_ELIG_RSLT_TRACK_DTLS_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
