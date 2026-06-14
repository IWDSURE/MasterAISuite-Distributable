# EEC_CONTEST_UPDATES

This table stores the updates from the contest participants in a contest.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestupdates-25968.html#eeccontestupdates-25968](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestupdates-25968.html#eeccontestupdates-25968)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_CONTEST_UPDATES_PK | UPDATE_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| UPDATE_LINE_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| CONTEST_ID | NUMBER |  |  |  | Foreign key to EEC_CONTEST_HDR |
| PARTICIPANT_LINE_ID | NUMBER |  |  |  | Foreign key to EEC_CONTEST_PARTICIPANTS |
| TEAM_ID | NUMBER |  |  |  | Reference of team id defined in EEC_CONTEST_PARTICIPANTS |
| PERSON_ID | NUMBER |  |  |  | Reference of Person id used in EEC_CONTEST_PARTICIPANTS |
| METRIC_ID | NUMBER |  | 18 |  | Reference of Metric Id used in EEC_CONTEST_METRIC_DETAILS |
| METRIC_WEIGHT | NUMBER |  | 5 |  | Weight of the metric |
| METRIC_SCORE | NUMBER |  | 18 |  | Score of the metric |
| ATTACHMENT | BLOB |  |  |  | Attachment supporting the metric score |
| UPDATE_DATE | TIMESTAMP |  |  | Yes | Date on which the metric is scored |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| UPDATE_COMMENTS | VARCHAR2 | 4000 |  |  | UPDATE_COMMENTS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| EEC_CONTEST_UPDATES_U1 | Unique | Default | UPDATE_LINE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
