# BEN_LER_BNFT_RSTRN_CTFN_F

BEN_LER_BNFT_RSTRN_CTFN_F identifies which certifications may be required when a person elects to enroll in a benefit in a plan or option in plan where the enrollment opportunity is the result of a specific life event.  . For example, a person is enrolled in three times pay life insurance.  The person gets married and elects ten time pay life insurance and the plan requires proof of good health when a person jumps more than two levels.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerbnftrstrnctfnf-12388.html#benlerbnftrstrnctfnf-12388](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerbnftrstrnctfnf-12388.html#benlerbnftrstrnctfnf-12388)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_BNFT_RSTRN_CTFN_F_PK | LER_BNFT_RSTRN_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LER_BNFT_RSTRN_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |
| ENRT_CTFN_TYP_CD | VARCHAR2 | 30 |  |  | Enrollment certification type. |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | CTFN_DETERMINE_CD |
| LER_POPL_ACTN_TYP_ID | NUMBER |  | 18 |  | LER_POPL_ACTN_TYP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LBNFT_RST_CTFN_F_PK | Unique | Default | LER_BNFT_RSTRN_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| BEN_LER_BRTRN_CTFN_F_N1 | Non Unique | Default | LER_POPL_ACTN_TYP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
