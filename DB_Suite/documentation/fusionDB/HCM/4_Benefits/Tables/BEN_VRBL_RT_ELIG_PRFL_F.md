# BEN_VRBL_RT_ELIG_PRFL_F

Intersection table of Variable rate Profile and Eligibility Profile tables.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrteligprflf-8957.html#benvrblrteligprflf-8957](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrteligprflf-8957.html#benvrblrteligprflf-8957)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VRBL_RT_ELIG_PRFL_F_PK | VRBL_RT_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| VRBL_RT_ELIG_PRFL_ID | NUMBER |  | 18 | Yes | System generated primary key column | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS | Active |
| VRBL_RT_PRFL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_VRBL_RT_PRFL_F | Active |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ELIGY_PRFL_F | Active |
| MNDTRY_FLAG | VARCHAR2 | 30 |  | Yes | Mandatory Flag Y or N | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_VRBL_RT_ELIG_PRFL_F_PK | Unique | FUSION_TS_TX_DATA | VRBL_RT_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE | Active |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
