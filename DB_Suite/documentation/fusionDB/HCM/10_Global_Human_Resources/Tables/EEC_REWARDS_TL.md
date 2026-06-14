# EEC_REWARDS_TL

This is the translated table that stores the Rewards information.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecrewardstl-15428.html#eecrewardstl-15428](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecrewardstl-15428.html#eecrewardstl-15428)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_REWARDS_TL_PK | REWARD_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REWARD_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 200 |  |  | Name of the reward |
| REWARD_PRIZE | VARCHAR2 | 500 |  |  | Prize for the reward |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| EEC_REWARDS_TL_U1 | Unique | Default | REWARD_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
