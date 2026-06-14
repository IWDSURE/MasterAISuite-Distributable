# EEC_CONTEST_METRIC_DETAILS

This table stores the metrics associated with the contest.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestmetricdetails-9871.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontestmetricdetails-9871.html)

## Primary Key

| Name | Columns |
|------|----------|
| EEC_CONTEST_METRIC_DETAIL_PK | METRIC_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| METRIC_LINE_ID | NUMBER |  |  | Yes | System generated number to store the metric line id |
| CONTEST_ID | NUMBER |  |  |  | Foreign key reference of contest id |
| METRIC_ID | NUMBER |  |  |  | Foreign key reference of metric id |
| ATTACHMENT_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether attachments are allowed or not |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether the metric is active or not for the contest |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| EEC_CONTEST_METRIC_DETAILS_U1 | Unique | Default | METRIC_LINE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
