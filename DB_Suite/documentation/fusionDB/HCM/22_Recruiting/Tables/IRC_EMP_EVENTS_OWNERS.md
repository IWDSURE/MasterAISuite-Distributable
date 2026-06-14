# IRC_EMP_EVENTS_OWNERS

This table stores the owners of the employee events

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventsowners-24527.html#ircempeventsowners-24527](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventsowners-24527.html#ircempeventsowners-24527)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_EVENTS_OWNERS_PK | EMP_EVENT_OWNER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMP_EVENT_OWNER_ID | NUMBER |  | 18 | Yes | Primary Key for this table. This is an auto-generated field. |
| EMP_EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_EMP_EVENTS_B table |
| OWNER_PERSON_ID | NUMBER |  | 18 | Yes | The person id of the owner of the event. Foreign key to PER_PERSONS |
| OWNER_TYPE_CODE | VARCHAR2 | 30 |  |  | The type of the owner, whether its owner or co owner. The values will be 'OWNER', 'CO-OWNER |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_EVENTS_OWNERS_FK1 | Non Unique | Default | EMP_EVENT_ID, OWNER_TYPE_CODE |
| IRC_EMP_EVENTS_OWNERS_FK2 | Non Unique | Default | OWNER_PERSON_ID |
| IRC_EMP_EVENTS_OWNERS_PK | Unique | Default | EMP_EVENT_OWNER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
