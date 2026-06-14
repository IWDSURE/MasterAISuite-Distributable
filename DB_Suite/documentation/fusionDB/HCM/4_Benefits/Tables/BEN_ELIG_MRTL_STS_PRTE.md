# BEN_ELIG_MRTL_STS_PRTE

BEN_ELIG_MRTL_STS_PRTE stores marital status criteria.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligmrtlstsprte-14828.html#beneligmrtlstsprte-14828](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligmrtlstsprte-14828.html#beneligmrtlstsprte-14828)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_MRTL_STS_PRTE_PK | ELIG_MRTL_STS_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_MRTL_STS_PRTE_ID | NUMBER |  | 18 | Yes | Primary Key |
| LEGISLATION_CODE | VARCHAR2 | 120 |  |  | Stores Legislation Code |
| START_DATE | DATE |  |  |  | Start Date |
| END_DATE | DATE |  |  |  | End Date |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Enterprise Identifier |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Employer |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Eligibilit Profile Identifier |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Flag |
| MARITAL_STATUS | VARCHAR2 | 30 |  |  | Marital Status |
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
| BEN_ELIG_MRTL_STS_PRTE_PK | Unique | Default | ELIG_MRTL_STS_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
