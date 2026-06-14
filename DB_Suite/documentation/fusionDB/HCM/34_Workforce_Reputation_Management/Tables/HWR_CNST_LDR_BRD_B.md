# HWR_CNST_LDR_BRD_B

This table contians the leader board information for contests

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstldrbrdb-13021.html#hwrcnstldrbrdb-13021](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstldrbrdb-13021.html#hwrcnstldrbrdb-13021)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_LDR_BRD_B_PK | LEADER_BOARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEADER_BOARD_ID | NUMBER |  | 18 | Yes | This column is the primary key of the table |
| NAME | VARCHAR2 | 512 |  | Yes | This column contains the name of the leader board. |
| CONTEST_ID | NUMBER |  | 18 | Yes | This columns references the HWR_CNST_B table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_LDR_BRD_B_N1 | Non Unique | FUSION_TS_TX_DATA | CONTEST_ID |
| HWR_CNST_LDR_BRD_B_U1 | Unique | FUSION_TS_TX_DATA | LEADER_BOARD_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
