# BEN_LER_ENRT_CTFN_F

BEN_LER_ENRT_CTFN_F identifies the types of certifications that may be required  in order to enroll in a plan as a result of a specified life event.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerenrtctfnf-7823.html#benlerenrtctfnf-7823](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerenrtctfnf-7823.html#benlerenrtctfnf-7823)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_ENRT_CTFN_F_PK | LER_ENRT_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LER_ENRT_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |
| ENRT_CTFN_TYP_CD | VARCHAR2 | 30 |  |  | Enrollment certification type. |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | CTFN_DETERMINE_CD |
| LER_POPL_ACTN_TYP_ID | NUMBER |  |  |  | LER_POPL_ACTN_TYP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_ENRT_CTFN_F_N1 | Non Unique |  | LER_POPL_ACTN_TYP_ID |
| BEN_LER_ENRT_CTFN_F_PK | Unique | Default | LER_ENRT_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
