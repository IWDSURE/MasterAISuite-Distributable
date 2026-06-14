# PER_NUDGE_CHANNEL_DETAILS

This table records the channel details of the assigned nudges.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgechanneldetails-5165.html#pernudgechanneldetails-5165](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgechanneldetails-5165.html#pernudgechanneldetails-5165)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_CHANNEL_DETAILS_PK | NUDGE_CHANNEL_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NUDGE_CHANNEL_DETAIL_ID | NUMBER |  | 18 | Yes | NUDGE_CHANNEL_DETAIL_ID |
| NUDGE_ID | NUMBER |  | 18 | Yes | NUDGE_ID |
| CHANNEL_TYPE | VARCHAR2 | 30 |  | Yes | CHANNEL_TYPE |
| RECIPIENT_TYPE | VARCHAR2 | 30 |  | Yes | RECIPIENT_TYPE |
| RECIPIENT_PERSON_ID | NUMBER |  | 18 |  | RECIPIENT_PERSON_ID |
| RECIPIENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | RECIPIENT_ASSIGNMENT_ID |
| PLAN_NUDGE_CHANNEL_ID | NUMBER |  | 18 | Yes | PLAN_NUDGE_CHANNEL_ID |
| RUN_ID | NUMBER |  | 18 |  | RUN_ID |
| CHANNEL_STATUS | VARCHAR2 | 30 |  | Yes | CHANNEL_STATUS |
| ERROR_DETAILS | VARCHAR2 | 4000 |  |  | ERROR_DETAILS |
| STATUS_CHANGED_AT | TIMESTAMP |  |  |  | STATUS_CHANGED_AT |
| REMINDER_COUNT | NUMBER |  | 3 |  | REMINDER_COUNT |
| NEXT_REMINDER_DATE | DATE |  |  |  | NEXT_REMINDER_DATE |
| REMINDER_DURATION | NUMBER |  | 3 |  | REMINDER_DURATION |
| DEFER_UNTIL_DATE | DATE |  |  |  | DEFER_UNTIL_DATE |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | OBJECT_TYPE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| WORKFLOW_INSTANCE | VARCHAR2 | 120 |  |  | WORKFLOW_INSTANCE |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_NUDGE_CHANNEL_DETAILS_N1 | Non Unique | Default | NUDGE_ID, CHANNEL_TYPE, RECIPIENT_TYPE |  |
| PER_NUDGE_CHANNEL_DETAILS_N2 | Non Unique | Default | RECIPIENT_PERSON_ID, CHANNEL_TYPE, RECIPIENT_TYPE |  |
| PER_NUDGE_CHANNEL_DETAILS_PK | Unique | Default | NUDGE_CHANNEL_DETAIL_ID |  |
| PER_NUDGE_CHANNEL_DETAILS_U1 | Unique | Default | NUDGE_ID, PLAN_NUDGE_CHANNEL_ID | Obsolete |
| PER_NUDGE_CHANNEL_DETAILS_N3 | Non Unique | Default | NUDGE_ID, PLAN_NUDGE_CHANNEL_ID |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
