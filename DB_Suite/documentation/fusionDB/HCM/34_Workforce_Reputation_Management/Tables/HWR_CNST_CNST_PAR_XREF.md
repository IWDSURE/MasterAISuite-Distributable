# HWR_CNST_CNST_PAR_XREF

Connects tables HWR_CNST_B and HWR_CNST_PAR_IND_B.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstcnstparxref-13542.html#hwrcnstcnstparxref-13542](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstcnstparxref-13542.html#hwrcnstcnstparxref-13542)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_CNST_PAR_XREF_PK | CONTEST_ID, CONTEST_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEST_ID | NUMBER |  | 18 | Yes | References CONTEST_ID column in HWR_CNST_B table |
| CONTEST_PARTICIPANT_ID | NUMBER |  | 18 | Yes | References CONTEST_PARTICIPANT_ID column in HWR_CNST_PAR_IND table |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of conversation. |
| REWARD_STATUS_ID | NUMBER |  | 18 |  | This column indicates the reward status ID. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_CNST_PAR_XREF_N1 | Non Unique | FUSION_TS_TX_DATA | CONTEST_PARTICIPANT_ID |
| HWR_CNST_CNST_PAR_XREF_U1 | Unique | FUSION_TS_TX_DATA | CONTEST_ID, CONTEST_PARTICIPANT_ID |
| HWR_CNST_CNST_PAR_XREF_U2 | Unique | FUSION_TS_TX_DATA | REWARD_STATUS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
