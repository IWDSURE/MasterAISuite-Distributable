# EEC_CONTEST_VOTERS

This table stores the voters information in a contest.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestvoters-11270.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestvoters-11270.html)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_CONTEST_VOTERS_PK | VOTER_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VOTER_LINE_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| CONTEST_ID | NUMBER |  |  |  | Foreign key reference to EEC_CONTEST_HDR |
| VOTER_PARTICIPANT_ID | NUMBER |  |  |  | Person id of the voter who has been registered for the contest |
| VOTER_TYPE | VARCHAR2 | 30 |  |  | Type of the voter |
| VOTING_LIMT | NUMBER |  |  |  | Voting limit. Default it is 1. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether the voter is active or not |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| EEC_CONTEST_VOTERS_U1 | Unique | Default | VOTER_LINE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
