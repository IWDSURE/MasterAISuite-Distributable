# BEN_POPL_RPTG_GRP_F

BEN_POPL_RPTG_GRP_F establishes affinity between a program or plan and a reporting group.  Plans and programs are grouped together for a number of reasons ,more importantly, however, the plan sponsor may have to group plans or programs in order to identify that they are, in essence, the same thing.This is necessary in those cases when for plan design purposes, the user must create multiple plan records for the same underlying plan. For example, they are reported together as a group for regulatory purposes, their financial statements are combined, the participants are reported against as a group.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplrptggrpf-14837.html#benpoplrptggrpf-14837](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplrptggrpf-14837.html#benpoplrptggrpf-14837)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_POPL_RPTG_GRP_F_PK | POPL_RPTG_GRP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPL_RPTG_GRP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| RPTG_GRP_ID | NUMBER |  | 18 |  | Foreign key to BEN_RPTG_GRP. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORDR_NUM | NUMBER |  | 18 |  | Order Number |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent table discriminator. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_POPL_RPTG_GRP_F_FK3 | Non Unique | Default | RPTG_GRP_ID |
| BEN_POPL_RPTG_GRP_F_N1 | Non Unique | Default | PGM_ID |
| BEN_POPL_RPTG_GRP_F_N2 | Non Unique | Default | PL_ID |
| BEN_POPL_RPTG_GRP_F_PK | Unique | Default | POPL_RPTG_GRP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
