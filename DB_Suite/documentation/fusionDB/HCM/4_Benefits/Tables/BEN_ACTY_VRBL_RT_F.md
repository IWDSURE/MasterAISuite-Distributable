# BEN_ACTY_VRBL_RT_F

BEN_ACTY_VRBL_RT_F identifies the variable rate profiles which prescribe how to calculate activity base rates , contributions, distributions, and accrued benefits whose calculation varies by some factor,for example, length of service, age, location.
BEN_ACTY_VRBL_RT_F is the intersection of BEN_ACTY_BASE_RT_F and  BEN_VRBL_RT_F.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactyvrblrtf-29678.html#benactyvrblrtf-29678](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactyvrblrtf-29678.html#benactyvrblrtf-29678)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ACTY_VRBL_RT_F_PK | ACTY_VRBL_RT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTY_VRBL_RT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| ACTY_BASE_RT_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTY_BASE_RT_F. |
| VRBL_RT_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_VRBL_RT_PRFL_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ACTY_VRBL_RT_F_N1 | Non Unique | Default | VRBL_RT_PRFL_ID |
| BEN_ACTY_VRBL_RT_F_N2 | Non Unique | Default | ACTY_BASE_RT_ID |
| BEN_ACTY_VRBL_RT_F_PK | Unique | Default | ACTY_VRBL_RT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
