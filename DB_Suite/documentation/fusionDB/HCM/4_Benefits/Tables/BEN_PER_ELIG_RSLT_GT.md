# BEN_PER_ELIG_RSLT_GT

ben_per_elig_rslt_track table holds data to track top level row for eligibility profile id or eligibility obj id

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpereligrsltgt-19734.html#benpereligrsltgt-19734](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpereligrsltgt-19734.html#benpereligrsltgt-19734)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_ELIG_RSLT_GT_PK | PER_ELIG_RSLT_TRACK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ELIG_RSLT_TRACK_ID | NUMBER |  | 18 | Yes | Person Eligibility result tracking identifier |
| EFFECTIVE_DATE | DATE |  |  | Yes | Effective Date of the eligibility evaluation. |
| ELIG_OBJ_ID | NUMBER |  | 18 |  | Eligibility Object Identifier |
| ELIG_PRFL_ID | NUMBER |  | 18 |  | Eligibility Profile Identifier |
| ELIG_PROD | VARCHAR2 | 30 |  |  | Calling eligibility product |
| ELIG_PROD_CALLER | VARCHAR2 | 30 |  |  | Calling eligibility product end user |
| PERSON_ID | NUMBER |  | 18 |  | person identifier |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | person assignment identifier |
| ELIG_FLAG | VARCHAR2 | 1 |  | Yes | Eligible flag |
| INELG_RSN_CD | VARCHAR2 | 30 |  |  | Ineligibility reason code |
| INELG_RSN_VALUE | VARCHAR2 | 600 |  |  | Ineligibility reason meaning |
| CRIT_TAB_SHORT_NAME | VARCHAR2 | 30 |  |  | Eligiblity Criteria short name |
| CRIT_TAB_PK_ID | NUMBER |  | 18 | Yes | Eligiblity Criteria foreign key id |
| CRIT_TAB_EXCLUDE_FLAG | VARCHAR2 | 30 |  |  | Eligiblity Criteria Exclude flag value |
| CRIT_TAB_PER_VALUE | VARCHAR2 | 600 |  |  | Eligiblity Criteria Person value |
| CONFIG_ID1 | NUMBER |  | 18 |  | Configuration identifier Column |
| CONFIG_ID2 | NUMBER |  | 18 |  | Configuration identifier Column |
| CONFIG_ID3 | NUMBER |  | 18 |  | Configuration identifier Column |
| CONFIG_NUM1 | NUMBER |  | 18 |  | Configuration Number Column |
| CONFIG_NUM2 | NUMBER |  | 18 |  | Configuration Number Column |
| CONFIG_NUM3 | NUMBER |  | 18 |  | Configuration Number Column |
| CONFIG_DATE1 | DATE |  |  |  | Configuration date Column |
| CONFIG_DATE2 | DATE |  |  |  | Configuration date Column |
| CONFIG_DATE3 | DATE |  |  |  | Configuration date Column |
| CONFIG_CHAR1 | VARCHAR2 | 240 |  |  | Configuration Char Column |
| CONFIG_CHAR2 | VARCHAR2 | 240 |  |  | Configuration Char Column |
| CONFIG_CHAR3 | VARCHAR2 | 240 |  |  | Configuration Char Column |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PARENT_CHILD_CD | VARCHAR2 | 240 |  |  | Stores parent child discriminatory value |
| MNDTRY_FLAG | VARCHAR2 | 30 |  |  | Indicates if the criteria is mandatory |
| ELIG_RSLT_TRACK_PAR_ID | NUMBER |  | 18 |  | Stores parent ID |
| CRIT_TAB_GROUP_ID | NUMBER |  | 18 |  | ID for criteria group |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_PER_ELIG_RSLT_GT_PK | Unique | PER_ELIG_RSLT_TRACK_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
