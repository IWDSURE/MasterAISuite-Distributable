# BEN_PL_GD_R_SVC_CTFN_F

BEN_PL_GD_R_SVC_CTFN_F identifies what certification may be required to substantiate a reimbursement claim  for the plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplgdrsvcctfnf-17041.html#benplgdrsvcctfnf-17041](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplgdrsvcctfnf-17041.html#benplgdrsvcctfnf-17041)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_GD_R_SVC_CTFN_F_PK | PL_GD_R_SVC_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_GD_R_SVC_CTFN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PL_GD_OR_SVC_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_GD_OR_SVC_F. |
| PFD_FLAG | VARCHAR2 | 30 |  | Yes | Preferred Y or N. |
| LACK_CTFN_DENY_RMBMT_FLAG | VARCHAR2 | 30 |  | Yes | Lack of certification deny reimbursement Y or N. |
| RMBMT_CTFN_TYP_CD | VARCHAR2 | 30 |  | Yes | Reimbursement certification type. |
| LACK_CTFN_DENY_RMBMT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RQD_FLAG | VARCHAR2 | 30 |  |  | Reuired Flag  Y or N. |
| CTFN_RQD_WHEN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_GD_R_SVC_CTFN_F_N1 | Non Unique |  | PL_GD_OR_SVC_ID |
| BEN_PL_GD_R_SVC_CTFN_F_PK | Unique | Default | PL_GD_R_SVC_CTFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
