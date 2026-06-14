# BEN_POPL_ACTN_TYP_F

BEN_POPL_ACTN_TYP_F  identifies the length of time a person will have to satisfy the requirements of an action type and may be defined for program or plans in programs or plans not in programs.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplactntypf-15711.html#benpoplactntypf-15711](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplactntypf-15711.html#benpoplactntypf-15711)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_POPL_ACTN_TYP_F_PK | POPL_ACTN_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPL_ACTN_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ACTN_TYP_DUE_DT_CD | VARCHAR2 | 30 |  |  | Action item type due date code. |
| ACTN_TYP_DUE_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ACTN_TYP_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTN_TYP_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F |
| SSPND_FLAG | VARCHAR2 | 30 |  |  | Suspend Flag |
| CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | Certification Determincation Code. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent table discriminator. |
| ACTN_TYP_CD | VARCHAR2 | 30 |  |  | ACTN_TYP_CD |
| ACTN_TYP_LVL_CD | VARCHAR2 | 30 |  |  | ACTN_TYP_LVL_CD |
| PTIP_ID | NUMBER |  |  |  | PTIP_ID |
| RQD_FLAG | VARCHAR2 | 30 |  |  | RQD_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_POPL_ACTN_TYP_F_FK3 | Non Unique | Default | ACTN_TYP_ID |
| BEN_POPL_ACTN_TYP_F_N2 | Non Unique | Default | PL_ID |
| BEN_POPL_ACTN_TYP_F_N3 | Non Unique |  | OIPL_ID |
| BEN_POPL_ACTN_TYP_F_N4 | Non Unique |  | PTIP_ID |
| BEN_POPL_ACTN_TYP_F_PK | Unique | Default | POPL_ACTN_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
