# HTS_MSGS

Information associated with a messages related to internalization of imported shifts.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsmsgs-11005.html#htsmsgs-11005](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsmsgs-11005.html#htsmsgs-11005)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_MSGS_PK | HTS_MSGS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HTS_MSGS_ID | NUMBER |  | 18 | Yes | HTS_MSGS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MASTER_JOB_ID | NUMBER |  | 18 |  | MASTER_JOB_ID |
| SLAVE_JOB_ID | NUMBER |  | 18 |  | SLAVE_JOB_ID |
| SCHED_REQUEST_ID | NUMBER |  | 18 |  | SCHED_REQUEST_ID |
| SCHED_EVENT_ID | NUMBER |  | 18 |  | SCHED_EVENT_ID |
| SCHED_SHIFT_EVENT_ID | NUMBER |  | 18 |  | SCHED_SHIFT_EVENT_ID |
| SCHED_SHIFT_ATRB_ID | NUMBER |  | 18 |  | SCHED_SHIFT_ATRB_ID |
| RESOURCE_ASSIGN_ID | NUMBER |  | 18 |  | RESOURCE_ASSIGN_ID |
| MESSAGE_FIELD | VARCHAR2 | 256 |  |  | MESSAGE_FIELD |
| MESSAGE_NAME | VARCHAR2 | 256 |  | Yes | MESSAGE_FIELD |
| APPLICATION_ID | NUMBER |  | 16 | Yes | APPLICATION_ID instead of short name, since the name can change |
| APPLICATION_SHORT_NAME | VARCHAR2 | 30 |  |  | APPLICATION_SHORT_NAME |
| MESSAGE_LEVEL | VARCHAR2 | 30 |  | Yes | MESSAGE_LEVEL |
| DATE_FROM | TIMESTAMP |  |  | Yes | DATE_FROM |
| DATE_TO | TIMESTAMP |  |  |  | DATE_TO |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_MSGS_U1 | Unique | Default | HTS_MSGS_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
