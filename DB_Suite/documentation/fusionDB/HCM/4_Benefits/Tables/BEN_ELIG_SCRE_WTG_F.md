# BEN_ELIG_SCRE_WTG_F

Stores computed score for each eligibility criteria

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligscrewtgf-18786.html#beneligscrewtgf-18786](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligscrewtgf-18786.html#beneligscrewtgf-18786)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_SCRE_WTG_F_PK | ELIG_SCRE_WTG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_SCRE_WTG_ID | NUMBER |  |  | Yes | Primary Key |
| ELIG_PER_ID | NUMBER |  |  |  | Foreign key to ben_elig_per_f |
| ELIG_PER_OPT_ID | NUMBER |  |  |  | Foreign key to ben_elig_per_opt_f |
| ELIG_RSLT_ID | NUMBER |  |  |  | Foreign key to ben_elig_rslt_f |
| PER_IN_LER_ID | NUMBER |  | 18 |  | Person Life Event ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ELIGY_PRFL_ID | NUMBER |  |  |  | Eligibility Profile Id |
| CRIT_TAB_SHORT_NAME | VARCHAR2 | 30 |  |  | Criteria Table Short Name |
| CRIT_TAB_PK_ID | NUMBER |  |  |  | Criteria Table Primary Key |
| COMPUTED_SCORE | NUMBER |  |  |  | Computed Score |
| BENEFIT_ACTION_ID | NUMBER |  |  |  | Benefit Acition Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_SCRE_WTG_F_N1 | Non Unique | Default | ELIG_PER_ID |
| BEN_ELIG_SCRE_WTG_F_N2 | Non Unique | Default | ELIG_PER_OPT_ID |
| BEN_ELIG_SCRE_WTG_F_N3 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_SCRE_WTG_F_N4 | Non Unique | Default | CRIT_TAB_PK_ID, CRIT_TAB_SHORT_NAME |
| BEN_ELIG_SCRE_WTG_F_PK | Unique | Default | ELIG_SCRE_WTG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
