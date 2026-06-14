# BEN_PER_INFO_CHG_CS_LER

BEN_PER_INFO_CHG_CS_LER_F identifies a specific change to a column in a table that, when combined with others, make up a profile from which life events can be detected as person's data change.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperinfochgcsler-23603.html#benperinfochgcsler-23603](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperinfochgcsler-23603.html#benperinfochgcsler-23603)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_INFO_CHG_CS_LER_PK | PER_INFO_CHG_CS_LER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PER_INFO_CHG_CS_LER_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS | Active |
| PER_INFO_CHG_CS_LER_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. | Active |
| OLD_VAL | VARCHAR2 | 180 |  |  | Old value. | Active |
| NEW_VAL | VARCHAR2 | 180 |  |  | New value. | Active |
| SOURCE_COLUMN | VARCHAR2 | 90 |  | Yes | Source column. | Active |
| SOURCE_TABLE | VARCHAR2 | 90 |  | Yes | Source table. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| NAME | VARCHAR2 | 600 |  |  | Name of the personal information that causes the life event. | Active |
| WHATIF_LBL_TXT | VARCHAR2 | 300 |  |  | What-if label text. | Active |
| RULE_OVERRIDES_FLAG | VARCHAR2 | 30 |  | Yes | Rule Overrides Y or N | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_INFO_CHG_CS_LER_N1 | Non Unique |  | NAME |
| BEN_PER_INFO_CHG_CS_LER_PK | Unique | Default | PER_INFO_CHG_CS_LER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
