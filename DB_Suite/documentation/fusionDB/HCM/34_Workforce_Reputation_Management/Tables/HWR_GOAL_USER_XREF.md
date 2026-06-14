# HWR_GOAL_USER_XREF

This cross reference (xref) table stores relationship between goal and wellness user.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgoaluserxref-21372.html#hwrgoaluserxref-21372](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgoaluserxref-21372.html#hwrgoaluserxref-21372)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_GOAL_USER_XREF_PK | GOAL_ID, USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | This is the primary key for the wellness user goal table. |
| USER_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the wellness user table. |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of conversation. |
| REWARD_STATUS_ID | NUMBER |  | 18 |  | This column is a foreign key to HWR_REWARD_STATUS.REWARD_STATUS_ID. |
| ACCOMPLISHMENT_DATE | DATE |  |  |  | This column indicates when the goal has been reached by the user. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_GOAL_USER_XREF_N1 | Non Unique | FUSION_TS_TX_DATA | USER_ID |
| HWR_GOAL_USER_XREF_U1 | Unique | FUSION_TS_TX_DATA | GOAL_ID, USER_ID |
| HWR_GOAL_USER_XREF_U2 | Unique | FUSION_TS_TX_DATA | REWARD_STATUS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
