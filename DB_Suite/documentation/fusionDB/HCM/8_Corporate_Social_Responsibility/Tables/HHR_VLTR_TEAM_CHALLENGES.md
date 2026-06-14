# HHR_VLTR_TEAM_CHALLENGES

This table stores the information about team challenges.

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrteamchallenges-3051.html#hhrvltrteamchallenges-3051](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrteamchallenges-3051.html#hhrvltrteamchallenges-3051)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_TEAM_CHALLENGES_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |
| USER_ID | NUMBER |  | 18 | Yes | USER_ID |
| CHALLENGING_TEAM_ID | NUMBER |  | 18 | Yes | CHALLENGING_TEAM_ID |
| CHALLENGED_TEAM_ID | NUMBER |  | 18 | Yes | CHALLENGED_TEAM_ID |
| CHALLENGE_STATUS | NUMBER |  | 18 | Yes | CHALLENGE_STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_VLTR_TEAM_CHALLENGES_U1 | Unique | FUSION_TS_TX_IDX | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
