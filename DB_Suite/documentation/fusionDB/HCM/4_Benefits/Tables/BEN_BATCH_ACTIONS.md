# BEN_BATCH_ACTIONS

BEN_BATCH_ACTIONS stores the statistical data about each benefits process that was run.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchactions-19466.html#benbatchactions-19466](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchactions-19466.html#benbatchactions-19466)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_ACTIONS_PK | BATCH_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| BATCH_ACTION_ID | NUMBER |  |  | Yes | System generated primary key column. | Active |
| BATCH_ID | NUMBER |  |  | Yes | Unique Identifier for a batch. | Active |
| BATCH_TYPE | VARCHAR2 | 30 |  | Yes | Type of the batch. | Active |
| ROLLUP_COUNT | NUMBER |  |  |  | The rollup count. | Active |
| ROLLUP_SUMOVN | NUMBER |  |  |  | The rollup sum. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BATCH_ACTIONS_FK1 | Non Unique | FUSION_TS_TX_DATA | BATCH_ID |
| BEN_BATCH_ACTIONS_PK1 | Unique | FUSION_TS_TX_DATA | BATCH_ACTION_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
