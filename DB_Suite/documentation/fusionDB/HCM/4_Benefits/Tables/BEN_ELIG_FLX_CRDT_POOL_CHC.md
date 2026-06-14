# BEN_ELIG_FLX_CRDT_POOL_CHC

This table will hold the Flex Credit Pool Choice records

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligflxcrdtpoolchc-17760.html#beneligflxcrdtpoolchc-17760](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligflxcrdtpoolchc-17760.html#beneligflxcrdtpoolchc-17760)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_FLXCR_POOLCHC_PK | ELIG_FLX_CRDT_POOL_CHC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_FLX_CRDT_POOL_CHC_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| BENEFIT_RELATION_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_BENEFIT_RELATIONS_F |
| PER_IN_LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PER_IN_LER |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ELIG_PER_ELCTBL_CHC |
| CRDT_POOL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTY_BASE_RT_F |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  | Yes | Flex Credits Pool Level |
| POOL_ORDR_NUM | NUMBER |  | 18 |  | Flex Credits Pool Level |
| CONTEXT_PGM_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PGM_F |
| CONTEXT_PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F |
| CONTEXT_OPT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OPT_F |
| PGM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PGM_F |
| PLIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PLIP_F |
| OIPLIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPLIP_F |
| PTIP_ID | NUMBER |  | 18 |  | Reserved for Future Use |
| PL_TYP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_TYP_F |
| CMBN_PLIP_ID | NUMBER |  | 18 |  | Reserved for Future Use |
| CMBN_PTIP_ID | NUMBER |  | 18 |  | Reserved for Future Use |
| CMBN_PTIP_OPT_ID | NUMBER |  | 18 |  | Reserved for Future Use |
| PIL_ELCTBL_CHC_POPL_ID | NUMBER |  | 18 |  | Foreign key to BEN_PIL_ELCTBL_CHC_POPL_F. |
| USE_TO_CALC_NET_FLX_CR_FLAG | VARCHAR2 | 30 |  |  | Reserved for Future Use |
| AUTO_ALCT_EXCS_FLAG | VARCHAR2 | 30 |  |  | Copied from Credit Pool |
| EXCS_TRTMT_CD | VARCHAR2 | 30 |  |  | Copied from Credit Pool |
| ADD_TO_PGM_POOL_FLAG | VARCHAR2 | 30 |  |  | Add to Program Pool flag |
| PRNT_POOL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F (Credit Pools) |
| CHILD_POOL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F (Credit Pools) |
| ALWS_NGTV_USG_FLAG | VARCHAR2 | 30 |  |  | Allows overspending flag |
| PCT_NGTV_USG_BY_TOTAL_POOL | NUMBER |  |  |  | Overspending Limit as a % of Total Credits of the Pool |
| CASH_DSTRBN_RSTRCN_CD | VARCHAR2 | 30 |  |  | Copied from Credit Pool |
| MN_CASH_DSTRBL_PCT | NUMBER |  |  |  | Copied from Credit Pool |
| MX_CASH_DSTRBL_PCT | NUMBER |  |  |  | Copied from Credit Pool |
| MN_CASH_DSTRBL_VAL | NUMBER |  |  |  | Copied from Credit Pool |
| MX_CASH_DSTRBL_VAL | NUMBER |  |  |  | Copied from Credit Pool |
| VAL | NUMBER |  |  |  | Defined Value |
| ANN_VAL | NUMBER |  |  |  | Annual Value |
| CMCD_VAL | NUMBER |  |  |  | Communicated Value |
| SPENDING_LIMIT | NUMBER |  |  |  | Spending Limit |
| CRDT_POOL_SPND_RLVR_OPT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_CRDT_POOL_SPND_RLVR_OPT_F |
| ENRT_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ENRT_RT |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F |
| ORDR_NUM | NUMBER |  | 18 |  | Sequence / Order number for Rollover Options |
| RLVR_DSTRBN_RSTRCN_CD | VARCHAR2 | 30 |  |  | Rollover Distribution Limits or Restriction Code |
| MN_RLVR_DSTRBL_PCT | NUMBER |  |  |  | Min Limit for Rollover in Percentage |
| MX_RLVR_DSTRBL_PCT | NUMBER |  |  |  | Max Limit for Rollover in Percentage |
| MN_RLVR_DSTRBL_VAL | NUMBER |  |  |  | Min Limit for Rollover Amount |
| MX_RLVR_DSTRBL_VAL | NUMBER |  |  |  | Max Limit for Rollover Amount |
| RLVR_RNDG_CD | VARCHAR2 | 30 |  |  | Rounding Code for Rollover amount |
| RLVR_RNDG_RL | NUMBER |  | 18 |  | Rounding Rule for Rollover amount |
| POOL_CHC_CLASS | VARCHAR2 | 30 |  | Yes | Ledger Row Classification |
| POOL_CHC_TYP_CD | VARCHAR2 | 30 |  | Yes | Ledger Row Type - Credit or Debit |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID Field |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID Field |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID Field |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID Field |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID Field |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template Number Field |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template Number Field |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template Number Field |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template Number Field |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template Number Field |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template Character Field |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template Character Field |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template Character Field |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template Character Field |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template Character Field |
| CONFIG_DATE_1 | DATE |  |  |  | Template Date Field |
| CONFIG_DATE_2 | DATE |  |  |  | Template Date Field |
| CONFIG_DATE_3 | DATE |  |  |  | Template Date Field |
| CONFIG_DATE_4 | DATE |  |  |  | Template Date Field |
| CONFIG_DATE_5 | DATE |  |  |  | Template Date Field |
| FPC_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| FPC_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| FPC_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | Defined Value Frequency |
| CMCD_REF_PERD_CD | VARCHAR2 | 30 |  |  | Communicated Value Frequency |
| FLEX_CRDT_LDGR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_FLEX_CRDT_LDGR |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_FLXCR_POOLCHC_N1 | Non Unique | Default | BUSINESS_GROUP_ID |
| BEN_ELIG_FLXCR_POOLCHC_N2 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_ELIG_FLXCR_POOLCHC_N3 | Non Unique | Default | PER_IN_LER_ID |
| BEN_ELIG_FLXCR_POOLCHC_N4 | Non Unique | Default | ELIG_PER_ELCTBL_CHC_ID |
| BEN_ELIG_FLXCR_POOLCHC_N5 | Non Unique | Default | CRDT_POOL_ID |
| BEN_ELIG_FLXCR_POOLCHC_N6 | Non Unique | Default | CONTEXT_PGM_ID |
| BEN_ELIG_FLXCR_POOLCHC_N7 | Non Unique | Default | PIL_ELCTBL_CHC_POPL_ID |
| BEN_ELIG_FLXCR_POOLCHC_PK | Unique | Default | ELIG_FLX_CRDT_POOL_CHC_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
