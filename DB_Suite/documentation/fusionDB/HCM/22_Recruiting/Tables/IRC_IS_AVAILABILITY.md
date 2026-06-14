# IRC_IS_AVAILABILITY

IRC_IS_AVAILABIITY used for storing availability of interviewer

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisavailability-24895.html#ircisavailability-24895](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisavailability-24895.html#ircisavailability-24895)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_AVAILABILITY_PK | AVAILABILITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AVAILABILITY_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated |
| PERSON_ID | NUMBER |  | 18 | Yes | Person_id of the user whose availability is stored. Foreign key to per_persons |
| USE_O365_AVAILABILITY_FLAG | VARCHAR2 | 1 |  | Yes | Stores Y/N for the setting to use O365 availability only |
| DAY_OF_WEEK | VARCHAR2 | 18 |  |  | Lookup code for the weekday. The corresponding Lookup code is ORA_IRC_IS_WEEKDAY |
| IS_AVAILABLE_FLAG | VARCHAR2 | 1 |  |  | Stores Y/N to indicate if the interviewer is available on the day of week |
| START_TIME | TIMESTAMP |  |  |  | Start time of the availability period |
| END_TIME | TIMESTAMP |  |  |  | End time of the availability period |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_AVAILABILITY_FK1 | Non Unique | Default | PERSON_ID |
| IRC_IS_AVAILABILITY_PK | Unique | Default | AVAILABILITY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
