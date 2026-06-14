# PER_NUDGE_PLAN_NDG_CHNLS_B

This table records the nudge channel details for a nudge plan.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanndgchnlsb-28773.html#pernudgeplanndgchnlsb-28773](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanndgchnlsb-28773.html#pernudgeplanndgchnlsb-28773)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_PLAN_NDG_CHNLS_B_PK | PLAN_NUDGE_CHANNEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_NUDGE_CHANNEL_ID | NUMBER |  | 18 | Yes | PLAN_NUDGE_CHANNEL_ID |
| PLAN_NUDGE_CHANNEL_CODE | VARCHAR2 | 240 |  | Yes | PLAN_NUDGE_CHANNEL_CODE |
| PLAN_NUDGE_ID | NUMBER |  | 18 | Yes | PLAN_NUDGE_ID |
| CHANNEL_TYPE | VARCHAR2 | 30 |  | Yes | CHANNEL_TYPE |
| RECIPIENT_TYPE | VARCHAR2 | 30 |  | Yes | RECIPIENT_TYPE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| CONTENT_SOURCE | VARCHAR2 | 30 |  | Yes | CONTENT_SOURCE |
| HEADING_RESOURCE | VARCHAR2 | 240 |  |  | HEADING_RESOURCE |
| TITLE_RESOURCE | VARCHAR2 | 240 |  |  | TITLE_RESOURCE |
| CONTENT_RESOURCE | VARCHAR2 | 240 |  |  | CONTENT_RESOURCE |
| ADDITIONAL_CONTENT1_RESOURCE | VARCHAR2 | 240 |  |  | ADDITIONAL_CONTENT1_RESOURCE |
| ADDITIONAL_CONTENT2_RESOURCE | VARCHAR2 | 240 |  |  | ADDITIONAL_CONTENT2_RESOURCE |
| ACTION_LABEL_RESOURCE | VARCHAR2 | 240 |  |  | ACTION_LABEL_RESOURCE |
| TEMPLATE_ID | NUMBER |  | 18 |  | TEMPLATE_ID |
| CHECKLIST_ID | NUMBER |  | 18 |  | CHECKLIST_ID |
| INITIATOR_PERSON_ID | NUMBER |  | 18 |  | INITIATOR_PERSON_ID |
| DISMISS_FLAG | VARCHAR2 | 4 |  |  | DISMISS_FLAG |
| DEFERRAL_TYPE | VARCHAR2 | 30 |  | Yes | DEFERRAL_TYPE |
| DEFERRAL_DAYS | NUMBER |  | 3 |  | DEFERRAL_DAYS |
| ACTION_TYPE | VARCHAR2 | 30 |  |  | ACTION_TYPE |
| ACTION_CODE | VARCHAR2 | 240 |  |  | ACTION_CODE |
| APPLICATION_TASK_CODE | VARCHAR2 | 240 |  |  | APPLICATION_TASK_CODE |
| ACTION_URL | VARCHAR2 | 400 |  |  | ACTION_URL |
| REPORT_PATH | VARCHAR2 | 400 |  |  | REPORT_PATH |
| REMINDER_FLAG | VARCHAR2 | 4 |  | Yes | REMINDER_FLAG |
| REMINDER_RECURRENCE | VARCHAR2 | 30 |  |  | REMINDER_RECURRENCE |
| REMINDER_DURATION | NUMBER |  | 3 |  | REMINDER_DURATION |
| REMINDER_RELATIVE_TO | VARCHAR2 | 30 |  |  | REMINDER_RELATIVE_TO |
| REMINDER_OFFSET | NUMBER |  | 3 |  | REMINDER_OFFSET |
| REASSIGN_ON_RECIPIENT_CHANGE | VARCHAR2 | 4 |  |  | REASSIGN_ON_RECIPIENT_CHANGE |
| PRIORITY | NUMBER |  | 5 | Yes | PRIORITY |
| GROUP_ID | NUMBER |  | 18 |  | GROUP_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| WORKFLOW_CODE | VARCHAR2 | 200 |  |  | WORKFLOW_CODE |
| WORKFLOW_MESSAGE | VARCHAR2 | 4000 |  |  | WORKFLOW_MESSAGE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_NUDGE_PLAN_NDG_CHNLS_B_N1 | Non Unique | Default | PLAN_NUDGE_ID, CHANNEL_TYPE, RECIPIENT_TYPE |
| PER_NUDGE_PLAN_NDG_CHNLS_B_PK | Unique | Default | PLAN_NUDGE_CHANNEL_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
