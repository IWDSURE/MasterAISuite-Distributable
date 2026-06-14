# BEN_LER_BNFT_RSTRN_F

BEN_LER_BNFT_RSTRN_F identifies restrictions which may be imposed a person elects to enroll in a benefit in a plan or option in plan where the enrollment opportunity is the result of a specific life event. . For example, the plan may only allow a person to change up to two levels of life insurance without certification and up to five levels with proof of good health.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerbnftrstrnf-30176.html#benlerbnftrstrnf-30176](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerbnftrstrnf-30176.html#benlerbnftrstrnf-30176)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_BNFT_RSTRN_F_PK | LER_BNFT_RSTRN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LER_BNFT_RSTRN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| MX_CVG_INCR_WCF_ALWD_AMT | NUMBER |  |  |  | Maximum coverage increase with certification allowed amount. |
| MX_CVG_INCR_ALWD_AMT | NUMBER |  |  |  | Maximum coverage increase allowed amount. |
| MX_CVG_ALWD_AMT | NUMBER |  |  |  | Maximum coverage allowed amount. |
| MX_CVG_MLT_INCR_NUM | NUMBER |  | 18 |  | Maximum coverage multiple increase number. |
| MX_CVG_MLT_INCR_WCF_NUM | NUMBER |  | 18 |  | Maximum coverage multiple increase with certification number. |
| MX_CVG_WCFN_AMT | NUMBER |  |  |  | Maximum coverage with certification amount. |
| MX_CVG_WCFN_MLT_NUM | NUMBER |  | 18 |  | Maximum coverage with certification multiple number. |
| MN_CVG_RQD_AMT | NUMBER |  |  |  | Minimum coverage amount. |
| CVG_INCR_R_DECR_ONLY_CD | VARCHAR2 | 30 |  |  | Coverage increment or decrement only. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CVG_AMT_LMT_RL | NUMBER |  |  |  | CVG_AMT_LMT_RL |
| CVG_MLT_LMT_RL | VARCHAR2 | 20 |  |  | CVG_MLT_LMT_RL |
| MX_CVG_ALWD_MLT_NUM | NUMBER |  |  |  | MX_CVG_ALWD_MLT_NUM |
| MN_CVG_RQD_MLT_NUM | NUMBER |  |  |  | MN_CVG_RQD_MLT_NUM |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_BNFT_RSTRN_F_N1 | Non Unique |  | LER_ID |
| BEN_LER_BNFT_RSTRN_F_N2 | Non Unique |  | PL_ID |
| BEN_LER_BNFT_RSTRN_F_PK | Unique | Default | LER_BNFT_RSTRN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
