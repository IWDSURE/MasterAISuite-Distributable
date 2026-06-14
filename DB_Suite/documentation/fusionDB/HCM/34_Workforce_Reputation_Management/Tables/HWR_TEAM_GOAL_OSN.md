# HWR_TEAM_GOAL_OSN

The HWR Team Goal OSN Details are stored in this table

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamgoalosn-17333.html#hwrteamgoalosn-17333](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamgoalosn-17333.html#hwrteamgoalosn-17333)

## Primary Key

| Name | Columns |
|------|----------|
| SYS_C002667297 | TEAM_GOAL_OSN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_GOAL_OSN_ID | NUMBER |  | 19 | Yes | TEAM_GOAL_OSN_ID |
| TEAM_GOAL_ASSOC_ID | NUMBER |  | 19 | Yes | TEAM_GOAL_ASSOC_ID |
| TEAM_ID | NUMBER |  | 19 | Yes | TEAM_ID |
| GOAL_TYPE | VARCHAR2 | 255 |  | Yes | GOAL_TYPE |
| TEAM_NAME | VARCHAR2 | 255 |  | Yes | TEAM_NAME |
| TEAM_GOAL_HEADER | VARCHAR2 | 512 |  | Yes | TEAM_GOAL_HEADER |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DAILY_TARGET_VALUE | VARCHAR2 | 256 |  | Yes | DAILY_TARGET_VALUE |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_GOAL_OSN_U1 | Unique | FUSION_TS_TX_DATA | TEAM_GOAL_OSN_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
