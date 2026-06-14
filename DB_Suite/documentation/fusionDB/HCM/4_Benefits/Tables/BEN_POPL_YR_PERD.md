# BEN_POPL_YR_PERD

BEN_POPL_YR_PERD identifies the years for which this plan or program is active.  The actual plan years ,with start and stop dates, are associated to the plan or program.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplyrperd-7332.html#benpoplyrperd-7332](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplyrperd-7332.html#benpoplyrperd-7332)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_POPL_YR_PERD_PK | POPL_YR_PERD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPL_YR_PERD_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| YR_PERD_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_YR_PERD. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| ACPT_CLM_RQSTS_THRU_DT | DATE |  |  |  | Accept claims through date. |
| PY_CLMS_THRU_DT | DATE |  |  |  | Pay claims through date. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent table discriminator. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_POPL_YR_PERD_FK3 | Non Unique | Default | YR_PERD_ID |
| BEN_POPL_YR_PERD_N1 | Non Unique | Default | PGM_ID |
| BEN_POPL_YR_PERD_N2 | Non Unique | Default | PL_ID |
| BEN_POPL_YR_PERD_PK | Unique | Default | POPL_YR_PERD_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
