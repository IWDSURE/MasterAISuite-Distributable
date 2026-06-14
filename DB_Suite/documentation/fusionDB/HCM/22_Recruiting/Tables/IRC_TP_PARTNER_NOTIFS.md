# IRC_TP_PARTNER_NOTIFS

This table is used for storing partner notification data to be sent to the partner and the status of the notifications.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctppartnernotifs-23530.html#irctppartnernotifs-23530](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctppartnernotifs-23530.html#irctppartnernotifs-23530)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TP_PARTNER_NOTIFS_PK | NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTIFICATION_ID | NUMBER |  | 18 | Yes | Primary key value of this table. System generated. |
| CATEGORY_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_CATEGORIES_B table. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS table. |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Indicates the action for which the partner should receive notification. |
| ACTION_REASON_CODE | VARCHAR2 | 30 |  |  | Action reason for the action type if applicable. |
| ENTITY_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Indicates the entity type of the action. |
| ENTITY_ID | NUMBER |  | 18 | Yes | Stores Surrogate key of the entity type. |
| ACTION_DATA | CLOB |  |  |  | Additional action data stored in JSON format. |
| ACTION_DATE | TIMESTAMP |  |  | Yes | Action occurrence date in timestamp format. |
| REQUESTED_BY | VARCHAR2 | 64 |  | Yes | Stores the id of the user who triggered the action. |
| NOTIFICATION_STATUS_CODE | VARCHAR2 | 30 |  |  | Status code of the notification. |
| TRY_COUNT | NUMBER |  | 4 |  | This column stores the number of tries made to invoke the partner service. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROCESSING_TIME | NUMBER |  | 18 |  | Time taken to process the row in milliseconds |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TP_PARTNER_NOTIFS_FK1 | Non Unique | Default | CATEGORY_ID |
| IRC_TP_PARTNER_NOTIFS_FK2 | Non Unique | Default | PROVISIONING_ID |
| IRC_TP_PARTNER_NOTIFS_N2 | Non Unique | Default | ENTITY_ID |
| IRC_TP_PARTNER_NOTIFS_N3 | Non Unique | Default | NOTIFICATION_STATUS_CODE, ENTITY_TYPE_CODE |
| IRC_TP_PARTNER_NOTIFS_N4 | Non Unique | Default | NOTIFICATION_STATUS_CODE, NOTIFICATION_ID, TRY_COUNT, REQUEST_ID |
| IRC_TP_PARTNER_NOTIFS_PK | Unique | Default | NOTIFICATION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
