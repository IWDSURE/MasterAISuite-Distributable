# BEN_PTIP_DPNT_CVG_CTFN_F

BEN_PTIP_DPNT_CVG_CTFN_F  identifies the certifications that may be required when participants designate contacts that have been determine to be eligible for coverage under the terms identifies by the plan type  for the plan or option in plan under which the participant is covering the dependent.  .  For example,  a participant requests the addition of a new dependent for the Stay Healthy Family medical coverage and a certification of proof of birth or adoption is required for all Medical Plans in the program.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benptipdpntcvgctfnf-19812.html#benptipdpntcvgctfnf-19812](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benptipdpntcvgctfnf-19812.html#benptipdpntcvgctfnf-19812)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PTIP_DPNT_CVG_CTFN_F_PK | PTIP_DPNT_CVG_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PTIP_DPNT_CVG_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DPNT_CVG_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Dependent coverage certification type. |
| RLSHP_TYP_CD | VARCHAR2 | 30 |  |  | Relationship type. |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DPNT_CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | Certification Determination Code |
| POPL_ACTN_TYP_ID | NUMBER |  | 18 |  | Action Type |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PTIP_DPNT_CVG_CTFN_F_N1 | Non Unique | Default | POPL_ACTN_TYP_ID |
| BEN_PTIP_DPNT_CVG_CTFN_F_PK | Unique | Default | PTIP_DPNT_CVG_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
