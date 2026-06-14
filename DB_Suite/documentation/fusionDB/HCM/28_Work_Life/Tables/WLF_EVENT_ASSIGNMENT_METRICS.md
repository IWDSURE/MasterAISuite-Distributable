# WLF_EVENT_ASSIGNMENT_METRICS

Table to store assignment profile metrics.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventassignmentmetrics-6521.html#wlfeventassignmentmetrics-6521](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventassignmentmetrics-6521.html#wlfeventassignmentmetrics-6521)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_event_assignment_metri_PK | METRICS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| METRICS_ID | NUMBER |  | 18 | Yes | Primary key, uniquely identifies each metrics record |
| EVENT_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Foreign key linking to the event assignment |
| ADD_PERSON_IDS_COUNT | NUMBER |  | 18 |  | Count of persons newly added |
| WITHDRAW_PERSON_IDS_COUNT | NUMBER |  | 18 |  | Count of persons withdrawn |
| REACTIVE_PERSON_IDS_COUNT | NUMBER |  | 18 |  | Count of persons reactivated |
| LATEST_JOB_ID | NUMBER |  | 18 |  | Job identifier of the latest processing |
| ASSIGNED_TO_COUNT | NUMBER |  | 18 |  | Total learners count |
| LATEST_RUN_DURATION | NUMBER |  | 18 |  | Latest processing duration |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ASSIGNMENT_MTRCS_N1 | Non Unique | Default | EVENT_ASSIGNMENT_ID |
| WLF_ASSIGNMENT_MTRCS_U1 | Unique | Default | METRICS_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
