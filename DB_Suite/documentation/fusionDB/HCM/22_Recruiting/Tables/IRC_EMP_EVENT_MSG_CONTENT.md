# IRC_EMP_EVENT_MSG_CONTENT

This table stores the details of the employee event message content details

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventmsgcontent-9777.html#ircempeventmsgcontent-9777](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventmsgcontent-9777.html#ircempeventmsgcontent-9777)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_EVENT_MSG_CONTENT_PK | CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| ACTION_TRACKING_ID | NUMBER |  | 18 | Yes | Stores ACTION_TRACKING_ID. Foreign key to irc_emp_event_action_trk table. |
| SUBJECT | VARCHAR2 | 2000 |  |  | Stores subject part for the message. |
| BODY | CLOB |  |  |  | Stores body content for the message. |
| TEMPLATE_ID | NUMBER |  | 18 |  | Stores TEMPLATE_ID. Foreign key to hrc_alert_templates_b table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_EVENT_MSG_CONTENT_FK1 | Non Unique | Default | TEMPLATE_ID |
| IRC_EMP_EVENT_MSG_CONTENT_PK | Unique | Default | CONTENT_ID |
| IRC_EMP_EVENT_MSG_CONTENT_U1 | Unique | Default | ACTION_TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
