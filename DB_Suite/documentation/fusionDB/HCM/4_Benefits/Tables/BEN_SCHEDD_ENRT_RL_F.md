# BEN_SCHEDD_ENRT_RL_F

BEN_SCHEDD_ENRT_RL_F specifies the rules to be enforced  for a particular type of scheduled enrollment period and  for a particular compensation program or plan.  It identifies a rule used to determine enrollment requirements in those cases when the standard, delivered method does not meet the business requirement. . For example , where the scheduled enrollment parameters vary by location, organization unit.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benscheddenrtrlf-14755.html#benscheddenrtrlf-14755](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benscheddenrtrlf-14755.html#benscheddenrtrlf-14755)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_SCHEDD_ENRT_RL_F_PK | SCHEDD_ENRT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDD_ENRT_RL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ORDR_TO_APLY_NUM | NUMBER |  | 18 |  | Order to apply. |
| ENRT_PERD_ID | NUMBER |  | 18 |  | Foreign key to BEN_ENRT_PERD. |
| FORMULA_ID | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
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
| BEN_SCHEDD_ENRT_RL_F_FK2 | Non Unique | Default | ENRT_PERD_ID |
| BEN_SCHEDD_ENRT_RL_F_PK | Unique | Default | SCHEDD_ENRT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
