# IRC_IS_REQ_AUTO_SCHEDULE

This table stores the automatic interview schedule configuration information

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisreqautoschedule-9820.html#ircisreqautoschedule-9820](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisreqautoschedule-9820.html#ircisreqautoschedule-9820)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_REQ_AUTO_SCHEDULE_PK | SCHEDULE_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Stores ID of the requisition on which the schedule is configured. Foreign key to irc_requisitions_b |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Stores ID of the schedule which is assigned to automatic interview invite action. Foreign key to irc_is_schedules_b |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Stores ID of the action usage at which the automatic interview invite is configured. Foreign key to irc_lc_action_usages_b |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_REQ_AUTO_SCHEDULE_FK2 | Non Unique | Default | SCHEDULE_ID |
| IRC_IS_REQ_AUTO_SCHEDULE_PK | Unique | Default | SCHEDULE_CONFIG_ID |
| IRC_IS_REQ_AUTO_SCHEDULE_U1 | Unique | Default | REQUISITION_ID, STEP_ACTION_USAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
