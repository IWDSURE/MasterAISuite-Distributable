# HWR_TEAM_CHALLENGE

The HWR Team Challenge details are stored in this table

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamchallenge-27142.html#hwrteamchallenge-27142](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamchallenge-27142.html#hwrteamchallenge-27142)

## Primary Key

| Name | Columns |
|------|----------|
| SYS_C002667232 | CHALLENGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHALLENGE_ID | NUMBER |  | 19 | Yes | CHALLENGE_ID |
| SOURCE_TEAM_ID | NUMBER |  | 19 | Yes | SOURCE_TEAM_ID |
| SOURCE_GOAL_ID | NUMBER |  | 19 | Yes | SOURCE_GOAL_ID |
| TARGET_TEAM_ID | NUMBER |  | 19 | Yes | TARGET_TEAM_ID |
| TARGET_GOAL_ID | NUMBER |  |  |  | TARGET_GOAL_ID |
| STATUS | VARCHAR2 | 256 |  |  | STATUS |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_CHALLENGE_U1 | Unique | FUSION_TS_TX_DATA | CHALLENGE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
