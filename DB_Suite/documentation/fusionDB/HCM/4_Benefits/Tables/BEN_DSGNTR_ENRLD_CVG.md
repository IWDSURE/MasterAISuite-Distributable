# BEN_DSGNTR_ENRLD_CVG

BEN_DSGNTR_ENRLD_CVG_F  identifies whether the participant, must be  enrolled in the plan or option in order for the designated dependent to be eligible for coverage.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendsgntrenrldcvg-3475.html#bendsgntrenrldcvg-3475](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendsgntrenrldcvg-3475.html#bendsgntrenrldcvg-3475)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DSGNTR_ENRL_CVG_PK | DSGNTR_ENRLD_CVG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DSGNTR_ENRLD_CVG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| DSGNTR_CRNTLY_ENRLD_FLAG | VARCHAR2 | 30 |  |  | Designator currently enrolled Y or N. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ELIGY_PRFL. |
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
| BEN_DSGNTR_ENRL_CVG_PK | Unique | Default | DSGNTR_ENRLD_CVG_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
