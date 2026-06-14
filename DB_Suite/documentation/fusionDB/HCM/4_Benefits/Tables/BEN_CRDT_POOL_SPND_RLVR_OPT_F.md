# BEN_CRDT_POOL_SPND_RLVR_OPT_F

BEN_CRDT_POOL_SPND_RLVR_OPT_F stores the activity base rates which are specified as spending or rollover options for credit pools defined for flex programs.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencrdtpoolspndrlvroptf-21658.html#bencrdtpoolspndrlvroptf-21658](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencrdtpoolspndrlvroptf-21658.html#bencrdtpoolspndrlvroptf-21658)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CRDT_POOL_SPND_RLVR_O_PK | CRDT_POOL_SPND_RLVR_OPT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CRDT_POOL_SPND_RLVR_OPT_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| CRDT_POOL_ACTY_BASE_RT_ID | NUMBER |  | 18 | Yes | The Activity Base Rate ID for the Flex Credit Pool Record |
| SPND_OR_RLVR_OPT | VARCHAR2 | 30 |  | Yes | Flag to determine if this will be a SPENDING_OPTION/ROLLOVER_OPTION |
| ACTY_BASE_RT_ID | NUMBER |  | 18 | Yes | The ID of the Activity Base Rate which is the actual Spending/Rollover option |
| CRDT_POOL_PGM_ID | NUMBER |  | 18 | Yes | Credit Pool's ProgramID |
| ORDR_NUM | NUMBER |  | 18 |  | Sequence/Order number |
| RLVR_DSTRBN_RSTRCN_CD | VARCHAR2 | 30 |  |  | Rollover Distribution Limits/Restriction Code PCT_EXCS or AMT or  PCT_TOTL |
| MN_RLVR_DSTRBL_PCT | NUMBER |  |  |  | Min Limit for Rollover in Percentage, when RLVR_DSTRBN_RSTRCN_CD is PCT_EXCS/PCT_TOTL |
| MX_RLVR_DSTRBL_PCT | NUMBER |  |  |  | Max Limit for Rollover in Percentage, when RLVR_DSTRBN_RSTRCN_CD is PCT_EXCS/PCT_TOTL |
| MN_RLVR_DSTRBL_VAL | NUMBER |  |  |  | Min Limit for Rollover Amount, when RLVR_DSTRBN_RSTRCN_CD is AMT |
| MX_RLVR_DSTRBL_VAL | NUMBER |  |  |  | Max Limit for Rollover Amount, when RLVR_DSTRBN_RSTRCN_CD is AMT |
| RLVR_RNDG_CD | VARCHAR2 | 30 |  |  | Rounding Code for Rollover amount (during default/automatic mode) |
| RLVR_RNDG_RL | NUMBER |  | 18 |  | Foreign Key to FF_FORMULAS_F |
| ABP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column |
| ABP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| ABP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PCT_RNDG_RL | NUMBER |  | 18 |  | PCT_RNDG_RL |
| VAL_RNDG_RL | NUMBER |  | 18 |  | VAL_RNDG_RL |
| PCT_RNDG_CD | VARCHAR2 | 30 |  |  | PCT_RNDG_CD |
| VAL_RNDG_CD | VARCHAR2 | 30 |  |  | VAL_RNDG_CD |
| RLOVR_VAL_INCRMT_NUM | NUMBER |  | 18 |  | RLOVR_VAL_INCRMT_NUM |
| RLOVR_VAL_RL | VARCHAR2 | 18 |  |  | RLOVR_VAL_RL |
| MX_RCHD_DFLT_ORDR_NUM | NUMBER |  | 18 |  | MX_RCHD_DFLT_ORDR_NUM |
| PCT_RLOVR_INCRMT_NUM | NUMBER |  | 18 |  | PCT_RLOVR_INCRMT_NUM |
| PRTT_ELIG_RLOVR_RL | NUMBER |  | 18 |  | PRTT_ELIG_RLOVR_RL |
| CRS_RLOVR_PROCG_CD | VARCHAR2 | 30 |  |  | CRS_RLOVR_PROCG_CD |
| MX_PCT_TTL_CRS_CN_ROLL_NUM | NUMBER |  |  |  | MX_PCT_TTL_CRS_CN_ROLL_NUM |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CRDT_POOL_SPND_RLVR_OPT_N2 | Non Unique | Default | CRDT_POOL_PGM_ID, ACTY_BASE_RT_ID |
| BEN_CRDT_POOL_SPND_RLVR_OPT_PK | Unique | Default | CRDT_POOL_SPND_RLVR_OPT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
