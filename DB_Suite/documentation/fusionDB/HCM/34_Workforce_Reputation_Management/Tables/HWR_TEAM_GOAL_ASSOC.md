# HWR_TEAM_GOAL_ASSOC

The HWR Team and Goall Association details are stored in this table

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamgoalassoc-10369.html#hwrteamgoalassoc-10369](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamgoalassoc-10369.html#hwrteamgoalassoc-10369)

## Primary Key

| Name | Columns |
|------|----------|
| SYS_C002667201 | TEAM_GOAL_ASSOC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_GOAL_ASSOC_ID | NUMBER |  | 19 | Yes | TEAM_GOAL_ASSOC_ID |
| GOAL_ID | NUMBER |  | 19 | Yes | GOAL_ID |
| TEAM_ID | NUMBER |  | 19 | Yes | TEAM_ID |
| SOURCE_ID | NUMBER |  | 18 |  | This column is to store the source_id when a team goal assoc object is synced with the default conversationapart from OSN. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column is to store the conversation_id when a teamgoal assoc object is synced with the default conversationapart from OSN. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| IS_DELETED | NUMBER |  |  |  | IS_DELETED |
| DELETED_BY | VARCHAR2 | 50 |  |  | DELETED_BY |
| DELETION_DATE | TIMESTAMP |  |  |  | DELETION_DATE |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_GOAL_ASSOC_U1 | Unique | FUSION_TS_TX_DATA | TEAM_GOAL_ASSOC_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
