# BEN_DPNT_CVG_RQD_RLSHP

BEN_DPNT_CVG_RQD_RLSHP_F identifies the relationship between a participant and a dependent which must be satisfied in order for a  participant to designate a dependent for a program, plan type in program,   or plan.  These requirements are associated with a dependent  coverage eligibility profile and not directly to the program, plan in program or plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendpntcvgrqdrlshp-14579.html#bendpntcvgrqdrlshp-14579](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendpntcvgrqdrlshp-14579.html#bendpntcvgrqdrlshp-14579)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DPNT_CVG_RQD_RLSHP_PK | DPNT_CVG_RQD_RLSHP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DPNT_CVG_RQD_RLSHP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_DPNT_CVG_RQD_RLSHP_F. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PER_RELSHP_TYP_CD | VARCHAR2 | 30 |  | Yes | Person relationship type. |
| CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Coverage start date code. |
| CVG_THRU_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| CVG_THRU_DT_CD | VARCHAR2 | 30 |  |  | Coverage through date code. |
| CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ELIGY_PRFL. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_DPNT_CVG_RQD_RLSHP_PK | Unique | Default | DPNT_CVG_RQD_RLSHP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
