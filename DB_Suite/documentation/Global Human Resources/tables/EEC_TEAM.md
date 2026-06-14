# EEC_TEAM

This table stores team information details of a contest.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecteam-13845.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecteam-13845.html)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_TEAM_PK | TEAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| CONTEST_ID | NUMBER |  | 18 |  | Foreign key reference to EEC_CONTEST_HDR |
| TEAM_NAME | VARCHAR2 | 200 |  |  | Name of the team |
| TEAM_DESC | VARCHAR2 | 4000 |  |  | Description of the team |
| TEAM_LOGO | BLOB |  |  |  | Logo of the team |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether the team is active or not |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| EEC_TEAM_U1 | Unique | Default | TEAM_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
