# EEC_LB_CONTEST_DETAILS

This table stores the participants consolidated score in a contest.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeclbcontestdetails-18562.html#eeclbcontestdetails-18562](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeclbcontestdetails-18562.html#eeclbcontestdetails-18562)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_LB_CONTEST_DETAILS_PK | CONTEST_LB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEST_LB_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| CONTEST_ID | NUMBER |  |  |  | Foreign key reference of EEC_CONTEST_HDR |
| CONTEST_STAGE_ID | NUMBER |  |  |  | Foreign key reference of EEC_CONTEST_STAGES |
| CONTEST_PARTICIPANT_LINE_ID | NUMBER |  |  |  | Foreign key reference of EEC_CONTEST_PARTICIPANTS |
| TEAM_ID | NUMBER |  |  |  | Foreign key reference of EEC_CONTEST_PARTICIPANTS.TEAM_ID |
| PERSON_ID | NUMBER |  |  |  | Foreign key reference of EEC_CONTEST_PARTICIPANTS.PERSON_ID |
| PARTICIPANT_SCORE | NUMBER |  | 18 |  | Cumulative score of the participant |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| EEC_LB_CONTEST_DETAILS_U1 | Unique | Default | CONTEST_LB_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
