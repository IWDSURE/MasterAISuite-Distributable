# HWR_REWARD_STATUS

The resume table stores reward status.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrewardstatus-23954.html#hwrrewardstatus-23954](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrewardstatus-23954.html#hwrrewardstatus-23954)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_REWARD_STATUS_PK | REWARD_STATUS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REWARD_STATUS_ID | NUMBER |  | 18 | Yes | This column indicates the reward status ID and is the primary key. |
| REWARD_ID | NUMBER |  | 18 | Yes | This column shows the reward ID. |
| STATUS | VARCHAR2 | 256 |  | Yes | This column indicates whether the reward is paid or not paid. |
| DUE_DATE | DATE |  |  |  | This column indicates the due date of the reward. |
| COMMENT_TEXT | VARCHAR2 | 500 |  |  | This is the comment associated with the reward |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_REWARD_STATUS_N1 | Non Unique | FUSION_TS_TX_DATA | REWARD_ID |
| HWR_REWARD_STATUS_U1 | Unique | FUSION_TS_TX_DATA | REWARD_STATUS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
