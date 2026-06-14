# CMP_CWB_MODEL_DTL

CMP_CWB_MODEL_DTL identifies the
                                         details of a particular matrix row.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodeldtl-30540.html#cmpcwbmodeldtl-30540](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodeldtl-30540.html#cmpcwbmodeldtl-30540)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_MODEL_DTL_PK | MODEL_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_DTL_ID | NUMBER |  | 18 | Yes | System generated primary key
                                               column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| MODEL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_CWB_MATRIX. |
| CRIT1_VAL | VARCHAR2 | 150 |  | Yes | First criteria value. |
| CRIT2_VAL | VARCHAR2 | 150 |  |  | Second criteria value. |
| CRIT3_VAL | VARCHAR2 | 150 |  |  | Third Criteria Value |
| CRIT4_VAL | VARCHAR2 | 150 |  |  | Criteria Value |
| NUM_VAL1 | NUMBER |  |  |  | Number Value |
| NUM_VAL2 | NUMBER |  |  |  | Number Value |
| TEXT_VAL | VARCHAR2 | 150 |  |  | TEXT_VAL |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| DATE_VAL | DATE |  |  |  | DATE_VAL |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_MODEL_DTL_N1 | Non Unique | Default | MODEL_ID, CRIT1_VAL, CRIT2_VAL, CRIT3_VAL, CRIT4_VAL |
| CMP_CWB_MODEL_DTL_UK1 | Unique | Default | MODEL_DTL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
