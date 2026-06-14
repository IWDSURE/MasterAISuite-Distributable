# HWR_GOAL_F

The goal table stores wellness user fitness goals.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgoalf-10689.html#hwrgoalf-10689](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgoalf-10689.html#hwrgoalf-10689)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_GOAL_F_PK | GOAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | This is column stores unique goal ID field |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of conversation. |
| GOAL_METRIC | VARCHAR2 | 512 |  | Yes | This is column stores the metric of the goal. |
| LOWER_BOUND | NUMBER |  |  |  | This stores the lower bound of the goal metric. |
| UPPER_BOUND | NUMBER |  |  |  | This stores the upper bound value for the Goal Metric |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| UNITS | VARCHAR2 | 50 |  |  | This stores the units to be used for reading the goals |
| FREQUENCY | VARCHAR2 | 50 |  |  | This stores the frequency of the wellness user data goal. |
| GOAL_TYPE | VARCHAR2 | 80 |  |  | This is column stores the goal type. |
| CATEGORY | VARCHAR2 | 256 |  |  | This column shows whether this goal is wellness program goal or user goal. |
| GOAL_NAME | VARCHAR2 | 400 |  |  | This is the name associated with the goal being represented. |
| PARTICIPATION_RATE_TARGET | NUMBER |  | 18 |  | This column stores the target participation rate. |
| REWARD_ID | NUMBER |  | 18 |  | This column stores the reward id for the corresponding goal. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_GOAL_F_N1 | Non Unique | FUSION_TS_TX_DATA | REWARD_ID |
| HWR_GOAL_F_U1 | Unique | FUSION_TS_TX_DATA | GOAL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
