# BEN_ENRT_CTFN_F

BEN_ENRT_CTFN_F  identifies the certification which may be required in order for any person to substantiate their enrollment in a plan as a result of a life event reason. Life events include open and administrative enrollments as well as actual participant life events.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtctfnf-11407.html#benenrtctfnf-11407](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtctfnf-11407.html#benenrtctfnf-11407)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENRT_CTFN_F_PK | ENRT_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENRT_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Enrollment certification type. |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| POPL_ACTN_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_POPL_ACTN_TYP_F. |
| CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | Certification Determination Code. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ENRT_CTFN_F_N2 | Non Unique | Default | POPL_ACTN_TYP_ID |
| BEN_ENRT_CTFN_F_PK | Unique | Default | ENRT_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
