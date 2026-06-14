# BEN_CNTNG_PRTN_ELIG_PRFL

BEN_CNTNG_PRTN_ELIG_PRFL_F identifies the eligibility criteria for participation in a compensation plan on a continuing basis. For example,  after a life event occurs which typically disqualifies a participant  from participation and/or reduces/eliminates any employer contribution subsidy.   . In the US, continuing participation is a focus for COBRA, in and outside the US, plan sponsors may allow prior participants in a  plan (typically medical) to continue to participate if that person pays the premiums.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencntngprtneligprfl-3730.html#bencntngprtneligprfl-3730](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencntngprtneligprfl-3730.html#bencntngprtneligprfl-3730)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CNTNG_PRTN_ELIG_PRFL_PK | CNTNG_PRTN_ELIG_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CNTNG_PRTN_ELIG_PRFL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| NAME | VARCHAR2 | 240 |  |  | Name of the continuing participation eligibility profile. |
| PYMT_MUST_BE_RCVD_UOM | VARCHAR2 | 30 |  |  | Payment must be received unit of measure. |
| PYMT_MUST_BE_RCVD_NUM | NUMBER |  | 18 |  | Payment must be received number. |
| PYMT_MUST_BE_RCVD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CNTNG_PRTN_ELIG_PRFL_PK | Unique | Default | CNTNG_PRTN_ELIG_PRFL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
