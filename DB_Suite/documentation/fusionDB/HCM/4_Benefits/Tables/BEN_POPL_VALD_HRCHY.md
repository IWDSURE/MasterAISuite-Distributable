# BEN_POPL_VALD_HRCHY

BEN_POPL_VALD_HRCHY identifies the various paths within a program or plan not in program hierarchy which are validated against the predefined set of reporting rules.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplvaldhrchy-26764.html#benpoplvaldhrchy-26764](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplvaldhrchy-26764.html#benpoplvaldhrchy-26764)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_POPL_VALD_HRCHY_PK | POPL_VALD_HRCHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPL_VALD_HRCHY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PGM_ID | NUMBER |  | 18 |  | Program ID. |
| PTIP_ID | NUMBER |  | 18 |  | Plan type in program ID. |
| PL_TYP_ID | NUMBER |  | 18 |  | Plan type ID. |
| PLIP_ID | NUMBER |  | 18 |  | Plan in program ID. |
| PL_ID | NUMBER |  | 18 |  | Plan ID. |
| OIPL_ID | NUMBER |  | 18 |  | Option in plan ID. |
| OPT_ID | NUMBER |  | 18 |  | Option ID. |
| PGM_NAME | VARCHAR2 | 1000 |  |  | Program name. |
| PL_TYP_NAME | VARCHAR2 | 1000 |  |  | Plan type name. |
| PL_NAME | VARCHAR2 | 1000 |  |  | Plan name. |
| OPT_NAME | VARCHAR2 | 1000 |  |  | Option name. |
| EFFECTIVE_DATE | DATE |  |  |  | Effective date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS. |
| PTIP_ORDR_NUM | NUMBER |  | 18 |  | Plan type in program order number. |
| PLIP_ORDR_NUM | NUMBER |  | 18 |  | Plan in program order number. |
| OIPL_ORDR_NUM | NUMBER |  | 18 |  | Option in plan order number. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_POPL_VALD_HRCHY_PK | Unique | Default | POPL_VALD_HRCHY_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
