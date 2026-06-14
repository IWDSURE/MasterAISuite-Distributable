# IRC_IS_SCHEDULE_MAPPING

IRC_IS_SCHEDULE_MAPPING table stores the list of requisition ids associated to the interview schedules.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisschedulemapping-27937.html#ircisschedulemapping-27937](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisschedulemapping-27937.html#ircisschedulemapping-27937)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_SCHEDULE_MAPPING_PK | SCHEDULE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_MAPPING_ID | NUMBER |  | 18 | Yes | The primary key for this table. |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Foreign key to the associated schedule(IRC_SCHEDULE_B) for this schedule mapping. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Business Object ID - It can be Requisition Id .. etc |
| OBJECT_TYPE | VARCHAR2 | 32 |  | Yes | Business Object Type - It can be ORA_REQUISITION .. etc |
| CREATION_MODE | VARCHAR2 | 64 |  |  | Highlight the way the schedule has been created, either ORA_IS_CREATED_MANUALLY or ORA_IS_CREATED_FROM_DEFAULT_TEMPLATE or ORA_IS_CREATED_FROM_REQ_TEMPLATE. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_SCHEDULE_MAPPING_FK1 | Non Unique | Default | SCHEDULE_ID |
| IRC_IS_SCHEDULE_MAPPING_N1 | Non Unique | Default | OBJECT_TYPE, OBJECT_ID |
| IRC_IS_SCHEDULE_MAPPING_PK | Unique | Default | SCHEDULE_MAPPING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
