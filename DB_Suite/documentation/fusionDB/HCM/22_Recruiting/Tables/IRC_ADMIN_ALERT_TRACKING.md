# IRC_ADMIN_ALERT_TRACKING

This table stores all the email alerts information in recruiting context that were sent to admin.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircadminalerttracking-24044.html#ircadminalerttracking-24044](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircadminalerttracking-24044.html#ircadminalerttracking-24044)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ADMIN_ALERT_TRACKING_PK | ADMIN_ALERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADMIN_ALERT_ID | NUMBER |  | 18 | Yes | Primary Key of  the table. System generated. |
| ALERT_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_ALERTS_B. |
| ALERT_ACTIVITY_CODE | VARCHAR2 | 50 |  | Yes | The code for the type of alert scenario. |
| ALERT_CONTEXT_CODE | VARCHAR2 | 30 |  | Yes | The context in which the Admin alert was sent. |
| ENTITY_TYPE_CODE | VARCHAR2 | 30 |  | Yes | The type of entity that caused the alert trigger. |
| ENTITY_ID | NUMBER |  | 18 |  | The ID of the entity that caused the alert trigger. |
| TRIGGER_THRESHOLD | NUMBER |  | 18 |  | The threshold value at which the alert was triggered. |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  | Yes | The email address of the Admin who was alerted. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ADMIN_ALERT_TRACKING_FK1 | Non Unique | Default | ALERT_ID |
| IRC_ADMIN_ALERT_TRACKING_N1 | Non Unique | Default | ALERT_ACTIVITY_CODE, CREATION_DATE, TRIGGER_THRESHOLD, ENTITY_ID |
| IRC_ADMIN_ALERT_TRACKING_PK | Unique | Default | ADMIN_ALERT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
