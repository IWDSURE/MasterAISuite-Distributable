# BEN_POPL_ENRT_TYP_CYCL

BEN_POPL_ENRT_TYP_CYCL keeps track of which program/plan is offered by default or unrestricted modes.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplenrttypcycl-26413.html#benpoplenrttypcycl-26413](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpoplenrttypcycl-26413.html#benpoplenrttypcycl-26413)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_POPL_ENRT_TYP_CYCL_PK | POPL_ENRT_TYP_CYCL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| POPL_ENRT_TYP_CYCL_ID | NUMBER |  | 18 | Yes | Primary Key. ID | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID | Active |
| ENRT_TYP_CYCL_CD | VARCHAR2 | 30 |  | Yes | Enrollment Type Cycle CD U,UO,A,O,L | Active |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F | Active |
| PGM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PGM_F | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Compensation Object Type | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_POPL_ENRT_TYP_CYCL_N1 | Non Unique | Default | PL_ID |
| BEN_POPL_ENRT_TYP_CYCL_N2 | Non Unique | Default | PGM_ID |
| BEN_POPL_ENRT_TYP_CYCL_PK | Unique | Default | POPL_ENRT_TYP_CYCL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
