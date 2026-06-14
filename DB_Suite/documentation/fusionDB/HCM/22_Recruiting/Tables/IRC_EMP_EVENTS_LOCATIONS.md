# IRC_EMP_EVENTS_LOCATIONS

This table stores the event location related details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventslocations-7054.html#ircempeventslocations-7054](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventslocations-7054.html#ircempeventslocations-7054)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_EVENTS_LOCATIONS_PK | EMP_EVENT_LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMP_EVENT_LOCATION_ID | NUMBER |  | 18 | Yes | Primary Key for this table. This is an auto-generated field. |
| EMP_EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_EMP_EVENTS_B table |
| FORMAT_CODE | VARCHAR2 | 30 |  |  | Indicates if the event is in-person or virtual as a lookup code, ORA_IRC_EMP_EVENT_FORMAT |
| MAX_CAPACITY_INPERSON | NUMBER |  | 10 |  | Max capacity of the In person event in a location |
| MAX_CAPACITY_VIRTUAL | NUMBER |  | 10 |  | Max capacity of the Virtual event in a location |
| COUNTRY_CODE | VARCHAR2 | 30 |  |  | Country code of the Country where event is occurring from HZ_GEOGRAPHIES. |
| STATE_GEOGRAPHY_ID | NUMBER |  | 18 |  | GEOGRAPHY_ID of the State where event is occurring. Foreign key to HZ_GEOGRAPHIES table. |
| CITY_GEOGRAPHY_ID | NUMBER |  | 18 |  | GEOGRAPHY_ID of the City where event is occurring. Foreign key to HZ_GEOGRAPHIES table. |
| LOCATION_DETAILS | CLOB |  |  |  | This column stores the Location Details for In person event |
| WEB_CONF_LINK | VARCHAR2 | 300 |  |  | Web conference link for virtual event |
| MEETING_DETAILS | CLOB |  |  |  | Used to store meeting details of virtual events |
| REGISTERED_COUNT_INPERSON | NUMBER |  | 10 |  | The count of the employees registered for the in_person employee event |
| REGISTERED_COUNT_VIRTUAL | NUMBER |  | 10 |  | The count of the employees registered for the virtual employee event |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_EVENTS_LOCATIONS_FK1 | Non Unique | Default | EMP_EVENT_ID |
| IRC_EMP_EVENTS_LOCATIONS_PK | Unique | Default | EMP_EVENT_LOCATION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
