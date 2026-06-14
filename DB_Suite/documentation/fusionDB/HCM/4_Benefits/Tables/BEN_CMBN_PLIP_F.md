# BEN_CMBN_PLIP_F

BEN_CMBN_PLIP_F  is a collection of plans in a program that may provide credits to a participant for enrolling in one or more  plans in the program.  For example, the combination of Vision LTD Plan, Vision STD, and Vision Sick Time may be combined to provide  credits if a participant enrolls in any one of the plans.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencmbnplipf-14855.html#bencmbnplipf-14855](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencmbnplipf-14855.html#bencmbnplipf-14855)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CMBN_PLIP_F_PK | CMBN_PLIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CMBN_PLIP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| NAME | VARCHAR2 | 240 |  |  | Name of the combination plan in program. |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PGM_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PGM_F. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CMBN_PLIP_F_N1 | Non Unique | Default | PGM_ID |
| BEN_CMBN_PLIP_F_N2 | Non Unique | Default | NAME |
| BEN_CMBN_PLIP_F_PK | Unique | Default | CMBN_PLIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
