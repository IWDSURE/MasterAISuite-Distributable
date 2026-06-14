# HXT_TM_MTRX_TBB_USGS

Interface table between UI Time Entries Table (HXT_TM_MTRX) and Time Building Blocks Table (HXT_TM_BLDG_BLKS).

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxtbbusgs-27251.html#hxttmmtrxtbbusgs-27251](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxtbbusgs-27251.html#hxttmmtrxtbbusgs-27251)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TM_MTRX_TBB_USGS_PK | TM_MTRX_TBB_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_MTRX_TBB_USAGE_ID | NUMBER |  | 18 | Yes | Primary Key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_MTRX_ROW_ID | NUMBER |  | 18 | Yes | Foriegn key to HXT_TM_MTRX table |
| TM_BLDG_BLK_DTL_ID1 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID2 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID3 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID4 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID5 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID6 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID7 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID8 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID9 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID10 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID11 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID12 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID13 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID14 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID15 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID16 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID17 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID18 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID19 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID20 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID21 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID22 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID23 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID24 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID25 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID26 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID27 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID28 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID29 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID30 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_ID31 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block Id. |
| TM_BLDG_BLK_DTL_VERSION1 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION2 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION3 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION4 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION5 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION6 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION7 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION8 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION9 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION10 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION11 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION12 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION13 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION14 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION15 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION16 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION17 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION18 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION19 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION20 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION21 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION22 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION23 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION24 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION25 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION26 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION27 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION28 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION29 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION30 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| TM_BLDG_BLK_DTL_VERSION31 | NUMBER |  | 18 |  | Foreign Key to HXT_TM_BLDG_BLKS table. Mapped Detail Scope Time building block version. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TM_MTRX_TBB_USGS_PK | Unique | Default | TM_MTRX_TBB_USAGE_ID |
| HXT_TM_MTRX_TBB_USGS_U1 | Unique | Default | TM_MTRX_ROW_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
