# EEC_CONTEST_HDR

This table stores all the Contests run in the Organization.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontesthdr-22873.html#eeccontesthdr-22873](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontesthdr-22873.html#eeccontesthdr-22873)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_CONTEST_HDR_PK | CONTEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEST_ID | NUMBER |  | 18 | Yes | System generated key to store the contest id |
| CONTEST_NAME | VARCHAR2 | 200 |  |  | Contest Name of the contest |
| OBJECTIVE | VARCHAR2 | 4000 |  |  | Objective of the contest |
| PARENT_CONTEST_ID | NUMBER |  |  |  | Stores Parent Contest Id |
| CONTEST_STAGE_ID | NUMBER |  |  |  | Stores Contest Stage Id |
| IMAGE | BLOB |  |  |  | Image of the Contest |
| CONTEST_START_DATE | TIMESTAMP |  |  |  | Start Date of the Contest |
| CONTEST_END_DATE | TIMESTAMP |  |  |  | End Date of the Contest |
| VOTING_START_DATE | TIMESTAMP |  |  |  | Start Date of Voting |
| VOTING_END_DATE | TIMESTAMP |  |  |  | End Date of Voting |
| CONTEST_TYPE | VARCHAR2 | 30 |  |  | Type of the Contest |
| PARTICIPANT_TYPE | VARCHAR2 | 30 |  |  | Type of Participant |
| UPDATE_OWNER | VARCHAR2 | 30 |  |  | Owner type who is allowed to update the contest |
| ALLOW_UPDATES_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether the contest can be updated |
| STATUS | VARCHAR2 | 30 |  |  | Status of the Contest |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Enabled Flag of the Contest |
| VISIBILITY | VARCHAR2 | 30 |  |  | To whom the contest should be visible |
| WIN_CRITERIA | VARCHAR2 | 30 |  |  | Winning Criteria of the contest |
| AWARD_TYPE | VARCHAR2 | 30 |  |  | Type of the Award |
| TIE_WINNER | VARCHAR2 | 30 |  |  | Deciding the winner in case of Tie |
| TEMPLATE_ID | NUMBER |  |  |  | Template Id on which the contest is created |
| INSTRUCTIONS | VARCHAR2 | 4000 |  |  | Instructions to the participants |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| EEC_CONTEST_HDR_U1 | Unique | Default | CONTEST_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
