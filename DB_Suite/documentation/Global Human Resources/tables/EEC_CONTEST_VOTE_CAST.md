# EEC_CONTEST_VOTE_CAST

This table stores the voting information for the contest participants in a contest.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestvotecast-24766.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestvotecast-24766.html)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_CONTEST_VOTE_CAST_PK | VOTE_CAST_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VOTE_CAST_LINE_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| CONTEST_ID | NUMBER |  |  |  | Foreign key reference of EEC_CONTEST_HDR |
| VOTER_PARTICIPANT_ID | NUMBER |  |  |  | Voter person id who has voted |
| TEAM_ID | NUMBER |  |  |  | Team id reference of EEC_CONTEST_PARTICIPANTS for whom the vote has been cast |
| PERSON_ID | NUMBER |  |  |  | Person id reference of EEC_CONTEST_PARTICIPANTS for whom the vote has been cast |
| VOTING_POINTS | NUMBER |  |  |  | Voting points given for the voting. |
| VOTE_UPDATE_DATE | TIMESTAMP |  |  | Yes | Date on which vote has been updated |
| STATUS | VARCHAR2 | 30 |  |  | Status of the vote |
| VOTER_COMMENTS | VARCHAR2 | 4000 |  |  | Comments from the voter |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| EEC_CONTEST_VOTE_CAST_U1 | Unique | Default | VOTE_CAST_LINE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
