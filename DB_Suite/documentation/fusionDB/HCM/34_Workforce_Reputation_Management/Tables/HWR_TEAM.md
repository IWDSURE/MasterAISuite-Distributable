# HWR_TEAM

The HWR Team Details are stored in this table

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteam-29480.html#hwrteam-29480](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteam-29480.html#hwrteam-29480)

## Primary Key

| Name | Columns |
|------|----------|
| SYS_C002629072 | TEAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_ID | NUMBER |  | 19 | Yes | TEAM_ID |
| TEAM_NAME | VARCHAR2 | 255 |  | Yes | TEAM_NAME |
| DESCRIPTION | VARCHAR2 | 3000 |  |  | DESCRIPTION |
| EFFECTIVE_DATE | TIMESTAMP |  |  | Yes | EFFECTIVE_DATE |
| SOURCE_APPLICATION | VARCHAR2 | 255 |  | Yes | SOURCE_APPLICATION |
| STATUS | VARCHAR2 | 20 |  | Yes | STATUS |
| IS_PRIVATE | NUMBER |  |  |  | This column is to indicate if the team is public or private |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| SOURCE_ID | NUMBER |  | 18 |  | This column is to store the source_id when a team object is synced with the default conversationapart from OSN. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column is to store the conversation_id when a team object is synced with the default conversationapart from OSN. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_TEAM_U1 | Unique | FUSION_TS_TX_DATA | TEAM_ID |  |
| HWR_TEAM_U2 | Unique | FUSION_TS_TX_DATA | TEAM_NAME | Obsolete |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
