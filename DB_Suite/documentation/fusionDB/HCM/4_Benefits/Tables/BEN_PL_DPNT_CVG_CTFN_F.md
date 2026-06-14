# BEN_PL_DPNT_CVG_CTFN_F

BEN_PL_DPNT_CVG_CTFN_F identifies the certification that may be required in order to designate a person as a dependent when dependent designation is defined at the plan level.  . For example, a person may be required to provided proof of birth or adoption when adding a child for the Stay Healthy Medical Plan coverage.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpldpntcvgctfnf-15897.html#benpldpntcvgctfnf-15897](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpldpntcvgctfnf-15897.html#benpldpntcvgctfnf-15897)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_DPNT_CVG_CTFN_F_PK | PL_DPNT_CVG_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_DPNT_CVG_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DPNT_CVG_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Dependent coverage certification type. |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |
| RLSHP_TYP_CD | VARCHAR2 | 30 |  |  | Relationship type. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| POPL_ACTN_TYP_ID | NUMBER |  | 18 |  | POPL_ACTN_TYP_ID |
| DPNT_CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | DPNT_CTFN_DETERMINE_CD |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_DPNT_CVG_CTFN_F_N1 | Non Unique | Default | POPL_ACTN_TYP_ID |
| BEN_PL_DPNT_CVG_CTFN_F_PK | Unique | Default | PL_DPNT_CVG_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
