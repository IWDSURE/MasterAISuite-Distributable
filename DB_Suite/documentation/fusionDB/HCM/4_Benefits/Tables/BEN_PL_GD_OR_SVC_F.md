# BEN_PL_GD_OR_SVC_F

BEN_PL_GD_OR_SVC_F  contains the list of goods or services that may be reimbursed by the compensation plan.  A process will validate whether or not these goods or services may be reimbursed as taxable or nontaxable.  Generally, reimbursements are nontaxable.  BEN_PL_GD_OR_SVC_F may also identify  the goods or services provided by a plan.  For example, the Medical FSA reimburses deductible amounts and prescription drugs.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplgdorsvcf-31576.html#benplgdorsvcf-31576](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplgdorsvcf-31576.html#benplgdorsvcf-31576)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_GD_OR_SVC_F_PK | PL_GD_OR_SVC_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_GD_OR_SVC_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PL_F. |
| GD_OR_SVC_TYP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_GD_OR_SVC_TYP. |
| ALW_RCRRG_CLMS_FLAG | VARCHAR2 | 30 |  | Yes | Allows recurring claims Y or N. |
| GD_OR_SVC_USG_CD | VARCHAR2 | 30 |  |  | Goods or services usage. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| GD_SVC_RECD_BASIS_CD | VARCHAR2 | 30 |  |  | Goods or service received. |
| GD_SVC_RECD_BASIS_DT | DATE |  |  |  | Goods or service received date. |
| GD_SVC_RECD_BASIS_MO | NUMBER |  | 18 |  | Goods or service received. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_GD_OR_SVC_F_FK2 | Non Unique | Default | GD_OR_SVC_TYP_ID |
| BEN_PL_GD_OR_SVC_F_N1 | Non Unique | Default | PL_ID |
| BEN_PL_GD_OR_SVC_F_PK | Unique | Default | PL_GD_OR_SVC_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
