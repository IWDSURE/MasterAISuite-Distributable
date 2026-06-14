# HWR_CNST_LDR_BRD_POS_B

This table stores the postions of the leader board table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstldrbrdposb-11852.html#hwrcnstldrbrdposb-11852](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstldrbrdposb-11852.html#hwrcnstldrbrdposb-11852)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_LDR_BRD_POS_B_PK | LEADER_BOARD_POSITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LEADER_BOARD_POSITION_ID | NUMBER |  | 18 | Yes | This column is the primary key of the table |  |
| RANK | NUMBER |  | 18 |  | This column reference RANK column in HWR_CNST_LDR_BRD_B |  |
| RECENT_ACTIVITY_CONSIDERED | TIMESTAMP |  |  |  | This column reference RECENT_ACTIVITY_CONSIDERED column in HWR_CNST_LDR_BRD_B |  |
| LEADER_BOARD_ID | NUMBER |  | 18 | Yes | This column reference LEADER_BOARD_ID column in HWR_CNST_LDR_BRD_B |  |
| NAME | VARCHAR2 | 256 |  | Yes | This column contains the name of the leader board position tuple. | Obsolete |
| POINTS | NUMBER |  |  | Yes | The column contains the points of the leader board postion tuple. |  |
| CONTEST_PARTICIPANT_ID | NUMBER |  | 18 |  | This column is a foreign key to HWR_CNST_PAR_IND_B table |  |
| RANK_FLAG | NUMBER |  | 18 |  | This column shows if the currnent position has moved up, down, or has not changed. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_LDR_BRD_POS_B_N1 | Non Unique | FUSION_TS_TX_DATA | LEADER_BOARD_ID |
| HWR_CNST_LDR_BRD_POS_B_N2 | Non Unique | FUSION_TS_TX_DATA | CONTEST_PARTICIPANT_ID |
| HWR_CNST_LDR_BRD_POS_B_U1 | Unique | FUSION_TS_TX_DATA | LEADER_BOARD_POSITION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
