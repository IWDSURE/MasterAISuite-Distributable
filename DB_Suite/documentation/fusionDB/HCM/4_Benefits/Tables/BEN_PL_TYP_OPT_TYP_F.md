# BEN_PL_TYP_OPT_TYP_F

BEN_PL_TYP_OPT_TYP_F identifies the specific plan types and the option types that are valide for each plan type.  This enables the presentation of only  those options valid for a certain plan type, for example,  medical plan types offer coverage options of employee only, employee plus one and employee plus family  life, insurance type plans offer options of 1 times pay and 2 times pay.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpltypopttypf-7861.html#benpltypopttypf-7861](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpltypopttypf-7861.html#benpltypopttypf-7861)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_TYP_OPT_TYP_F_PK | PL_TYP_OPT_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_TYP_OPT_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PL_TYP_OPT_TYP_CD | VARCHAR2 | 30 |  | Yes | Option type. |
| PL_TYP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PL_TYP_F. |
| OPT_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_OPT_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further identifies the legislation of startup data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_TYP_OPT_TYP_F_N1 | Non Unique | Default | PL_TYP_ID |
| BEN_PL_TYP_OPT_TYP_F_N2 | Non Unique | Default | OPT_ID |
| BEN_PL_TYP_OPT_TYP_F_PK | Unique | Default | PL_TYP_OPT_TYP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
