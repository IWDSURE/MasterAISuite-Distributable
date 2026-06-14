# BEN_ELIG_CMBN_AGE_LOS_PRTE

BEN_ELIG_CMBN_AGE_LOS_PRTE_F  identifies that a combination of age and length of service are included in (most typical usage) or excluded from (least typical) an eligibility profile.  These criteria must be satisfied in order for the person to be eligible to participate in the compensation object.   BEN_ELIG_CMBN_AGE_LOS_PRTE_F  is the intersection of BEN_ELIGY_PRFL  and BEN_CMBN_AGE_LOS_FCTR.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligcmbnagelosprte-27120.html#beneligcmbnagelosprte-27120](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligcmbnagelosprte-27120.html#beneligcmbnagelosprte-27120)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_CMBN_AGE_LOS_PRT_PK | ELIG_CMBN_AGE_LOS_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_CMBN_AGE_LOS_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CMBN_AGE_LOS_FCTR_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_CMBN_AGE_LOS_FCTR_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| MNDTRY_FLAG | VARCHAR2 | 30 |  | Yes | Mandatory Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_CMBN_AGE_LOS_PRTE_FK2 | Non Unique | Default | CMBN_AGE_LOS_FCTR_ID |
| BEN_ELIG_CMBN_AGE_LOS_PRTE_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_CMBN_AGE_LOS_PRTE_PK | Unique | Default | ELIG_CMBN_AGE_LOS_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
