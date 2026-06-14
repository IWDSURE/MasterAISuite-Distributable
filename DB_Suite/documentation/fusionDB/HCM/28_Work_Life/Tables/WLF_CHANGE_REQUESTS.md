# WLF_CHANGE_REQUESTS

Table to store change requests to be processed by ESS jobs.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfchangerequests-22935.html#wlfchangerequests-22935](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfchangerequests-22935.html#wlfchangerequests-22935)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CHANGE_REQUESTS_PK | CHANGE_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANGE_REQUEST_ID | NUMBER |  | 18 | Yes | Primary Key for change requests |
| OBJECT_ID | NUMBER |  | 18 | Yes | Object Id that holds Id of an object that has change request to be processed. eg: learning_item_id |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Object Type of the current change request |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | Action type of the change request |
| CHANGE_REQUEST_DATE | TIMESTAMP |  |  |  | Object with request effective date to be considered while processing |
| DELETE_EXISTING_CONTENT | VARCHAR2 | 30 |  |  | Flag if we need to delete existing content |
| RESTART_IN_PROG_ATTEMPTS | VARCHAR2 | 30 |  |  | Flag if we need to restart attempts |
| NOTIFY_TARGET_USERS | VARCHAR2 | 30 |  |  | Flag if we job needs toSend notification to target users |
| KEEP_COMPLETIONS | VARCHAR2 | 30 |  |  | Keep Completed enrollments of learning item. |
| NOTIFICATION_MESSAGE | VARCHAR2 | 4000 |  |  | Notification Message to Target users |
| REASON_CODE | VARCHAR2 | 30 |  |  | Reason code for the action chosen |
| REASON_COMMENTS | VARCHAR2 | 4000 |  |  | Comments for the action reason |
| REQUEST_START_DATE | TIMESTAMP |  |  |  | Request start date |
| REQUEST_END_DATE | TIMESTAMP |  |  |  | Request end date |
| REQUEST_JOB_ID | NUMBER |  | 18 |  | ESS request id that processed the change request |
| REQUEST_JOB_CREATED_BY_ID | NUMBER |  | 18 |  | Person Id of User who triggered the Request ESS job |
| REQUEST_RUN_DATE | TIMESTAMP |  |  |  | Request processed date |
| PROCESSING_STATUS | VARCHAR2 | 30 |  |  | Change request status |
| STATUS | VARCHAR2 | 30 |  |  | Status |
| RECONCILE_IMPACT_TYPE | VARCHAR2 | 30 |  |  | Defines if reconcile have major impact |
| PREVIOUS_RELATED_CONTENT_ID | NUMBER |  | 18 |  | Previous effective related content id |
| CREATED_BY_ID | NUMBER |  | 18 |  | Person Id of user who created the change request |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| OBJECT_DETAILS | CLOB |  |  |  | Stores object related info during delete operation. |
| EXCLUDE_FROM_TRANSCRIPT | VARCHAR2 | 30 |  |  | Flag if we need to exclude from transcript |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CHANGE_REQUESTS_N1 | Non Unique | Default | OBJECT_ID |
| WLF_CHANGE_REQUESTS_N2 | Non Unique | Default | OBJECT_TYPE |
| WLF_CHANGE_REQUESTS_N3 | Non Unique | Default | ACTION_TYPE |
| WLF_CHANGE_REQUESTS_N4 | Non Unique | Default | PROCESSING_STATUS |
| WLF_CHANGE_REQUESTS_N5 | Non Unique | Default | REQUEST_JOB_ID |
| WLF_CHANGE_REQUESTS_N6 | Non Unique | Default | CREATED_BY_ID |
| WLF_CHANGE_REQUESTS_N7 | Non Unique | Default | PREVIOUS_RELATED_CONTENT_ID |
| WLF_CHANGE_REQUESTS_U1 | Unique | Default | CHANGE_REQUEST_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
