# EEC_CONTEST_STAGES

This table stores the stages of the contest in a competition.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecconteststages-18032.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eecconteststages-18032.html)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_CONTEST_STAGES_PK | CONTEST_STAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEST_STAGE_ID | NUMBER |  | 18 | Yes | System generated key for this entry |
| CONTEST_ID | NUMBER |  | 18 |  | Foreign key to store the contest |
| STAGE_NAME | VARCHAR2 | 200 |  |  | Name of the Stage |
| STAGE_DESCRIPTION | VARCHAR2 | 200 |  |  | Description of Stage |
| STAGE_ORDER | NUMBER |  | 2 |  | Order of the Stage |
| START_DATE | TIMESTAMP |  |  |  | Start date of the stage |
| END_DATE | TIMESTAMP |  |  |  | End date of the Stage |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| EEC_CONTEST_STAGES_U1 | Unique | Default | CONTEST_STAGE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
