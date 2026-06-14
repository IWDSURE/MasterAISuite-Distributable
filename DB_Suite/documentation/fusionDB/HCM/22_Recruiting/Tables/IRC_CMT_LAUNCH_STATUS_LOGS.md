# IRC_CMT_LAUNCH_STATUS_LOGS

This table stores message status logs information for the launch.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunchstatuslogs-16533.html#irccmtlaunchstatuslogs-16533](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunchstatuslogs-16533.html#irccmtlaunchstatuslogs-16533)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CMT_LAUNCH_STATUS_LOGS_PK | STATUS_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STATUS_LOG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| LAUNCH_ID | NUMBER |  | 18 | Yes | Foreign key to irc_cmt_launches table |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores new status of the launch. Stores launch status as a lookup code.The corresponding lookup type is ORA_IRC_CMT_LAUNCH_STATUS_TYPE |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | Stores the ESS Job Request ID of the current launch row |
| ERROR_REASON | CLOB |  |  |  | Stores the reason for error status of the launch. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CMT_LAUNCH_STATUS_LOGS_FK1 | Non Unique | Default | LAUNCH_ID |
| IRC_CMT_LAUNCH_STATUS_LOGS_PK | Unique | Default | STATUS_LOG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
