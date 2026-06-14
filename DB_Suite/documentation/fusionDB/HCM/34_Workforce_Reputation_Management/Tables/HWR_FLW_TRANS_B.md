# HWR_FLW_TRANS_B

The transition table is used to store transitions.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwtransb-23450.html#hwrflwtransb-23450](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwtransb-23450.html#hwrflwtransb-23450)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_FLW_TRANS_B_PK | FLOW_ID, TO_STEP_ID, FROM_STEP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FLOW_ID | NUMBER |  | 18 | Yes | This is the flow id and is also part of the composed primary key. | Active |
| TO_STEP_ID | NUMBER |  | 18 | Yes | This is the FROM step id and is also part of the composed primary key. | Active |
| FROM_STEP_ID | NUMBER |  | 18 | Yes | This is the TO step id and is also part of the composed primary key. | Active |
| BRANCH_INDEX | NUMBER |  | 18 | Yes | Represents the branch index of the transition from the source step. This index is 1 based. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_FLW_TRANS_B_N1 | Non Unique | FUSION_TS_TX_DATA | FROM_STEP_ID |  |
| HWR_FLW_TRANS_B_N2 | Non Unique | FUSION_TS_TX_DATA | TO_STEP_ID |  |
| HWR_FLW_TRANS_B_U1 | Unique | FUSION_TS_TX_DATA | FLOW_ID, TO_STEP_ID, FROM_STEP_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
