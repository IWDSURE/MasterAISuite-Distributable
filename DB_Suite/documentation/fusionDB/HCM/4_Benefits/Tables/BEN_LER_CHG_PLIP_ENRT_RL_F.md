# BEN_LER_CHG_PLIP_ENRT_RL_F

BEN_LER_CHG_PLIP_ENRT_RL_F  identifies a rule  to be used to determine the parameters which control enrollment for this life event reason and plan.  A rule is used in those cases when the delivered, standard approach attributed in life event reason to change plan enrollment  does not support the business requirement

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerchgplipenrtrlf-22693.html#benlerchgplipenrtrlf-22693](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerchgplipenrtrlf-22693.html#benlerchgplipenrtrlf-22693)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_CHG_PLIP_ENT_RL_F_PK | LER_CHG_PLIP_ENRT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LER_CHG_PLIP_ENRT_RL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| FORMULA_ID | NUMBER |  | 18 | Yes | Foreign key to FF_FORMULAS_F. |
| LER_CHG_PLIP_ENRT_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_CHG_PLIP_ENRT_F. |
| ORDR_TO_APLY_NUM | NUMBER |  | 18 |  | Order to apply. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LCHG_PLIP_ENT_RL_F_N1 | Non Unique | Default | LER_CHG_PLIP_ENRT_ID |
| BEN_LCHG_PLIP_ENT_RL_F_PK | Unique | Default | LER_CHG_PLIP_ENRT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
