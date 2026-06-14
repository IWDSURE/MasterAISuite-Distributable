# BEN_ELIG_SVC_AREA_PRTE

BEN_ELIG_SVC_AREA_PRTE_F identifies a group of postal codes.  A person must live, in one of the postal codes in the service area in order to be eligible for or (most typical usage) or not eligible to participate in (least typical) a compensation object. BEN_ELIG_SVC_AREA_PRTE_F  is the intersection of BEN_ELIGY_PRFL_F  and BEN_SVC_AREA.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligsvcareaprte-8944.html#beneligsvcareaprte-8944](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligsvcareaprte-8944.html#beneligsvcareaprte-8944)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_SVC_AREA_PRTE_PK | ELIG_SVC_AREA_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_SVC_AREA_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| EXCLD_FLAG | VARCHAR2 | 1 |  | Yes | Exclude Y or N. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| SVC_AREA_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_SVC_AREA_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
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
| BEN_ELIG_SVC_AREA_PRTE_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_SVC_AREA_PRTE_N2 | Non Unique | Default | SVC_AREA_ID |
| BEN_ELIG_SVC_AREA_PRTE_PK | Unique | Default | ELIG_SVC_AREA_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
