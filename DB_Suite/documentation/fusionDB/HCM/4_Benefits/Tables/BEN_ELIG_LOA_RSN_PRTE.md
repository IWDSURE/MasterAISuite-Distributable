# BEN_ELIG_LOA_RSN_PRTE

BEN_LOA_RSN_PRTE_F identifies which leaves of absence based on absence type are included in (most typical usage) or excluded from (least typical) an eligibility profile. These requirements must be satisfied in order for the person to be eligible to participate in the compensation object.  BEN_LOA_RSN_PRTE_F is the intersection of BEN_ELIGY_PRFL_F and PER_ABS_ATTENDANCE_REASONS  and PER_ABSENCE_ATTENDANCE_TYPES.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligloarsnprte-16105.html#beneligloarsnprte-16105](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligloarsnprte-16105.html#beneligloarsnprte-16105)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_LOA_RSN_PRTE_PK | ELIG_LOA_RSN_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_LOA_RSN_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group Identifier |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ABSENCE_ATTENDANCE_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ABSENCE_ATTENDANCE_TYPES. |
| ABS_ATTENDANCE_REASON_ID | NUMBER |  | 18 |  | Foreign Key to PER_ABSENCE_ATTENDANCE_REASONS. |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_LOA_RSN_PRTE_N1 | Non Unique | FUSION_TS_TX_IDX | ELIGY_PRFL_ID |
| BEN_ELIG_LOA_RSN_PRTE_PK | Unique | FUSION_TS_TX_IDX | ELIG_LOA_RSN_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
