# BEN_ELIG_SCHEDD_HRS_PRTE

BEN_ELIG_SCHEDD_HRS_PRTE_F  identifies the scheduled hours using the schedule number value on a person's assignment to determine whether a person is eligible or in some cases is to be excluded from eligibility to participate in a compensation object . .BEN_ELIG_SCHEDD_HRS_PRTE_F is the intersection of BEN_ELIGY_PRFL_F and HR_LOOKUPS.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligscheddhrsprte-16339.html#beneligscheddhrsprte-16339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligscheddhrsprte-16339.html#beneligscheddhrsprte-16339)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_SCHEDD_HRS_PRTE_PK | ELIG_SCHEDD_HRS_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_SCHEDD_HRS_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| HRS_NUM | NUMBER |  | 22 |  | Number of hours. |
| FREQ_CD | VARCHAR2 | 30 |  |  | Frequency of normal working hours. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DETERMINATION_CD | VARCHAR2 | 30 |  |  | Determination Code |
| DETERMINATION_RL | NUMBER |  | 18 |  | Determination Rule |
| MAX_HRS_NUM | NUMBER |  | 22 |  | Maximum Hours |
| ROUNDING_CD | VARCHAR2 | 30 |  |  | Rounding Code |
| ROUNDING_RL | NUMBER |  | 18 |  | Rounding Rule |
| SCHEDD_HRS_RL | NUMBER |  | 18 |  | Scheduled Hours Rule |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight |
| USE_WORK_SCHEDULE_FLAG | VARCHAR2 | 30 |  |  | Identifies whether to evaluate hours from work schedules |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_SCHEDD_HRS_PRTE_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_SCHEDD_HRS_PRTE_PK | Unique | Default | ELIG_SCHEDD_HRS_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
