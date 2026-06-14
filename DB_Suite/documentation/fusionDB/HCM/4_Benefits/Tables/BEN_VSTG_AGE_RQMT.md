# BEN_VSTG_AGE_RQMT

BEN_VSTG_AGE_RQMT identifies the minimum and maximum age ranges which are then used to determine vesting values for a rate.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvstgagerqmt-6025.html#benvstgagerqmt-6025](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvstgagerqmt-6025.html#benvstgagerqmt-6025)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VSTG_AGE_RQMT_PK | VSTG_AGE_RQMT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VSTG_AGE_RQMT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| TO_AGE_YRS_NUM | NUMBER |  | 18 |  | To age in years. |
| FROM_AGE_YRS_NUM | NUMBER |  | 18 |  | From age in years. |
| TO_AGE_MOS_NUM | NUMBER |  | 18 |  | To age in months. |
| FROM_AGE_MOS_NUM | NUMBER |  | 18 |  | From age in months. |
| AGE_FCTR_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_AGE_FCTR_F. |
| VSTG_SCHED_ID | NUMBER |  | 18 |  | Foreign key to BEN_VSTG_SCHED_F. |
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
| BEN_VSTG_AGE_RQMT_FK2 | Non Unique | Default | AGE_FCTR_ID |
| BEN_VSTG_AGE_RQMT_N1 | Non Unique | Default | VSTG_SCHED_ID |
| BEN_VSTG_AGE_RQMT_PK | Unique | Default | VSTG_AGE_RQMT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
