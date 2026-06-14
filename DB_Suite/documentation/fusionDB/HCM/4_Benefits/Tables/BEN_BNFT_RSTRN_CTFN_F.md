# BEN_BNFT_RSTRN_CTFN_F

BEN_BNFT_RSTRN_CTFN_F identifies the certification(s) that may be required when a restriction has been placed on the levels of benefits or coverage, such as life insurance.  . For example, the plan provides coverage from 10,000 to 100,000  in increments of 10,000.  The person may only increase his or her coverage up  to two multiples of 10,000 and certification must be provided if he or she elects  higher coverage.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftrstrnctfnf-8753.html#benbnftrstrnctfnf-8753](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftrstrnctfnf-8753.html#benbnftrstrnctfnf-8753)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BNFT_RSTRN_CTFN_F_PK | BNFT_RSTRN_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BNFT_RSTRN_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RQD_FLAG | VARCHAR2 | 30 |  | Yes | Required Y or N. |
| ENRT_CTFN_TYP_CD | VARCHAR2 | 30 |  |  | Enrollment certification type. |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| POPL_ACTN_TYP_ID | NUMBER |  | 18 |  | POPL_ACTN_TYP_ID |
| CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | CTFN_DETERMINE_CD |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BNFT_RSTRN_CTFN_F_N1 | Non Unique |  | POPL_ACTN_TYP_ID |
| BEN_BNFT_RSTRN_CTFN_F_PK | Unique | Default | BNFT_RSTRN_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
