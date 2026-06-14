# BEN_CSS_RLTD_PER_PER_IN_LER

BEN_CSS_RLTD_PER_PER_IN_LER  identifies which life event reported by or detected for a participant may spawn a life event for other persons related to him or her.   For example, a triggered life event of death for a participant causes a loss of coverage life event to related persons.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencssrltdperperinler-15544.html#bencssrltdperperinler-15544](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencssrltdperperinler-15544.html#bencssrltdperperinler-15544)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CSS_RLTD_PER_PER_IN_L_PK | CSS_RLTD_PER_PER_IN_LER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CSS_RLTD_PER_PER_IN_LER_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| ORDR_TO_PRCS_NUM | NUMBER |  | 18 |  | Order to process. | Active |
| LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_LER_F. | Active |
| RSLTG_LER_ID | NUMBER |  | 18 | Yes | Foreign key top BEN_LER_F. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CSS_RLTD_PER_PER_IN_LER_N1 | Non Unique | Default | LER_ID |
| BEN_CSS_RLTD_PER_PER_IN_LER_N2 | Non Unique | Default | RSLTG_LER_ID |
| BEN_CSS_RLTD_PER_PER_IN_LER_PK | Unique | Default | CSS_RLTD_PER_PER_IN_LER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
