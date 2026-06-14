# IRC_REC_EVENT_LOC_USAGES

This table stores the event location related details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventlocusages-17386.html#ircreceventlocusages-17386](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventlocusages-17386.html#ircreceventlocusages-17386)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENT_LOC_USAGES_PK | LOCATION_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_USAGE_ID | NUMBER |  | 18 | Yes | Primary Key for this table. This is an auto-generated field. |
| EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REC_EVENTS_B table |
| EVENT_FORMAT_CODE | VARCHAR2 | 30 |  |  | Indicates if the event is in-person or virtual as a look up code, ORA_IRC_REC_EVT_FORMAT |
| LOCATION_ID | NUMBER |  | 18 |  | Location where event is occurring in case of office location. Foreign key to PER_LOCATIONS table. |
| ADDRESS_ID | NUMBER |  | 18 |  | Address of event location in case of in-person event. Foreign key to PER_ADDRESSES_F table |
| LOCATION_TYPE_CODE | VARCHAR2 | 30 |  |  | Indicates whether office location or not. Uses look up type ORA_IRC_REC_EVT_LOC_TYPE. |
| MAX_CAPACITY | NUMBER |  | 9 |  | Max capacity of the event in a location |
| WEB_CONF_LINK | VARCHAR2 | 300 |  |  | Web conference link for virtual event |
| ACCESS_CODE | VARCHAR2 | 60 |  |  | This column stores the access code for virtual event |
| PHONE_NUMBER | VARCHAR2 | 60 |  |  | Phone number in case of virtual event |
| PHONE_AREA_CODE | VARCHAR2 | 30 |  |  | Phone area code in case of virtual event |
| PHONE_COUNTRY_CODE | VARCHAR2 | 30 |  |  | Phone country code in case of virtual event |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LOCATION_FQN_ID | NUMBER |  | 18 |  | Denormalized location id used for event search indexation |
| CITY_ID | NUMBER |  | 18 |  | Denormalized hz_geographies city id used for event search indexation |
| STATE_ID | NUMBER |  | 18 |  | Denormalized hz_geographies state id used for event search indexation |
| COUNTRY_ID | NUMBER |  | 18 |  | Denormalized hz_geographies country id used for event search indexation |
| LATITUDE | NUMBER |  |  |  | Denormalized irc_geo_coordinates Latitude information used for event search indexation |
| LONGITUDE | NUMBER |  |  |  | Denormalized irc_geo_coordinates Longitude information used for event search indexation |
| MEETING_ID | VARCHAR2 | 60 |  |  | Used to store meeting id of virtual events |
| PHONE_LEGISLATION_CODE | VARCHAR2 | 4 |  |  | Used to store legislation code for the event phone number |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENT_LOC_USAGES_FK1 | Non Unique | Default | EVENT_ID |
| IRC_REC_EVENT_LOC_USAGES_FK2 | Non Unique | Default | LOCATION_ID |
| IRC_REC_EVENT_LOC_USAGES_FK3 | Non Unique | Default | ADDRESS_ID |
| IRC_REC_EVENT_LOC_USAGES_PK | Unique | Default | LOCATION_USAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
