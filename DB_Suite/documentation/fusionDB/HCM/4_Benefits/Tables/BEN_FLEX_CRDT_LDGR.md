# BEN_FLEX_CRDT_LDGR

This table will hold the Flex Credit Ledger Entries.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benflexcrdtldgr-25905.html#benflexcrdtldgr-25905](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benflexcrdtldgr-25905.html#benflexcrdtldgr-25905)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_FLEX_CRDT_LDGR_PK | FLEX_CRDT_LDGR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLEX_CRDT_LDGR_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| LDGR_STRT_DT | DATE |  |  | Yes | Ledger Start Date |
| LDGR_END_DT | DATE |  |  | Yes | Ledger End Date |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ALL_PEOPLE_F |
| BENEFIT_RELATION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_RELATIONS_F |
| PER_IN_LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PER_IN_LER |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PGM_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PGM_F |
| CRDT_POOL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTY_BASE_RT_F |
| ELIG_FLX_CRDT_POOL_CHC_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ELIG_FLX_CRDT_POOL_CHC |
| LDGR_CLASS | VARCHAR2 | 30 |  | Yes | Ledger Row Classification |
| LDGR_TYP_CD | VARCHAR2 | 30 |  | Yes | Ledger Row Type - Credit or Debit |
| FLEX_PRTT_ENRT_RSLT_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PRTT_ENRT_RSLT |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PRTT_ENRT_RSLT |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F |
| PRTT_RT_VAL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PRTT_RT_VAL |
| PRNT_POOL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F (Credit Pools) |
| CHILD_POOL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F (Credit Pools) |
| FCL_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| FCL_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FCL_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | Defined Value Frequency |
| CMCD_REF_PERD_CD | VARCHAR2 | 30 |  |  | Communicated Value Frequency |
| DONATED_TO_PRNT_POOL_VAL | NUMBER |  |  |  | Credits donated to program pool |
| RECD_FROM_CHILD_POOL_VAL | NUMBER |  |  |  | Credits received from a child level pool |
| CMCD_DONATED_TO_PRNT_VAL | NUMBER |  |  |  | Communicated Value of credits donated to parent pool |
| ANN_DONATED_TO_PRNT_VAL | NUMBER |  |  |  | Annual Value of credits donated to parent pool |
| CMCD_RECD_FROM_CHILD_VAL | NUMBER |  |  |  | Communicated Value of credits received from child pool |
| ANN_RECD_FROM_CHILD_VAL | NUMBER |  |  |  | Annual Value of credits received from child pool |
| SPENDING_LIMIT | NUMBER |  |  |  | Spending Limit |
| FRFTD_VAL | NUMBER |  |  |  | Defined Value of Forfeited Credits |
| CMCD_FRFTD_VAL | NUMBER |  |  |  | Communicated Value of Forfeited Credits |
| ANN_FRFTD_VAL | NUMBER |  |  |  | Annual Value of Forfeited Credits |
| PRVDD_VAL | NUMBER |  |  |  | Defined Value of Credits Provided |
| CMCD_PRVDD_VAL | NUMBER |  |  |  | Communicated Value of Credits Provided |
| ANN_PRVDD_VAL | NUMBER |  |  |  | Annual Value of Credits Provided |
| RLD_UP_VAL | NUMBER |  |  |  | Defined Value of Rolled-over Credits |
| CMCD_RLD_UP_VAL | NUMBER |  |  |  | Communicated Value of Rolled-over Credits |
| ANN_RLD_UP_VAL | NUMBER |  |  |  | Annual Value of Rolled-over Credits |
| USED_VAL | NUMBER |  |  |  | Defined Value of Credits Used |
| CMCD_USED_VAL | NUMBER |  |  |  | Communicated Value of Credits Used |
| ANN_USED_VAL | NUMBER |  |  |  | Annual Value of Credits Used |
| CASH_RECD_VAL | NUMBER |  |  |  | Defined Value of Credits Received as Cash |
| CMCD_CASH_RECD_VAL | NUMBER |  |  |  | Communicated Value of Credits Received as Cash |
| ANN_CASH_RECD_VAL | NUMBER |  |  |  | Annual Value of Credits Received as Cash |
| SUM_USED_VAL | NUMBER |  |  |  | Sum of Used Val by Credit Pool |
| SUM_RLD_OVR_VAL | NUMBER |  |  |  | Sum of Rolled Over Val by Credit Pool |
| SUM_CASH_RECD_VAL | NUMBER |  |  |  | Sum of Cash Received Val by Credit Pool |
| SUM_FRFTD_VAL | NUMBER |  |  |  | Sum of Forfeited Val by Credit Pool |
| SUM_ANN_USED_VAL | NUMBER |  |  |  | Sum of Used Val by Credit Pool |
| SUM_ANN_RLD_OVR_VAL | NUMBER |  |  |  | Sum of Rolled Over Val by Credit Pool |
| SUM_ANN_CASH_RECD_VAL | NUMBER |  |  |  | Sum of Cash Received Val by Credit Pool |
| SUM_ANN_FRFTD_VAL | NUMBER |  |  |  | Sum of Forfeited Val by Credit Pool |
| SUM_CMCD_USED_VAL | NUMBER |  |  |  | Sum of Used Val by Credit Pool |
| SUM_CMCD_RLD_OVR_VAL | NUMBER |  |  |  | Sum of Rolled Over Val by Credit Pool |
| SUM_CMCD_CASH_RECD_VAL | NUMBER |  |  |  | Sum of Cash Received Val by Credit Pool |
| SUM_CMCD_FRFTD_VAL | NUMBER |  |  |  | Sum of Forfeited Val by Credit Pool |
| ENDED_PER_IN_LER_ID | NUMBER |  | 18 |  | Used for Backout-Restore Logic |
| LDGR_STAT_CD | VARCHAR2 | 30 |  |  | Used for Backout-Restore Logic |
| ENDED_LDGR_THRU_DT | DATE |  |  |  | Used for Backout-Restore Logic |
| ORIGINAL_LDGR_STRT_DT | DATE |  |  |  | Used for Backout-Restore Logic |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_FLEX_CRDT_LDGR_N1 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_FLEX_CRDT_LDGR_N2 | Non Unique | Default | PER_IN_LER_ID |
| BEN_FLEX_CRDT_LDGR_N3 | Non Unique | Default | PGM_ID |
| BEN_FLEX_CRDT_LDGR_N4 | Non Unique | Default | CRDT_POOL_ID |
| BEN_FLEX_CRDT_LDGR_N5 | Non Unique | Default | PERSON_ID |
| BEN_FLEX_CRDT_LDGR_PK | Unique | Default | FLEX_CRDT_LDGR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
