# BEN_ELIG_STDNT_STAT_CVG

BEN_ELIG_STDNT_STAT_CVG_F identifies the applicable student status which must be satisfied in order for a contact with the personal relationship flag on to be eligible for a participant to designate him or her for coverage.  These requirements are associated with a dependent coverage eligibility profile and not directly to the program, plan type in program, or plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligstdntstatcvg-20426.html#beneligstdntstatcvg-20426](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligstdntstatcvg-20426.html#beneligstdntstatcvg-20426)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_STDNT_STAT_CVG_PK | ELIG_STDNT_STAT_CVG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_STDNT_STAT_CVG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| ELIGY_PRFL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_DPNT_CVG_ELIGY_PRFL_F. |
| CVG_STRT_CD | VARCHAR2 | 30 |  |  | Coverage start date code. |
| CVG_STRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| CVG_THRU_CD | VARCHAR2 | 30 |  |  | Coverage through date code. |
| CVG_THRU_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| STDNT_STAT_CD | VARCHAR2 | 30 |  | Yes | Student status. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_STDNT_STAT_CVG_PK | Unique | Default | ELIG_STDNT_STAT_CVG_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
