# BEN_PRTT_CLM_GD_OR_SVC_TYP

BEN_PRTT_CLM_GD_OR_SVC_TYP identifies the provided goods and/or services for which a participant is seeking reimbursement.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttclmgdorsvctyp-22447.html#benprttclmgdorsvctyp-22447](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttclmgdorsvctyp-22447.html#benprttclmgdorsvctyp-22447)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTT_CLM_GD_SVC_TYP_PK | PRTT_CLM_GD_OR_SVC_TYP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTT_CLM_GD_OR_SVC_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PRTT_REIMBMT_RQST_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PRTT_REIMBMT_RQST_F. |
| GD_OR_SVC_TYP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_GD_OR_SVC_TYP. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PL_GD_OR_SVC_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_GD_OR_SVC_F. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRTT_CLM_GD_SVC_TYP_FK2 | Non Unique | Default | GD_OR_SVC_TYP_ID |
| BEN_PRTT_CLM_GD_SVC_TYP_N1 | Non Unique | Default | PRTT_REIMBMT_RQST_ID |
| BEN_PRTT_CLM_GD_SVC_TYP_PK1 | Unique | Default | PRTT_CLM_GD_OR_SVC_TYP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
