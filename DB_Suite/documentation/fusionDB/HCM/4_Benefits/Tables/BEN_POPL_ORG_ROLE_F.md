# BEN_POPL_ORG_ROLE_F

BEN_POPL_ORG_ROLE_F identifies the services or functions performed by an organization for this program or plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplorgrolef-15912.html#benpoplorgrolef-15912](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplorgrolef-15912.html#benpoplorgrolef-15912)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_POPL_ORG_ROLE_F_PK | POPL_ORG_ROLE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPL_ORG_ROLE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the organization role in the program or plan. |
| POPL_ORG_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_POPL_ORG_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORG_ROLE_TYP_CD | VARCHAR2 | 30 |  | Yes | Organization role type. |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent table discriminator. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_POPL_ORG_ROLE_F_N1 | Non Unique | Default | POPL_ORG_ID |
| BEN_POPL_ORG_ROLE_F_N2 | Non Unique |  | NAME |
| BEN_POPL_ORG_ROLE_F_PK | Unique | Default | POPL_ORG_ROLE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
