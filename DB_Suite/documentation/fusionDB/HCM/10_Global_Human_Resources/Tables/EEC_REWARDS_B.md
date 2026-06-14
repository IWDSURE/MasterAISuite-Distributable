# EEC_REWARDS_B

This is the base table that stores the Rewards information.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecrewardsb-8796.html#eecrewardsb-8796](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecrewardsb-8796.html#eecrewardsb-8796)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_REWARDS_B_PK | REWARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REWARD_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| POSITION | NUMBER |  |  |  | Position of the reward |
| REWARD_CRITERIA | VARCHAR2 | 30 |  |  | Criteria for the reward |
| THRESHOLD | NUMBER |  | 18 |  | Threshold value of the reward |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether the reward is active or not |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| EEC_REWARDS_B_U1 | Unique | Default | REWARD_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
